-- ============================================
-- Схема базы данных для управления студентами
-- Курс: kokk (повар)
-- ============================================

-- Таблица локаций/городов
CREATE TABLE locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE  -- Tallinn, Narva
);

-- Таблица групп/потоков обучения
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,           -- "kokk"
    location_id INTEGER DEFAULT 1, -- Tallinn по умолчанию
    start_date DATE,
    end_date DATE,
    notes TEXT,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

-- Таблица студентов
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Основные данные
    full_name TEXT NOT NULL,           -- Humay Jahagirova
    personal_code TEXT,                -- 49411180072 (isikukood)
    
    -- Связь с группой
    group_id INTEGER,
    list_number INTEGER,               -- Порядковый номер в группе (1, 2, 3...)
    
    -- Контакты студента
    phone TEXT,                        -- 58831254
    email TEXT,
    
    -- Дополнительные контакты (родители, опекуны и т.д.) в формате JSON
    -- Пример: [{"relation": "мама", "name": "Тамара", "phone": "58142224", "email": "tamara@example.com"}]
    additional_contacts JSON,
    
    -- Документы
    document_number TEXT,              -- 7-6.7/25/00098
    
    -- Даты обучения
    start_date DATE,                   -- 17.02.2025
    end_date DATE,                     -- 13.06.2025
    
    -- Статус (для пометок типа "ушла", "WFFF", "390 ak. t.")
    status TEXT DEFAULT 'active',      -- active, completed, dropped, on_leave
    
    -- Сырые данные из CSV (на всякий случай, для аудита)
    raw_data TEXT,
    
    -- Метаданные
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Таблица курсов (для будущего расширения)
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_hours INTEGER
);

-- Таблица преподавателей (для будущего расширения)
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    specialization TEXT
);

-- Связь студентов с курсами (записи на курсы)
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE,
    status TEXT DEFAULT 'active',
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Связь преподавателей с курсами
CREATE TABLE course_teachers (
    course_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, teacher_id),
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE
);

-- Индексы для быстрого поиска
CREATE INDEX idx_students_personal_code ON students(personal_code);
CREATE INDEX idx_students_group ON students(group_id);
CREATE INDEX idx_students_email ON students(email);

-- ============================================
-- Начальные данные
-- ============================================

INSERT INTO locations (name) VALUES 
    ('Tallinn'),
    ('Narva');
