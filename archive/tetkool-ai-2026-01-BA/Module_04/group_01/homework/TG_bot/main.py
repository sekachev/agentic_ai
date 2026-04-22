import os
import json
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from openai import OpenAI

from prompts import get_system_prompt, TOOLS
from tools.search_courses import search_courses
from tools.send_email import send_email

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Initialize OpenAI/OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

llm_model = os.getenv("LLM_MODEL", "google/gemini-2.0-flash-001")

# Store conversation history (in-memory for simplicity)
conversations = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text

    if user_id not in conversations:
        conversations[user_id] = [{"role": "system", "content": get_system_prompt()}]

    conversations[user_id].append({"role": "user", "content": user_text})

    try:
        # 1. First LLM Call
        response = client.chat.completions.create(
            model=llm_model,
            messages=conversations[user_id],
            tools=TOOLS,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        
        # Handle reasoning if present
        reasoning = getattr(response_message, 'reasoning', None)
        if reasoning:
            logging.info(f"LLM Reasoning: {reasoning}")

        tool_calls = response_message.tool_calls

        # 2. Handle Tool Calls
        if tool_calls:
            conversations[user_id].append(response_message)
            
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                logging.info(f"Tool Call: {function_name} with {function_args}")
                
                if function_name == "search_courses":
                    function_response = search_courses(**function_args)
                elif function_name == "send_email":
                    function_response = send_email(**function_args)
                else:
                    function_response = "Unknown function"

                conversations[user_id].append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })

            # 3. Second LLM Call with Tool Results
            second_response = client.chat.completions.create(
                model=llm_model,
                messages=conversations[user_id],
            )
            second_message = second_response.choices[0].message
            final_text = second_message.content
            
            # Check for reasoning in second response
            second_reasoning = getattr(second_message, 'reasoning', None)
            if second_reasoning:
                logging.info(f"LLM Second Reasoning: {second_reasoning}")
        else:
            final_text = response_message.content

        conversations[user_id].append({"role": "assistant", "content": final_text})
        await update.message.reply_text(final_text)

    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("Sorry, I encountered an error processing your request.")

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found in .env")
    else:
        application = ApplicationBuilder().token(token).build()
        
        message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
        application.add_handler(message_handler)
        
        print(f"Bot is running using model {llm_model}...")
        application.run_polling()
