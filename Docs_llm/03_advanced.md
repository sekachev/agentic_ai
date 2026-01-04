# Level 3: Advanced – Customization & Precision

This guide covers precise layout control, custom styling, and advanced configuration.

## 1. Precise Grid Positioning
The `<grid>` tag allows absolute positioning (`drop`) and sizing (`drag`).
- `drag="width height"`: Percentage of slide (e.g., `100 20`).
- `drop="x y"`: Origin point (e.g., `0 10`).

```html
<grid drag="40 100" drop="0 0" bg="gray">
Left Sidebar
</grid>

<grid drag="60 100" drop="40 0">
Main Content Area
</grid>
```

## 2. Styling and Classes
### Element Annotations
Apply CSS classes directly to Markdown elements.
```markdown
# Big Red Title <!-- element class="text-red-500" -->
```

### Inline CSS
Use the `style` attribute.
```markdown
# Custom Style <!-- element style="color: gold; font-family: serif;" -->
```

### Custom CSS (YAML)
Link external CSS files or define it globally in the frontmatter.
```yaml
---
css:
  - "path/to/my-style.css"
---
```

## 3. High-End Components
- **FontAwesome Icons:** Use `:fab-github:` or `:fas-rocket:`.
- **Charts.js:** Create interactive charts via code blocks.
  ```chart
  type: bar
  labels: [Q1, Q2, Q3]
  series:
    - title: Revenue
      data: [100, 200, 150]
  ```
- **Excalidraw:** Embed `.excalidraw` files for hand-drawn diagrams.

## 4. Slide Animations
### Auto-Animate (Smooth Transitions)
If you have two adjacent slides with similar elements, you can animate the transition between them by adding `data-auto-animate` to both slides.

```markdown
<!-- slide data-auto-animate -->
# My Title

---

<!-- slide data-auto-animate -->
# My Title
### Subtitle now appears
```

## 5. Templates
Automate slide structures. Define a template in a separate file and reference it.
- **Global Template:** `defaultTemplate: my-layout` in YAML.
- **Per Slide:** `<!-- slide template="my-layout" -->`.

Templates use placeholders like `<% content %>`.

## 5. Advanced Plugins (YAML)
Enable powerful revealed.js plugins:
- `enableChalkboard`: `true` (adds drawing tools).
- `enableMenu`: `true` (adds a slide selector).
- `enableOverview`: `true` (allows grid view of all slides).
- `autoSlide`: `5000` (auto-advance every 5 seconds).
