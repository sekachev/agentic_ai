# Level 2: Intermediate – Enhancing Your Slides

This guide covers features that add interactivity, structure, and media to your presentations.

## 1. Fragments (Reveal one-by-one)
Fragments allow you to reveal elements sequentially on a single slide.

### Shorthand for Lists (Fastest Way)
Instead of standard bullets, use these symbols to make items appear one by one automatically:
- **Unordered:** Use `+` instead of `-` or `*`.
- **Ordered:** Use `1)` instead of `1.`.

```markdown
# My List
- Permanent point
+ First point to appear
+ Second point to appear

# Ordered List
1. Always visible
2) Step one
3) Step two
```

### Manual Fragments
Add `<!-- element class="fragment" -->` after any block (paragraphs, images, etc.).

```markdown
* Point 1 <!-- element class="fragment" -->
* Point 2 <!-- element class="fragment" -->
```

### Fragment Styles:
- `fade-in`, `fade-out`, `fade-up`, `fade-down`, `zoom-in`, `highlight-red`, `highlight-blue`.

## 2. Layouts
Advanced Slides provides tags to structure the slide area.

### Split Layout
Splits the slide into columns.
```html
<split even gap="3">
![](image1.png)
![](image2.png)
![](image3.png)
</split>
```

### Basic Grid
Provides a 12x12 coordinate system for positioning.
```html
<grid drag="100 50" drop="0 0">
# Top Half
</grid>
<grid drag="100 50" drop="0 50">
# Bottom Half
</grid>
```

## 3. Advanced Markdown Features
- **Callouts:** Standard Obsidian callouts work in slides.
  ```markdown
  > [!info] Tip
  > Use grids for complex layouts.
  ```
- **Mermaid Diagrams:** Fully supported.
  ```mermaid
  graph LR
  A --> B
  ```
- **Math (KaTeX):** Use `$E=mc^2$` for inline or `$$...$$` for blocks.
- **Presenter Notes:** Content after `note:` will only be visible in the speaker view.
  ```markdown
  # Slide Title
  note: Remember to mention the sales figures.
  ```

## 4. Backgrounds
You can set backgrounds per slide using annotations.

```markdown
<!-- slide bg="red" -->
# Red Background

<!-- slide bg="https://example.com/image.jpg" -->
# Image Background
```

## 5. UI Customization (YAML)
- `progress`: `true`/`false` (shows progress bar).
- `controls`: `true`/`false` (shows navigation arrows).
- `slideNumber`: `true`/`false` (shows page numbers).
