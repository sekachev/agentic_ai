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
БЛОК КОДА
```



---
### Как работает API?
стандарт openai
https://platform.openai.com/docs/guides/text?lang=curl
+ какак выглядит запрос
+ как работает ответ
+ openrouter.ai



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
https://artificialanalysis.ai
https://epoch.ai	

---
### Чем пользуются люди?
https://openrouter.ai
---
### Запускаем локальные LLM.
https://hf.co/
https://ollama.com

---
### Квантизация

GLM-4.7 (358B)

| Тип кванта  | Пример $\pi$ | Вес (VRAM + KV Cache) | Цена "железа" | Качество ответов      |
| :---------- | :----------- | :-------------------- | :------------ | :-------------------- |
| **BF16**    | 3.14159265   | **~800 ГБ**           | **$650,000**  | Идеальное (Reference) |
| **Q8_0**    | 3.14159      | **~420 ГБ**           | **$320,000**  | Неотличимо            |
| **Q6_K**    | 3.1415       | **~330 ГБ**           | **$130,000**  | Почти без потерь      |
| **Q4_K_M**  | 3.14         | **~240 ГБ**           | **$100,000**  | **Золотой стандарт**  |
| **IQ3_XXS** | 3.1          | **~165 ГБ**           | **$60,000**   | Заметная деградация   |
| **IQ2_XXS** | 3.0          | **~130 ГБ**           | **$45,000**   | Глупые ошибки         |
| **TQ1_0**   | 1            | **~90 ГБ**            | **$5,000**    | "Белый шум" / Бред    |

---
### Квантизация 1 bit

Веса: [-1, 0, 1]

https://bitnet-demo.azurewebsites.net/

---
### Промпт инжиниринг 
+ Осведомленность (google maps issue)
	+ Unknown unknowns -> Known unknowns
	+ Какие есть пути из А в Б
	+ out of the box thinking
+ Акинатор https://ru.akinator.com
+ Zero-shot
+ One-shot, Few-shot
+ Persona


---
### Промпт инжиниринг 
https://ai.google.dev/gemini-api/docs/prompting-strategies#gemini-3
https://www.kaggle.com/whitepaper-prompt-engineering
  

---
### Function calling
https://platform.openai.com/docs/guides/function-calling


---

### Динамический контекст инжиниринг 

Skills anthtropic
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills


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

```bash 
curl https://openrouter.ai/api/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $OPENROUTER_API_KEY" \
 -d '{ "model": "xiaomi/mimo-v2-flash:free", 
	 "messages": [ 
	 { "role": "system", "content": "You are a friendly, conversational assistant who enjoys lighthearted small talk." }, 
	 { "role": "user", "content": "Hi there! How is your day going?" }, 
	 { "role": "assistant", "content": "It’s going wonderfully! I’m processing data smoothly and feeling ready to help. How about you?" }, 
	 { "role": "user", "content": "I am doing well. I am thinking about making a fruit salad later." }, 
	 { "role": "assistant", "content": "That sounds delicious and refreshing! What kind of fruits are you planning to put in it?" }, 
	 { "role": "user", "content": "I definitely want to add some strawberries. By the way, how many r’s are in the word ‘strawberry’?" } ], 
	 "reasoning": { 
	 "enabled": true } }'
```

