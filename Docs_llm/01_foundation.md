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
