# Level 1: Foundation – Core Architecture & Syntax

Advanced Slides for Obsidian uses Reveal.js. Every presentation starts with a YAML frontmatter block for global configuration.

## 1. YAML Configuration Reference
| Key | Description | Values (Default) |
| :--- | :--- | :--- |
| `theme` | Slide theme | `black`, `white`, `league`, `beige`, `sky`, `night`, `serif`, `simple`, `solarized`, `blood`, `moon` |
| `highlightTheme` | Code block highlighting | `monokai`, `zenburn`, `dracula`, `github`, `vscode` |
| `transition` | Slide transition style | `none`, `fade`, `slide` (def), `convex`, `concave`, `zoom` |
| `transitionSpeed` | Transition speed | `default`, `fast`, `slow` |
| `bg` | Default background | Color (hex/rgb), Image URL, or `transparent` (for OBS) |
| `width` / `height` | Resolution | `960` / `700` |
| `margin` | Content margin | `0.04` |
| `controls` | Nav arrows | `true` (def) / `false` |
| `progress` | Progress bar | `true` (def) / `false` |
| `slideNumber` | Page numbers | `true`, `false`, `c/t`, `h.v` |
| `center` | Vertically center | `true` (def) / `false` |
| `loop` | Loop presentation | `false` (def) / `true` |
| `autoSlide` | Auto advance (ms) | `0` (off) |
| `separator` | Horiz. slide regex | `^---` (surrounded by blank lines) |
| `verticalSeparator` | Vert. slide regex | `^--` (surrounded by blank lines) |
| `defaultTemplate` | Global template | Note name (without [[ ]]) |
| `enableLinks` | Title backlinks | `false` (def) / `true` |
| `notesSeparator` | Speaker notes delim | `note:` (def) |

## 2. Structural Syntax
### Slide Separation
- **Horizontal Slide:** `---` (surrounded by empty lines).
- **Vertical Slide:** `--` (surrounded by empty lines). Vertical slides belong to the preceding horizontal slide.

### Fragments (Sequential Reveal)
- **List Shorthand (Unordered):** Use `+` instead of `-` or `*`.
- **List Shorthand (Ordered):** Use `1)` instead of `1.`.
- **Manual Element Class:** Add `<!-- element class="fragment [variant]" -->` after any block.
  - **Variants:** `fade-in`, `fade-out`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `zoom-in`, `grow`, `shrink`, `highlight-red`, `highlight-blue`, `highlight-green`.

## 3. Standard Markdown & Obsidian Features
- **Highlights:** `==text==`. **Strikethrough:** `~~text~~`.
- **Images:** `![alt|100x100](url)` or `[[image.png|100]]`.
- **Links:** `[label](url)` or `[[Note Name]]`.
- **Blockquotes:** `> quote`. **Footnotes:** `[^1]` ... `[^1]: text`.
- **LaTeX:** Inline `$x^2$` or block `$$E=mc^2$$`.
- **Embeds:** `![[Note Name]]` injects full note content. Use `![[Note#Section]]` for precision.
- **Videos:** Supports `![[video.mp4]]`, YouTube, and Vimeo.

## 4. Preview & Rendering
- **Open Preview:** Use the Obsidian Command Palette (`Ctrl/Cmd + P`) and search for `Advanced Slides: Open Preview` or click the slide icon in the ribbon.
- **Navigation:** Use `Arrow Keys`, `Space`, or `PgUp/PgDown`. Press `ESC` or `O` for overview.

## 5. Quick Quickstart Example
```markdown
---
theme: night
transition: slide
---

# Slide 1 (Horizontal)
A basic slide.

---

# Slide 2 (Horizontal)
This slide has bullet points appearing one by one:
+ Point A
+ Point B

--

# Slide 2.1 (Vertical child)
This is a vertical sub-slide.
```
