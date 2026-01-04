# Source: https://mszturc.github.io/obsidian-advanced-slides/extend-syntax/blockcomment

You can use block comments to group parts of your slide. By annotating the block all items inside this block gets the properties of the annotation:

```
::: block
#### Header
_and_
Paragraph content
*in same block*
:::
---
no color
::: block <!-- element style="background-color: red;" -->
everything inside this block has red background color
::: block <!-- element style="background-color: blue;" -->
blue
:::
red
:::
no color
```