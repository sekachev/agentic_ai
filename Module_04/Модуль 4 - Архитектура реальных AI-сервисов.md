
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

<grid drag="45 60" drop="2 15" align="top">
<i class="fas fa-desktop fa-3x"></i>
<br>

### FRONTEND
+ <span style="color:orange">Интерфейс</span>: Chat UI, Стриминг
+ <span style="color:orange">UX</span>: Обработка событий
+ <span style="color:orange">Клиент</span>: Ввод данных
</grid>

<grid drag="45 60" drop="53 15" align="top">
<i class="fas fa-server fa-3x"></i>
<br>

### BACKEND
+ <span style="color:orange">Оркестрация</span>: LLM & Tools
+ <span style="color:orange">Безопасность</span>: API Keys
+ <span style="color:orange">Память</span>: БД & Контекст
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
<i class="fas fa-running fa-7x"></i>

## edusport.neuro.ee
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-car-side fa-7x"></i>

## ruttu.ee
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-microscope fa-7x"></i>

## ai.evc.ee
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-file-invoice fa-7x"></i>

## dunven.neuro.ee
</split>

---

<split left="1" right="2" gap="2">
<i class="fas fa-database fa-7x"></i>

## dims.neuro.ee
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

- Репозиторий: [github.com/sekachev/agentic_ai](https://github.com/sekachev/agentic_ai)
