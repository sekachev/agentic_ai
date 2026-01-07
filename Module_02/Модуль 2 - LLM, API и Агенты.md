## Модуль 2 - LLM, API и Агенты

---
### Минутка философии


---
### Что дает нам предсказание следующего слова?

+ https://www.youtube.com/watch?v=2YzLMPm3Jgw


---
### Как работает LLM? 
[[https://openrouter.ai/]]-> F12

---
### Как работает LLM? 

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
  "model": "xiaomi/mimo-v2-flash:free",
  "messages": [
    {
      "role": "user",
      "content": "Скажи привет!"
    }
  ],
  stream: false,
  "reasoning": {
    "enabled": false
  }
}'
```


---
### Что такое JSON? 

JSON (JavaScript Object Notation) — это формат обмена данными между клиентом и сервером.	

```json
{
"group": "AI-2026/01", 
"students": ["Ольга", "Татьяна"],
"active": true
}
```

```
Основные элементы:
`{ }` — Объект (набор пар "ключ: значение")
`[ ]` — Массив (упорядоченный список значений)
`"key"` — Ключ (всегда строка в двойных кавычках)
`"value"` — Значение (строка, число, объект, массив, `true`, `false` или `null`)
`:` — Разделитель между ключом и значением
`,` — Разделитель между элементами
```

---
### Что такое JSON? 

```json
{
  "model": "gpt-4o",
  "messages": [
	  {"role": "system", "content": "Ты кот"},
	  {"role": "user", "content": "Скажи мяу?"}
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
+ Top-K (Фильтр по количеству)
+ Top-P (Фильтр по вероятности)
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
+ Token Limit
+ structured output



---
### Открытые и закрытые модели:
https://epoch.ai	
https://artificialanalysis.ai


---
### Квантизация

| Тип кванта          | Пример $\pi$ (точность) | Вес модели (VRAM) | Кол-во RTX 3090 (24GB) | Примерная цена железа (только GPU)* | Качество ответов     |
| :------------------ | :---------------------- | :---------------- | :--------------------- | :---------------------------------- | :------------------- |
| **BF16** (Original) | 3.14159265              | **717 ГБ**        | **32 шт.**             | **$25,000 - $35,000**               | Идеальное (Эталон)   |
| **Q8_0** (8-bit)    | 3.14159                 | **381 ГБ**        | **17 шт.**             | **$13,000 - $17,000**               | Неотличимо от BF16   |
| **Q6_K** (6-bit)    | 3.1415                  | **294 ГБ**        | **13 шт.**             | **$10,000 - $13,000**               | Почти без потерь     |
| **Q4_K_M** (4-bit)  | 3.14                    | **216 ГБ**        | **10 шт.**             | **$8,000 - $10,000**                | **Золотой стандарт** |
| **IQ3_XXS** (3-bit) | 3.1                     | **145 ГБ**        | **7 шт.**              | **$5,500 - $7,000**                 | Заметная деградация  |
| **IQ2_XXS** (2-bit) | 3.0                     | **116 ГБ**        | **5 шт.**              | **$4,000 - $5,000**                 | Глупые ошибки        |
| **TQ1_0** (1-bit)   | 1                       | **84.5 ГБ**       | **4 шт.**              | **$3,200 - $4,000**                 | "Белый шум" / Бред   |


---
### Чем пользуются люди?
https://openrouter.ai


---
### Как работает API?
стандарт openai
https://platform.openai.com/docs/guides/text?lang=curl
+ какак выглядит запрос
+ как работает ответ
+ openrouter.ai



---
### Промпт инженеринг 
+ Задавать правильные вопросы
	+ Deep Knowledge + Vocabulary = The Ability to Direct AI.
+ Unknown unknowns
+ Zeros-shot
+ Few-shot
+ Persona


---
### Промпт инженеринг 
https://ai.google.dev/gemini-api/docs/prompting-strategies#gemini-3
https://www.kaggle.com/whitepaper-prompt-engineering
  



---
### Function calling
https://platform.openai.com/docs/guides/function-calling




---
### Agentic AI
https://www.youtube.com/watch?v=EDb37y_MhRw



---
### Agentic AI


  ```
  
Prompt  ──────▶  ACTIONS



		   PERCEIVE
		 (Восприятие)
		 ↗          ↘
	  LEARN        DECIDE
	(Обучение)    (Принятие решений)
		 ↖          ↙
		   EXECUTE
		 (Выполнение)


```

---
### Vending bench 
https://andonlabs.com/evals/vending-bench-2


---
### Antigravity
https://antigravity.google/



---
### MCP
- https://modelcontextprotocol.io/docs/learn/architecture


---
### Skills anthtropic
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills