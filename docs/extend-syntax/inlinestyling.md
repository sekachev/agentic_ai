# Source: https://mszturc.github.io/obsidian-advanced-slides/extend-syntax/inlinestyling

you may define css styles inside your markdown:

```
<style>
.with-border{
border: 1px solid red;
}
</style>
styled text <!-- element class="with-border" -->
```


it is possible to add further css files beside theme and highlight theme to slide deck:

```
---
css: [css/layout.css,css/customFonts.css]
---
```