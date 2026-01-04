# Obsidian Advanced Slides Documentation

## Table of Contents
- [Level 1: Foundation – Setup & Core Syntax](#level-1-foundation-setup-core-syntax)
    - [1. Initial Setup](#1-initial-setup)
    - [2. Slide Separation](#2-slide-separation)
    - [3. Basic Markdown Enhancements](#3-basic-markdown-enhancements)
        - [Text Styling & Comments](#text-styling-comments)
        - [Lists (Standard)](#lists-standard)
        - [Images & Media](#images-media)
    - [4. Themes & Customization](#4-themes-customization)
    - [5. Keyboard Shortcuts (In Browser)](#5-keyboard-shortcuts-in-browser)
- [Level 2: Intermediate – Layouts & Animations](#level-2-intermediate-layouts-animations)
    - [1. Fragments (Step-by-Step Reveals)](#1-fragments-step-by-step-reveals)
        - [Shorthand for Lists (Fastest Way)](#shorthand-for-lists-fastest-way)
        - [Manual Fragments & Classes](#manual-fragments-classes)
    - [2. Structural Layouts](#2-structural-layouts)
        - [Split Layout (Columns)](#split-layout-columns)
        - [Basic Grid Layout](#basic-grid-layout)
    - [3. Visual Enhancements](#3-visual-enhancements)
        - [Backgrounds](#backgrounds)
        - [Auto-Animate (Smooth Transitions)](#auto-animate-smooth-transitions)
    - [4. Rich Media & Plugins](#4-rich-media-plugins)
- [Level 3: Advanced – Precision, Templates & Plotting](#level-3-advanced-precision-templates-plotting)
    - [1. Absolute Grid Positioning (The 100x100 System)](#1-absolute-grid-positioning-the-100x100-system)
    - [2. Advanced Styling](#2-advanced-styling)
        - [Element Annotations](#element-annotations)
        - [Fragment Sequences](#fragment-sequences)
    - [3. reusable Templates](#3-reusable-templates)
    - [4. Advanced Components](#4-advanced-components)
    - [5. Global Config (Advanced YAML)](#5-global-config-advanced-yaml)

---

# Level 1: Foundation – Setup & Core Syntax

This guide covers the essential setup and fundamental syntax for creating presentations using the **Advanced Slides** plugin in Obsidian.

## 1. Initial Setup
A slide deck is a standard Markdown file in Obsidian. It must begin with a YAML frontmatter block for configuration.

```yaml
---
theme: night            # Options: black, white, league, beige, sky, night, serif, simple, solarized, blood, moon
highlightTheme: monokai # Code block style (zenburn, monokai, etc.)
transition: slide       # none, fade, slide, convex, concave, zoom
transitionSpeed: fast   # default, fast, slow
controls: true          # Show navigation arrows
progress: true          # Show progress bar
slideNumber: true       # Show slide numbers
---
```

## 2. Slide Separation
- **Horizontal Slide:** Use `---` surrounded by empty lines.
- **Vertical Slide:** Use `--` surrounded by empty lines.
- **Speaker Notes:** Use `note:` at the end of a slide. Notes are visible in the "Speaker View" (press `S` in browser).

```markdown
# Slide 1

---

# Slide 2.1 (Horizontal)
note: Remind everyone about the goals.

--

# Slide 2.2 (Vertical child of 2.1)
```

## 3. Basic Markdown Enhancements
Standard Obsidian Markdown works, but with presentation-specific optimizations:

### Text Styling & Comments
- `==highlighted==`, `~~strikethrough~~`, `**bold**`, `*italic*`.
- `%%Comment%%`: Hidden in the presentation.

### Lists (Standard)
- Bullet points (`-`, `+`, `*`) and numbered lists (`1.`).

### Images & Media
- **Standard:** `![Alt](url)`
- **Obsidian Internal:** `![[image.png]]`
- **Resizing:** `![[image.png|300]]` (sets width to 300px).
- **Video:** Use HTML for control: `<video data-autoplay src="file.mp4"></video>`.

## 4. Themes & Customization
- **Built-in Themes:** `black`, `white`, `league`, `beige`, `sky`, `night`, `serif`, `simple`, `solarized`, `blood`, `moon`, `dracula`.
- **Custom Theme:** Place CSS in your vault and reference it: `theme: css/my-theme.css`.
- **Global CSS:** Add a CSS array to YAML:
  ```yaml
  css:
    - "styles/custom.css"
  ```

## 5. Keyboard Shortcuts (In Browser)
After clicking "Open in Browser":
- `F`: Fullscreen.
- `S`: Speaker View (with notes and timer).
- `O`: Overview Mode (grid of all slides).
- `ESC`: Exit Overview mode.
- `?`: Show help menu.
- `ALT + Click`: Zoom into an element.

---

# Level 2: Intermediate – Layouts & Animations

This guide covers features that add structure, visual flow, and interactivity to your slides.

## 1. Fragments (Step-by-Step Reveals)
Fragments allow you to reveal elements one by one.

### Shorthand for Lists (Fastest Way)
Use these symbols to make items appear one by one automatically:
- **Unordered:** Use `+` instead of `-` or `*`.
- **Ordered:** Use `1)` instead of `1.`.

```markdown
# My List
- This item is always visible
+ Then this one appears
+ And finally this one
```

### Manual Fragments & Classes
Annotate any element with `<!-- element class="fragment STYLE" -->`.
- **Styles:** `fade-in`, `fade-out`, `zoom-in`, `highlight-red`, `highlight-green`, `highlight-blue`.

```markdown
# Surprise! <!-- element class="fragment zoom-in" -->
```

## 2. Structural Layouts
Advanced Slides uses `<split>` and `<grid>` tags for layout.

### Split Layout (Columns)
Divides the slide area into columns automatically.
```html
<split even gap="2">
# Left Column
Detailed text or code here.

# Right Column
![[diagram.png]]
</split>
```
- `even`: Distributes space equally.
- `gap`: Margin between columns (1-5).

### Basic Grid Layout
Uses a 12x12 relative coordinate system.
```html
<grid drag="50 100" drop="0 0">
## Left Half
</grid>
<grid drag="50 100" drop="50 0">
## Right Half
</grid>
```

## 3. Visual Enhancements
### Backgrounds
Set backgrounds per slide using annotations:
```markdown
<!-- slide bg="red" -->
<!-- slide bg="[[background.jpg]]" opacity="0.5" -->
<!-- slide bg="https://picsum.photos/1000" -->
```

### Auto-Animate (Smooth Transitions)
Animates matching elements between adjacent slides. Use `data-auto-animate` on both slides.
```markdown
<!-- slide data-auto-animate -->
# My Component

---

<!-- slide data-auto-animate -->
### Smaller Now
# My Component
```

## 4. Rich Media & Plugins
- **Callouts:** Standard Obsidian callouts (e.g., `> [!tip]`) are rendered beautifully.
- **Mermaid Diagrams:** Create flowcharts and diagrams directly.
- **Math (LaTeX):** Use `$E=mc^2$` or `$$...$$` blocks.
- **Chalkboard:** Allow drawing on slides. (Enable via YAML: `enableChalkboard: true`). Use `B` to toggle chalkboard, `C` to toggle notes canvas.

---

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
