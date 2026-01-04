# LLM Presentation Guide: Obsidian Advanced Slides

This is an enriched, condensed guide for LLMs (and power users) to master the **Advanced Slides** plugin in Obsidian. Each guide is designed to be comprehensive yet under 200 lines.

## 🗺️ Documentation Map

### [01_foundation.md](./01_foundation.md) - Level 1: Essentials
**Focus:** Infrastructure, basic styling, and presentation control.
- **Key Concepts:** YAML Frontmatter (themes, transitions, settings), Horizontal/Vertical slide separators, Obsidian internal links/embeds, and browser shortcuts.
- **When to Use:** Setting up a new deck or basic text-focused presentations.

### [02_features.md](./02_features.md) - Level 2: Interactivity
**Focus:** Enhancing dynamic flow and media.
- **Key Concepts:** Fragments (shorthand `+`/`)`), Auto-animate, Split layouts (columns), Backgrounds, Callouts, Mermaid, and the Chalkboard plugin.
- **When to Use:** Standard professional decks needing diagrams and step-by-step logic reveals.

### [03_advanced.md](./03_advanced.md) - Level 3: Precision & Logic
**Focus:** Structural perfection and advanced data.
- **Key Concepts:** Absolute 100x100 Grid positioning, reusable Templates with variables (`::: block`), Fragment indexing, interactive Charts, and advanced YAML settings.
- **When to Use:** Custom-branded templates, complex multi-box layouts, and data-driven presentations.

---

## ⚡ Quick Lookup

| Task | Syntax / Keyword | Level |
| :--- | :--- | :--- |
| **New Slide** | `---` (surrounded by empty lines) | 1 |
| **Speaker Notes** | `note: my note` | 1 |
| **One-by-one List** | Use symbols `+` or `1)` | 2 |
| **Two Columns** | `<split even>` ... `</split>` | 2 |
| **Exact Positioning** | `<grid drag="W H" drop="X Y">` | 3 |
| **Smooth Movement** | `<!-- slide data-auto-animate -->` | 2 |
| **Reusable Layout** | `<!-- slide template="[[note-name]]" -->` | 3 |
| **Interactive Chart** | ` ```chart ` block | 3 |
| **Drawing Tool** | `enableChalkboard: true` (YAML) | 2 |

---

## Technical Specs
- **Engine:** Reveal.js
- **Parser:** Marked.js
- **Icons:** FontAwesome 5
- **Charts:** Chart.js
- **Coordinate System:** Percentage based (0-100) for width/height and x/y.
