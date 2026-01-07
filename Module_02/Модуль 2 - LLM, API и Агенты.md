### Минутка философии


---
### Что дает нам предсказание следующего слова?
Стивен Джобс


---
### Как работает LLM? 
[[ChatGPT.com]]  -> F12


---
### Что такое JSON? 

JSON (JavaScript Object Notation) — это формат обмена данными между клиентом и сервером.	

```json
{"user": "Ivan", "roles": ["admin", "editor"], "active": true}
```
**Основные элементы:**
- `{ }` — **Объект** (набор пар "ключ: значение")
- `[ ]` — **Массив** (упорядоченный список значений)
- `"key"` — **Ключ** (всегда строка в двойных кавычках)
- `"value"` — **Значение** (строка, число, объект, массив, `true`, `false` или `null`)
- `:` — **Разделитель** между ключом и значением
- `,` — **Разделитель** между элементами

---
### Что такое JSON? 

```json
{
  "model": "gpt-4o",
  "messages": [
    {"role": "user", "content": "Как дела?"}
  ],
  "temperature": 0.7
}
```


---
### Что такое Markdown? 

**Markdown** — это облегченный язык разметки, максимально читабельный и удобный для правки текста, легко конвертируется в HTML.

```markdown
# Заголовок
## Подзаголовок
**жирный**
[aistudio](aistudio.google.com)

```

---
### Что такое Markdown? 

**Основные элементы:**
```markdown
`#` — Заголовки (от `#` до `######`)
`** **` или `__ __` — **Жирный текст**
`* *` или `_ _` — *Курсив*
`[Текст](URL)` — [Ссылка](https://google.com)
`-` или `*` — Маркированный список
`1.` — Нумерованный список
`> ` — Цитата
` ``` ` — Блок кода (например, для JSON):
```


---
### Как работает трансформер?
- Векторное представление
+ Порядок слов
+ Механизм внимания
+ Feed Forward Perceptron
+ итог - распределение вероятностей
+ Температура (softmax)
+ system instructions
+ Grant Sanderson (https://www.youtube.com/watch?v=LPZh9BOjkQs)


---
### Размышления модели - зачем? и как управлять?
	<thought> ... </thought> 
	<reasoning> ... </reasoning> 


---
### Что нам важно знать и запомнить?
- Stateless (как растет бутерброд)
+ Ограниченный контекст
+ Какой тип данных принимает в контекст?
+ Ограниченная выдача
+ Какой тип данных может возвращать?
+ Галлюцинации
+ Температура (softmax)
+ Top-K (Фильтр по количеству)
+ Top-P (Фильтр по вероятности)
+ Token Limit
+ structured output



---
### Открытые и закрытые модели:
- EPOCH.ai
- artificialanalysis.ai


---
### Чем пользуются люди?
- openrouter.ai


---
### Как работает API?
- стандарт openai
- какак выглядит запрос
- как работает ответ
- openrouter.ai



---
### Промпт инженеринг 
- Asking right questions
- Deep Knowledge + Vocabulary = The Ability to Direct AI.
- Unknown unknowns
- Zeros-shot
- Few-shot
- Persona
- https://ai.google.dev/gemini-api/docs/prompting-strategies#gemini-3
- https://www.kaggle.com/whitepaper-prompt-engineering
  



---
### Function calling
- https://platform.openai.com/docs/guides/function-calling





---
### Agentic AI
- https://www.youtube.com/watch?v=EDb37y_MhRw
- **AI Agent** = LLM + Memory + Agent Skills + Tools (MCP) + Planning.


---
### Vending bench 
- https://andonlabs.com/evals/vending-bench-2


---
### Antigravity
https://antigravity.google/



---
### MCP
- https://modelcontextprotocol.io/docs/learn/architecture


---
### Skills anthtropic
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills












---
### Как устроен черный ящик? (40 минут)
- 	- векторное представление + работа с векторами
	- порядок слов (плачет наша маша горько)
	- соседние слова (плачет наша маша)
	- вероятностное распределние / температура / top-p, top-k 
	- что "закодировано" в весах---
### Как нам превратить это в ассистента? (20 минут) /системный запрос/
---
### Что мы получим в итоге? 
	- stateless (ретроградная амнезия)
	- ограничен контекст
	- ограничена выдача
	- галюцинации (когда попали а там ничего нет)
---
### API 
	- как работает web-интерфейс LLM
	- посмотрим на запросы модели
	- попробуем отправить запрос напрямую


