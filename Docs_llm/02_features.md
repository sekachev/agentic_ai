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
