# Source: https://mszturc.github.io/obsidian-advanced-slides/basic-syntax/mermaid

```
---
theme: beige
highlightTheme: css/vs2015.css
---
```mermaid
sequenceDiagram
Alice->>+John: Hello John, how are you?
Alice->>+John: John, can you hear me?
John-->>-Alice: Hi Alice, I can hear you!
John-->>-Alice: I feel great!
```
```


![Mermaid](https://mszturc.github.io/obsidian-advanced-slides/images/mermaid.png)


```
---
theme: beige
highlightTheme: css/vs2015.css
---
#### Gitgraph Diagrams support
```mermaid
gitGraph
commit
commit
branch develop
checkout develop
commit
commit
checkout main
merge develop
commit
commit
```
```


![Gitgraph](https://mszturc.github.io/obsidian-advanced-slides/images/gitgraph.png)


It’s possivle to overload the default mermaid configuration to change the behaviour / layout of the rendered mermaid diagrams. Do do this add a mermaid property to yaml as following:

mermaid: themeVariables: fontSize: 32px theme: ‘forest’

```
---
mermaid:
themeVariables:
fontSize: 32px
theme: 'forest'
---
```