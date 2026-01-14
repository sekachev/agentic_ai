
# Модуль 4: Архитектура реальных AI-сервисов

---

<grid drag="100 100" drop="center">
![[module_4_cover.png]]
</grid>

---

## Структура модуля

+ <span style="color:orange">Frontend vs Backend</span>: Разделение ответственности
+ <span style="color:orange">Case Studies</span>: Разбор реальных проектов
+ <span style="color:orange">Architectural Tracing</span>: Проектирование систем
+ <span style="color:orange">Practice</span>: Сборка MVP

---

## Блок 1: Frontend vs Backend в AI
### Почему мы разделяем логику?

---

<grid drag="48 60" drop="2 20" align="top" bg="rgba(0,0,0,0.1)" pad="20px" border="1px solid #444">
<i class="fas fa-desktop fa-3x" style="color:#00d4ff"></i>
<br>

### FRONTEND
+ **Интерфейс**: Chat UI, Стриминг
+ **UX**: Обработка событий
+ **Клиент**: Ввод данных
</grid>

<grid drag="48 60" drop="50 20" align="top" bg="rgba(0,0,0,0.1)" pad="20px" border="1px solid #444">
<i class="fas fa-server fa-3x" style="color:#00d4ff"></i>
<br>

### BACKEND
+ **Оркестрация**: LLM & Tools
+ **Безопасность**: API Keys
+ **Память**: БД & Контекст
</grid>

---

<grid drag="100 80" drop="0 20" style="zoom: 1.8;">
```mermaid
sequenceDiagram
    autonumber
    participant U as USER
    participant F as FRONTEND
    participant B as BACKEND
    participant L as LLM / TOOLS

    U->>F: Message
    F->>B: API Request
    B->>L: Prompt
    L-->>B: Response
    B-->>F: Stream
    F-->>U: Display
```
</grid>

---

## Блок 2: Разбор реальных кейсов
### Экосистема прикладных решений

---

<split left="1" right="2" gap="2">
<i class="fas fa-running fa-5x"></i>

### edusport.neuro.ee
**Спортивные тренировки**
+ **Задача**: Умная запись. 
+ **AI-Агент**: Обрабатывает запросы на естественном языке и интегрируется с календарями.
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-car-side fa-5x"></i>

### ruttu.ee
**Умный дневник поездок**
+ **Задача**: Автозаполнение отчетности.
+ **AI-Агент**: Превращает GPS-данные в осмысленные отчеты для бухгалтерии.
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-microscope fa-5x"></i>

### ai.evc.ee
**Vision для медицины**
+ **Задача**: Анализ фото вен.
+ **AI-Агент**: Мультимодальный анализ изображений + сопоставление с базой знаний.
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-file-invoice fa-5x"></i>

### dunven.neuro.ee
**OCR & Structured Data**
+ **Задача**: JPG в Excel.
+ **AI-Агент**: Извлекает таблицы и данные с гарантированной структурой через JSON mode.
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-database fa-5x"></i>

### dims.neuro.ee
**Data Enrichment**
+ **Задача**: Разметка БД.
+ **AI-Агент**: Пакетная обработка тысяч строк для категоризации и поиска инсайтов.
</split>

---

## Architectural Tracing
### Как спроектировать свой сервис?

1. **Input**: Какие данные мы получаем? (Voice, Image, Text)
2. **Reasoning**: Сколько шагов нужно ИИ? (ReAct, Planning)
3. **Execution**: Какие инструменты вызвать? (Search, SQL, Python)
4. **Output**: В каком виде отдать результат? (JSON, Report, Plot)

---

## Практика: Проектирование MVP

**Задание**:
Выберите бизнес-задачу и нарисуйте схему взаимодействия:
+ `User` -> `Frontend` -> `Backend` -> `LLM` -> `Execution` -> `Result`

---

## Итоги модуля

+ **Separation of Concerns**: Фронт для людей, Бэк для безопасности.
+ **Data-First**: Архитектура строится вокруг потоков данных.
+ **Agentic Patterns**: Реальный сервис — это всегда агентная логика.

---

## Ресурсы
- Портал: [neuro.ee](https://neuro.ee)
- Репозиторий: [github.com/sekachev/agentic_ai](https://github.com/sekachev/agentic_ai)
