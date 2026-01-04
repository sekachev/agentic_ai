# Source: https://mszturc.github.io/obsidian-advanced-slides/extend-syntax/fragments

Fragments are used to highlight or incrementally reveal individual elements on a slide. Every element with the class fragment will be stepped through before moving on to the next slide.
The default fragment style is to start out invisible and fade in. This style can be changed by appending a different class to the fragment.


```
Fade in <!-- element class="fragment" -->
Fade out <!-- element class="fragment fade-out" -->
Highlight red <!-- element class="fragment highlight-red" -->
Fade in, then out <!-- element class="fragment fade-in-then-out" -->
Slide up while fading in <!-- element class="fragment fade-up" -->
---
- Permanent item
- Appear Fourth <!-- element class="fragment" data-fragment-index="4" -->
- Appear Third <!-- element class="fragment" data-fragment-index="3" -->
- Appear Second <!-- element class="fragment" data-fragment-index="2" -->
- Appear First <!-- element class="fragment" data-fragment-index="1" -->
```