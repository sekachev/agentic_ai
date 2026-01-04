# Source: https://mszturc.github.io/obsidian-advanced-slides/extend-syntax/fragmentedlists

Based on the Fragments concept Advanced Slides introduced a convention to automatically add fragment annotation to bullet points of ordered and unordered lists. By using `+`

or `)`

as indicator for a list, the list will be automatically displayed as a fragmented list.

```
# Unordered list
- First
- Second
- Third
---
# Fragmented unordered list
- Permanent
+ First
+ Second
+ Third
---
# Ordered list
1. First
2. Second
3. Third
---
# Fragmented ordered list
1. Permanent
2) Second
3) Third
4) Fourth
```