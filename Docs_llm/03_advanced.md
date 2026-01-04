# Level 3: Advanced – Precision, Templates & Plotting

Mastering absolute positioning, repeatable templates, and complex data visualization.

## 1. Absolute Grid Positioning (The 100x100 System)
For total layout control, use `<grid>` with percentage-based coordinates.
- `drag="width height"`: Area size (0-100).
- `drop="x y"`: Position from top-left (0-100) or keywords (`top`, `bottom`, `left`, `right`, `center`).
- `bg="color"`: Add a background color to the block.
- `align="left|right|top|bottom"`: Content alignment inside the block.
- `pad="20px"`: Inner padding.

```html
<grid drag="100 10" drop="top" bg="gray" align="center">
# Header Title
</grid>

<grid drag="40 70" drop="5 20" bg="white" pad="30px">
Left Content Box
</grid>

<grid drag="40 70" drop="55 20" bg="white" pad="30px">
Right Content Box
</grid>
```

## 2. Advanced Styling
### Element Annotations
Attach CSS classes or styles to ANY element.
```markdown
# Blue Title <!-- element class="text-blue" -->
This is small <!-- element style="font-size: 0.5em;" -->
```

### Fragment Sequences
Control the order and behavior of fragments.
```markdown
1. First <!-- element class="fragment" data-fragment-index="2" -->
2. Second <!-- element class="fragment" data-fragment-index="1" --> 
```
*(Result: 2 appears before 1)*

## 3. reusable Templates
Define complex layouts as templates in separate files (e.g., `tpl-footer.md`).

**Template File (`tpl-footer.md`):**
```markdown
<% content %>
<grid drag="100 10" drop="bottom">
<% footer %>
</grid>
```

**Usage in Presentation:**
```markdown
<!-- slide template="[[tpl-footer]]" -->
# Main Content here...
::: footer
Copyright 2024
:::
```
Use `<%? footer %>` (the `?`) to make a variable optional.

## 4. Advanced Components
- **FontAwesome Icons:** `:fas-rocket:`, `:fab-github:`, `:far-envelope:`.
- **Charts:** Create interactive Chart.js visualizations.
  ```chart
  type: bar
  labels: [Jan, Feb, Mar]
  series:
    - title: Revenue
      data: [10, 20, 15]
  ```
- **Excalidraw:** Embed live drawings that remain editable: `![[my-drawing.excalidraw]]`.

## 5. Global Config (Advanced YAML)
- `autoSlide: 5000`: Auto-advance slides every 5s.
- `loop: true`: Restart presentation at the end.
- `parallaxBackgroundImage`: Add a moving background.
- `enableMenu: true`: Show a sidebar table of contents.
- `enableTimeBar: true`: Show a countdown timer bar.
