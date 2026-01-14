
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

<grid drag="100 20" drop="0 10">
## Хранение данных: Client-Side
</grid>

<grid drag="100 70" drop="0 35">
+ <span style="color:orange">LocalStorage / SessionStorage</span>: Быстрое хранение строк (настройки, токены).
+ <span style="color:orange">OPFS</span>: Origin Private File System — быстрая файловая БД в браузере.


---

<grid drag="100 20" drop="0 10">
## Хранение в облаке (BaaS)
</grid>

<grid drag="45 60" drop="2 32" align="top">
<i class="fas fa-bolt fa-3x"></i>
<br>

### SUPABASE
+ Полноценный <span style="color:orange">PostgreSQL</span> база данных
</grid>

<grid drag="45 60" drop="53 32" align="top">
<i class="fas fa-cloud fa-3x"></i>
<br>

### CLOUDFLARE
+ <span style="color:orange">D1</span>: SQL-база
+ <span style="color:orange">R2</span>: Объектное хранилище
</grid>

---

<grid drag="100 20" drop="0 10">
## REST API & Deployment
</grid>

<grid drag="100 70" drop="0 32">
1. **Server-Side**: Разработка API на <span style="color:orange">FastAPI</span> (Python) или <span style="color:orange">Express</span> (Node.js).
2. **VPS (Virtual Private Server)**: Аренда своего сервера (Ubuntu) для полного контроля.
3. **Reverse Proxy**: Настройка <span style="color:orange">Nginx</span> для маршрутизации и SSL (HTTPS).
4. **DevOps**: Контейнеризация и автоматизация деплоя.
</grid>


---

## Итоги модуля

+ **Separation of Concerns**: Фронт для людей, Бэк для безопасности.
+ **Data-First**: Архитектура строится вокруг потоков данных.
+ **Persistence**: Правильный выбор между клиентским хранением и облачными БД.
+ **Agentic Patterns**: Реальный сервис — это всегда агентная логика.

---

## Ресурсы

- Репозиторий: [github.com/sekachev/agentic_ai](https://github.com/sekachev/agentic_ai)
