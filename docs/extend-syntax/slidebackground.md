# Source: https://mszturc.github.io/obsidian-advanced-slides/extend-syntax/slidebackground

you can change the background by annotating the slide:

```
<!-- slide bg="aquamarine" -->
## Slide with text based background
---
<!-- slide bg="#ff0000" -->
## Slide with hex based background
---
<!-- slide bg="rgb(70, 70, 255)" -->
## Slide with rgb based background
---
<!-- slide bg="hsla(315, 100%, 50%, 1)" -->
## Slide with hsl based background
---
# Slide without background
---
<!-- slide bg="https://picsum.photos/seed/picsum/800/600" -->
## Slide with image background
---
<!-- slide bg="[[image.jpg]]" -->
## Slide with image background #2
---
<!-- slide bg="https://picsum.photos/seed/picsum/800/600" data-background-opacity="0.5" -->
## with opacity
0.5 ≙ 50% opacity
---
## More options:
See [reveal backgrounds](https://revealjs.com/backgrounds/)
```


You can change the background of all slides by adding the following frontmatter:

```
---
bg: red
---
```


```
---
bg: '#ff0000'
---
```


```
---
bg: rgb(70, 70, 255)
---
```


You can also set the background to transparent for all slides. This is especially useful if you want to use your slides as overlay source for OBS.

```
---
bg: transparent
---
```