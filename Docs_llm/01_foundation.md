# Level 1: Foundation – Basic Obsidian Slides

This guide covers the essential core of creating presentations in Obsidian using the **Advanced Slides** plugin.

## 1. Core Structure
Each presentation starts with a YAML frontmatter block for configuration.

```yaml
---
theme: night
title: My First Presentation
---
```

### Slide Separation
- **Horizontal Slide:** Separate with `---` (three dashes) on its own line surrounded by empty lines.
- **Vertical Slide:** Separate with `--` (two dashes) on its own line surrounded by empty lines.

```markdown
# Slide 1 (Horizontal)

---

# Slide 2.1 (Horizontal)

--

# Slide 2.2 (Vertical child of 2.1)
```

## 2. Basic Markdown Components
Standard Obsidian/Markdown syntax works out of the box.

- **Headers:** `# Heading 1`, `## Heading 2`, etc.
- **Text Styles:** `*italic*`, `**bold**`, `==highlight==`, `~~strikethrough~~`.
- **Lists:**
  - `* Bullet point`
  - `1. Numbered point`
- **Blockquotes:** `> This is a quote.`
- **Images:** 
  - Standard: `![Alt Text](url)`
  - Obsidian internal: `![[image.png]]`
  - Resizing: `![[image.png|100]]` (width 100px)

## 3. Links & Embeds
- **Links:** `[Text](url)` or `[[Internal Link]]`.
- **Embeds:** `![[Note Name]]` will embed the content of another note as a slide component.

## 4. Key YAML Settings (Common)
Add these to the top of your file:
- `theme`: `black`, `white`, `league`, `beige`, `sky`, `night`, `serif`, `simple`, `solarized`, `blood`, `moon`.
- `highlightTheme`: Style for code blocks (e.g., `monokai`, `zenburn`).
- `transition`: `none`, `fade`, `slide`, `convex`, `concave`, `zoom`.

## 5. Preview & Rendering
- Toggle the **Advanced Slides Preview** in Obsidian (usually via the ribbon icon or command palette `Advanced Slides: Open Preview`).
