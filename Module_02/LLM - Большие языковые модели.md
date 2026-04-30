
---
# LLM - Большие языковые модели

---
# Генеративные модели

```
Данные -> Модель -> Предсказание
```

Модель из двух параметров

---
# Большие языковые модели

https://www.youtube.com/watch?v=YYjlCrpH2is

---
# Архитектура трансформера

![[Pasted image 20260429231730.png]]
- Черный ящик, который предсказывает слово


 https://poloclub.github.io/transformer-explainer/



---
# Визуализация

https://youtu.be/LPZh9BOjkQs?si=RvgFpLBA1Sx9a5Mw&t=277


---
# Что такое токен?
	
 Не слова, а токены https://platform.openai.com/tokenizer

переводим токены в векторы (пространство смыслов) https://projector.tensorflow.org/?utm_source=chatgpt.com

---
# Арифметические операции с векторами

--- 


---
# Completion vs. Chat

Лучший фильм про звездные войны это ________

---
# Насколько модели умные?

https://math.sekachev.ee
https://chat.sekachev.ee

---
# Какая модель самая умная?
https://artificialanalysis.ai/



--- 

# Модели с открытыми весми

Open-source  https://artificialanalysis.ai/models/open-source

Quantization hf.co

---
# Способность к рассуждению

- Reasoning
---
# Размер модели vs Знания

![[telegram-cloud-photo-size-2-5447143194744264082-y.jpg]]


---
# Галюцинации
![[Pasted image 20260429225206.png]]



# LLM не про решение новых задач! 

---

![[Pasted image 20260430085610.png]]

---
![[Pasted image 20260430085808.png]]


---



---
# Ограничения 
- вход (запрос) - 1m
- выход (генерация) - 64k

---
## Эффективность
![[xiaomi-open-sources-mimo-v2-5-ai-models-with-mit-license-v0-78wwi9e3zrxg1.webp]]

---
# Цена

[openrouter](https://openrouter.ai/rankings) 

---
# Проблема stateless
ретроградная амнезия
Context management

---
# Нам нужны действия

function calling
