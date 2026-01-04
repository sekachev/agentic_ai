# Level 2: Features – Complex Layouts & Media

Advanced Slides provides two primary systems for layout: `<grid>` (absolute/coordinate) and `<split>` (proportional/flex).

## 1. Grid Component (`<grid>`)
Highly precise 100x100 relative coordinate system.
**Syntax:** `<grid drag="W H" drop="X Y" [attributes]> content </grid>`

### Core Attributes
- `drag`: Width and Height in % of slide (e.g., `50 100`).
- `drop`: Position X and Y. Positive (from top-left) or Negative (from bottom-right).
  - **Named Positions:** `top`, `bottom`, `left`, `right`, `topleft`, `topright`, `bottomleft`, `bottomright`, `center`.
- `flow`: `col` (vertical stack) or `row` (horizontal stack).
- `bg`: Background color/hex. `border`: `width style color` (e.g., `2px solid white`).
- `align`: `left`, `right`, `center`, `justify`, `stretch` (horizontal alignment).
- `justify-content`: `start`, `end`, `center`, `space-between`, `space-around`, `space-evenly`.
- `pad`: CSS Padding (e.g., `20px 10px`). `rotate`: Degrees (0-360).
- `opacity`: `0.0`-`1.0`. `filter`: CSS filters (e.g., `blur(5px)`, `grayscale()`).
- `animate`: `type speed` (e.g., `fadeIn slow`). `frag`: Sequential reveal index.

## 2. Split Component (`<split>`)
Flex-based relative layout. **Syntax:** `<split [attributes]> content </split>`

### Core Attributes
- `even`: Distributes available width evenly between all children.
- `gap`: Spacing between elements (in em).
- `left` / `right`: Width ratios (e.g., `left="2" right="1"` makes left twice as wide).
- `wrap`: Number of children per row before breaking (e.g., `wrap="3"`).
- `no-margin`: Removes automatic spacing between items.

## 3. High-Order Components
- **Callouts:** Standard Obsidian `> [!type]`. Types: note, info, todo, tip, success, question, warning, failure, danger, bug, example, quote.
- **Mermaid:** Use code blocks ` ```mermaid `. Supports graphs, flowchart, sequence, gantt, pie, etc.
- **Charts:**
  - **JSON/YAML:** ` ```chart type: bar labels: [A,B] series: [{title: T, data: [1,2]}] ``` `
  - **Canvas:** `<canvas data-chart="line"> <!-- JSON config --> </canvas>`
- **Presenter Notes:** Content after `note:` at the end of a slide is visible only in Speaker View (`S`).
- **Embedded Slides:** Embed specific pages from another deck:
  ```slide
  { "slide": [[Presentation]], "page": "3/6" }
  ```
- **External Media:** Render images from URLs or URLs to videos (mp4, webm).

## 4. Practical Layout Recipes

### Side-by-Side Images (Split)
```html
<split even gap="2">
![[img1.png]]
![[img2.png]]
</split>
```

### Centered Content Box (Grid)
```html
<grid drag="60 40" drop="center" bg="gray" pad="20px" border="5px solid white">
### Important Note
This box is centered and has a border.
</grid>
```

### Bottom Summary Bar (Grid)
```html
<grid drag="100 10" drop="bottom" bg="rgba(0,0,0,0.5)">
Summary: Key takeaway here.
</grid>
```
