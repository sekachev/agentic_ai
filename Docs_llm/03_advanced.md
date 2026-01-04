# Level 3: Advanced – Customization & Extensions

## 1. Annotations (Targeted Styling)
Apply attributes directly to Markdown elements (`<!-- element ... -->`) or the whole slide (`<!-- slide ... -->`).

### Element Annotations
Must follow the targeted element immediately.
- `class`, `style`, `color`, `align`, `drag`, `drop`, `bg`.
- `<!-- element class="fragment" -->` reveals the element on click.

### Slide Annotations
Placed at the top of the slide.
- `bg`, `transition`, `transitionSpeed`, `template`.
- `data-auto-animate`: Enables smooth transitions for matched elements on adjacent slides.

## 2. Media & Design
- **FontAwesome Icons:**
  - **Syntax:** `:fas_rocket:`, `:fab_github:`.
  - **HTML:** `<i class="fas fa-camera fa-2x fa-spin"></i>`.
  - **Modifers:** `fa-xs`, `fa-lg`, `fa-2x`...`fa-7x` (sizing); `fa-rotate-90`, `fa-flip-horizontal` (rotation); `fa-spin`, `fa-pulse` (animation); `fa-pull-left`, `fa-border`.
- **Excalidraw:** Embed live editable diagrams: `![[diagram.excalidraw]]`.
- **Emojis:** Syntax `:smile:`, `:heart:`.

## 3. Plugins & Interactivity (YAML)
- `enableChalkboard`: Whiteboard (`B`) and Chalkboard (`C`).
- `enableMenu`: Slide search menu (`M`).
- `enableOverview`: Slide grid view (`ESC` / `O`).
- `enableTimeBar`: Visual countdown bar based on `timeForPresentation` (seconds).
- `enablePointer`: Red laser pointer on hover.

## 4. Templates
Notes in the templates folder containing `<% content %>` placeholders.
- **Global:** `defaultTemplate: name` in frontmatter.
- **Per Slide:** `<!-- slide template="name" -->`.
- **Slots:** Define slots in template (`<% slot1 %>`) and use in slide:
  ```markdown
  %% slot1 %%
  Content here
  ```

## 5. CSS & Customization
- **External CSS:** YAML `css: [ "path/to/local.css", "https://url.css" ]`.
- **Vault Themes:** Place `.css` in `.obsidian/plugins/obsidian-advanced-slides/css/` and load via `theme: css/name.css`.
- **Standard Classes:** `text-left`, `text-center`, `text-right`, `text-justify`.
- **Fragment Classes:** `fade-in`, `fade-out`, `zoom-in`, `grow`, `shrink`, `highlight-red`.

## 6. Advanced Usage Recipes

### Auto-Animate Movement
```markdown
<!-- slide data-auto-animate -->
### Step 1
<grid drag="20 20" drop="topleft" bg="blue"></grid>

---

<!-- slide data-auto-animate -->
### Step 2
<grid drag="20 20" drop="bottomright" bg="blue"></grid>
```

### Styled Element with Annotation
```markdown
# Warning Message <!-- element class="fragment zoom-in" style="color: red; font-size: 4em;" -->
```

### Multi-Slot Template Usage
```markdown
<!-- slide template="two-columns" -->
%% slot-left %%
### Pros
+ Speed
+ Control

%% slot-right %%
### Cons
- Learning curve
```
