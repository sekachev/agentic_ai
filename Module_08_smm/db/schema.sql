-- 1. БАЗА ЗНАНИЙ (Стратегия, Tone of Voice, информация о компании)
CREATE TABLE knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL, -- 'strategy', 'company_info', 'smm_rules'
    topic TEXT NOT NULL, -- 'mission', 'target_audience', 'formatting_rules'
    content TEXT NOT NULL, -- Текст инструкции или информации
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. ОБЪЕКТЫ (Курсы и преподаватели)
-- Чтобы LLM знала детали о том, что она рекламирует
CREATE TABLE entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL, -- 'course', 'teacher', 'service'
    name TEXT NOT NULL, -- Название курса или имя учителя
    details_ru TEXT, -- Описание на русском
    details_et TEXT, -- Описание на эстонском
    price_info TEXT, -- Цены, инфо про Töötukassa
    cta_link TEXT, -- Ссылка на сайт Profftech.ee
    is_active INTEGER DEFAULT 1 -- 1 = актуально, 0 = в архиве
);

-- 3. ИНФОПОВОДЫ (Сырые входные данные)
-- Сюда записываются конкретные события: "Старт курса через неделю", "Новый отзыв"
CREATE TABLE raw_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_text TEXT NOT NULL, -- "Открыта регистрация на поваров на эстонском"
    occurrence_date DATE, -- Когда событие произойдет
    priority INTEGER DEFAULT 2, -- Приоритет (1 - высокий, 3 - низкий)
    status TEXT DEFAULT 'new', -- 'new', 'used', 'ignored'
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 4. КОНТЕНТ-ПЛАН (Стратегический уровень на неделю)
CREATE TABLE content_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    week_start_date DATE NOT NULL,
    main_focus TEXT,              -- Главная цель недели (например, "Продажа языковых курсов")

-- JSON-поле со структурой недели:
-- [{"day": 1, "topic": "...", "goal": "...", "format": "post/reels"}, ...]
weekly_structure_json TEXT,   
    
    status TEXT DEFAULT 'planning' -- 'planning', 'ready', 'completed'
);

-- 5. ПОСТЫ (Операционный уровень - конкретный контент)
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,              -- Связь с планом недели
    event_id INTEGER,             -- Связь с инфоповодом (если есть)
    platform TEXT NOT NULL,       -- 'Facebook', 'Instagram'
    publish_date DATETIME,        -- Запланированная дата публикации

-- Контент (Двуязычный подход)
text_ru TEXT, -- Текст на русском (генерируется первым)
text_et TEXT, -- Текст на эстонском (генерируется вторым)
final_post_text TEXT, -- Склеенный текст (RU + ET) готовый к публикации

-- Медиа и Промпты
media_url TEXT, -- Ссылка на картинку/видео в облаке/папке
image_gen_prompt TEXT, -- Промпт для генерации визуала (DALL-E/Midjourney)

-- Воркфлоу (Стадии готовности)
-- 'draft_ru'      - написан только русский текст
-- 'translated'    - добавлен эстонский текст
-- 'approved'      - проверено человеком
-- 'scheduled'     - стоит в очереди на публикацию (Buffer/API)
-- 'published'     - успешно опубликован
-- 'error'         - ошибка публикации
status TEXT DEFAULT 'draft_ru',
    
    external_id TEXT,             -- ID поста в соцсети после публикации
    FOREIGN KEY (plan_id) REFERENCES content_plans(id) ON DELETE SET NULL,
    FOREIGN KEY (event_id) REFERENCES raw_events(id) ON DELETE SET NULL
);