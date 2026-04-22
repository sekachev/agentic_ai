require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const winston = require('winston');

// Load roles
const rolesPath = path.join(__dirname, 'roles.json');
const roles = JSON.parse(fs.readFileSync(rolesPath, 'utf8'));

// Configure logger
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    winston.format.printf(({ timestamp, level, message }) => {
      return `${timestamp} [${level.toUpperCase()}]: ${message}`;
    })
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'bot.log' })
  ]
});


// Load configuration
const token = process.env.TELEGRAM_BOT_TOKEN;
const openRouterKey = process.env.OPENROUTER_API_KEY;
const model = process.env.OPENROUTER_MODEL || 'google/gemini-2.0-flash-exp:free';

if (!token || !openRouterKey) {
  console.error('Error: TELEGRAM_BOT_TOKEN and OPENROUTER_API_KEY must be provided in .env');
  process.exit(1);
}


// Create bot
const bot = new TelegramBot(token, { polling: true });

// Set bot commands menu
bot.setMyCommands([
  { command: '/start', description: 'Запустить бота' },
  { command: '/role', description: 'Выбрать роль' },
  { command: '/summary', description: 'Показать саммари переписки' }
]);

logger.info('Bot is starting...');


// Simple in-memory storage for chat history
const sessions = new Map();

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Привет! Я бот с поддержкой ролей. Используй /role чтобы выбрать мою личность или просто начни общаться.');
});

bot.onText(/\/role/, (msg) => {
  const chatId = msg.chat.id;
  const keyboard = {
    inline_keyboard: Object.keys(roles).map(roleKey => [
      { text: roleKey.charAt(0).toUpperCase() + roleKey.slice(1), callback_data: `role:${roleKey}` }
    ])
  };
  bot.sendMessage(chatId, 'Выберите роль:', { reply_markup: keyboard });
});

bot.on('callback_query', (query) => {
  const chatId = query.message.chat.id;
  const data = query.data;

  if (data.startsWith('role:')) {
    const roleKey = data.split(':')[1];
    if (roles[roleKey]) {
      if (!sessions.has(chatId)) {
        sessions.set(chatId, {
          role: roleKey,
          messages: [{ role: 'system', content: roles[roleKey] }]
        });
      } else {
        const session = sessions.get(chatId);
        session.role = roleKey;
        // Добавляем новую системную инструкцию в историю, чтобы модель сменила поведение, но помнила контекст
        session.messages.push({ role: 'system', content: `[SYSTEM: Role changed] ${roles[roleKey]}` });
      }

      bot.answerCallbackQuery(query.id, { text: `Роль изменена на ${roleKey}` });
      bot.sendMessage(chatId, `Теперь я буду отвечать в роли: ${roleKey}\n*(Контекст сохранен, роль обновлена)*`, { parse_mode: 'Markdown' });
    }
  }
});

bot.onText(/\/summary/, async (msg) => {
  const chatId = msg.chat.id;
  const session = sessions.get(chatId);

  if (!session || session.messages.length <= 1) {
    bot.sendMessage(chatId, 'У нас еще недостаточно сообщений для саммари.');
    return;
  }

  bot.sendChatAction(chatId, 'typing');

  try {
    const summaryPrompt = "Сделай краткое саммари нашей переписки выше. Выдели основные темы и выводы.";
    const historyForSummary = [...session.messages, { role: 'user', content: summaryPrompt }];

    const response = await axios.post('https://openrouter.ai/api/v1/chat/completions', {
      model: model,
      messages: historyForSummary,
    }, {
      headers: {
        'Authorization': `Bearer ${openRouterKey}`,
        'Content-Type': 'application/json',
      }
    });

    const summary = response.data.choices[0].message.content;
    bot.sendMessage(chatId, `📝 *Саммари нашей переписки:*\n\n${summary}`, { parse_mode: 'Markdown' });
  } catch (error) {
    logger.error(`Error generating summary for UserID ${chatId}: ${error.message}`);
    bot.sendMessage(chatId, 'Не удалось создать саммари.');
  }
});

bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  if (!text || text.startsWith('/')) return;

  // Show typing status
  bot.sendChatAction(chatId, 'typing');

  try {
    // Get or create session history
    if (!sessions.has(chatId)) {
      sessions.set(chatId, { role: 'default', messages: [{ role: 'system', content: roles.default }] });
    }
    const session = sessions.get(chatId);

    // Ensure system prompt is set if history was somehow empty
    if (session.messages.length === 0) {
      session.messages.push({ role: 'system', content: roles[session.role] || roles.default });
    }

    session.messages.push({ role: 'user', content: text });

    // Limit history size (keep system prompt + last 10 messages)
    if (session.messages.length > 11) {
      session.messages.splice(1, 2);
    }

    // Call OpenRouter
    const response = await axios.post('https://openrouter.ai/api/v1/chat/completions', {
      model: model,
      messages: session.messages,
    }, {
      headers: {
        'Authorization': `Bearer ${openRouterKey}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://github.com/sekachev/test_tg_bot',
        'X-Title': 'Test Telegram Bot',
      }
    });

    const aiResponse = response.data.choices[0].message.content;

    // Save to history
    session.messages.push({ role: 'assistant', content: aiResponse });

    // Send response back
    bot.sendMessage(chatId, aiResponse);

    // Logging
    logger.info(`UserID: ${chatId} | Role: ${session.role} | Message: "${text}" | Response: "${aiResponse.replace(/\n/g, ' ')}"`);

  } catch (error) {
    const errorMsg = error.response ? JSON.stringify(error.response.data) : error.message;
    logger.error(`Error calling OpenRouter for UserID ${chatId}: ${errorMsg}`);
    bot.sendMessage(chatId, 'Извините, произошла ошибка при обработке вашего запроса.');
  }
});

process.on('SIGINT', () => {
  bot.stopPolling();
  process.exit();
});
