# Prompting Guide - FLUX.2 [klein]

> Master narrative prompting for FLUX.2 [klein] - scene-first prose, lighting mastery, and multi-reference composition

**FLUX.2 \[klein]** works best when you describe scenes like a novelist, not a search engine. Write flowing prose with lighting details, and the model delivers.

<Note>
  **No prompt upsampling**: \[klein] does not auto-enhance your prompts. What you write is what you get—so be descriptive.
</Note>

## Write Like a Novelist

Describe your scene as flowing prose—subject first, then setting, details, and lighting. This gives \[klein] clear relationships between elements.

<Frame caption="'A woman with short, blonde hair is posing against a light, neutral background. She is wearing colorful earrings and a necklace, resting her chin on her hand. The image has a soft, warm tone with a minimalist style.'">
  <img src="https://cdn.sanity.io/images/2gpum2i6/production/f7cdfd2dfc5436562eb94175b667eb5e467f65e9-1440x2048.jpg" alt="Portrait with soft, warm tone" />
</Frame>

<CardGroup cols={2}>
  <Card title="Do this">
    *"A woman with short, blonde hair is posing against a light, neutral background. She is wearing colorful earrings and a necklace, resting her chin on her hand."*
  </Card>

  <Card title="Not this">
    *"woman, blonde, short hair, neutral background, earrings, colorful, necklace, hand on chin, portrait, soft lighting"*
  </Card>
</CardGroup>

## Basic Prompt Structure

Use this framework for reliable results:

> **Subject → Setting → Details → Lighting → Atmosphere**

| Element        | Purpose                     | Example                                                           |
| -------------- | --------------------------- | ----------------------------------------------------------------- |
| **Subject**    | What the image is about     | "A weathered fisherman in his late sixties"                       |
| **Setting**    | Where the scene takes place | "stands at the bow of a small wooden boat"                        |
| **Details**    | Specific visual elements    | "wearing a salt-stained wool sweater, hands gripping frayed rope" |
| **Lighting**   | How light shapes the scene  | "golden hour sunlight filters through morning mist"               |
| **Atmosphere** | Mood and emotional tone     | "creating a sense of quiet determination and solitude"            |

## Lighting: The Most Important Element

Lighting has the single greatest impact on \[klein] output quality. Describe it like a photographer would.

<Tip>
  Instead of "good lighting," write "soft, diffused light from a large window camera-left, creating gentle shadows that define the subject's features."
</Tip>

<Columns cols={3}>
  <Frame caption="Soft diffused light">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/f7cdfd2dfc5436562eb94175b667eb5e467f65e9-1440x2048.jpg" alt="Portrait with soft, warm tone" />
  </Frame>

  <Frame caption="Dramatic side lighting">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/42594ec152e6f787b655e73c21497b4c3a8f1f4c-1440x2048.jpg" alt="Architecture with dramatic light and shadow" />
  </Frame>

  <Frame caption="Golden hour backlight">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/6594468e7f7c7e2e177489422e3091c5543dc5cf-1440x2048.jpg" alt="Lioness with cubs in golden savanna light" />
  </Frame>
</Columns>

**What to describe:**

* **Source**: natural, artificial, ambient
* **Quality**: soft, harsh, diffused, direct
* **Direction**: side, back, overhead, fill
* **Temperature**: warm, cool, golden, blue
* **Interaction**: catches, filters, reflects on surfaces

**Example lighting phrases:**

* "soft, diffused natural light filtering through sheer curtains"
* "dramatic side lighting creating deep shadows and highlights"
* "golden hour backlighting with lens flare"
* "overcast light creating even, shadow-free illumination"

## Word Order Matters

\[klein] pays more attention to what comes first. Front-load your most important elements.

**Priority**: Main subject → Key action → Style → Context → Secondary details

<Columns cols={2}>
  <div>
    **Strong word order**:

    *"An elderly woman with silver hair carefully arranges wildflowers in a ceramic vase. Soft afternoon light streams through lace curtains, casting delicate shadows across her focused expression."*

    Subject and action lead.
  </div>

  <div>
    **Weak word order**:

    *"In a warm, nostalgic room with antique furniture, soft afternoon light streams through lace curtains. An elderly woman with silver hair is there arranging wildflowers."*

    Subject buried in description.
  </div>
</Columns>

## Prompt Length

| Length     | Words   | Best For                                  |
| ---------- | ------- | ----------------------------------------- |
| **Short**  | 10-30   | Quick concepts, style exploration         |
| **Medium** | 30-80   | Most production work                      |
| **Long**   | 80-300+ | Complex editorial, detailed product shots |

<Warning>
  Longer prompts work well **when every detail serves the image**. Avoid filler — each sentence should add visual information.
</Warning>

### Style and Mood Annotations

Adding explicit style and mood descriptors at the end of your prompt can enhance consistency:

```
[Scene description]. Style: Country chic meets luxury lifestyle editorial.
Mood: Serene, romantic, grounded.
```

```
[Scene description]. Shot on 35mm film (Kodak Portra 400) with shallow
depth of field—subject razor-sharp, background softly blurred.
```

<Columns cols={3}>
  <Frame caption="1990s fashion editorial">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/ad3f43a52bdf1b82350e58da90d50d0122b8dc14-1440x2048.jpg" alt="Model on exercise ball in 1990s editorial style" />
  </Frame>

  <Frame caption="Surreal interior">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/dd1aa1741cc7a7e8149672f0aa65fc326561bbc6-1440x2048.jpg" alt="Two bison in stylized modern room with blue walls" />
  </Frame>

  <Frame caption="Golden hour silhouette">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/a182f770a402a3b318336d6156b5eb1dd8c80cec-1440x2048.jpg" alt="Musician silhouette against glowing orange sunset" />
  </Frame>
</Columns>

<Columns cols={3}>
  <Frame caption="Moody cityscape">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/daf268981d2956540a29d703e176b9fd78196a57-1440x2048.jpg" alt="Silhouette figure against city skyline at dusk" />
  </Frame>

  <Frame caption="Anime fantasy">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/f654ad9e8da73342e63d6f24df030ebb07836e18-1440x2048.jpg" alt="Anime dragon in nocturnal forest with neon glow" />
  </Frame>

  <Frame caption="Whimsical illustration">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/5834b78b879b5c775569a8ebf22c8dcfd0d04f26-1440x2048.jpg" alt="Wolf wearing sheep costume, whimsical style" />
  </Frame>
</Columns>

## Image Editing

For image editing, prompts describe the transformation you want. Focus on what changes while letting the input image(s) provide the foundation.

<Info>
  **Key principle**: Reference images carry visual details. Your prompt describes what should change or how elements should combine—not what they look like.
</Info>

### Single-Image Editing

| Edit Type               | Prompt Pattern                           | Example                                       |
| ----------------------- | ---------------------------------------- | --------------------------------------------- |
| **Style transfer**      | "Turn into \[style]"                     | "Reskin this into a realistic mountain vista" |
| **Object swap**         | "Replace \[element] with \[new element]" | "Replace the bike with a rearing black horse" |
| **Element replacement** | "Replace \[element] with \[new element]" | "Replace all the feathers with rose petals"   |
| **Add elements**        | "Add \[element] to \[location]"          | "Add small goblins climbing the right wall"   |
| **Environmental**       | "Change \[aspect] to \[new state]"       | "Change the season to winter"                 |

<Columns cols={2}>
  <Frame caption="Input">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/00f3de86b945fb15ebf80fedb73bf25613a6cc63-627x1115.jpg" alt="Original abstract artwork" />
  </Frame>

  <Frame caption="'Reskin this into a realistic mountain vista'">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/ff9926cc9f8fda72cef2423a74bb8837aa2a1b42-624x1104.jpg" alt="Mountain vista transformation" />
  </Frame>
</Columns>

<Columns cols={2}>
  <Frame caption="Input">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/59fdd6b45c1d2d4180390ae98380a9425ce8bd99-765x956.jpg" alt="Person on motorcycle" />
  </Frame>

  <Frame caption="'Replace the bike with a rearing black horse'">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/95be0d8eeab9acdd7cdfb73d68120385050b7073-752x944.jpg" alt="Person on rearing black horse" />
  </Frame>
</Columns>

<Columns cols={2}>
  <Frame caption="Input">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/479b03e2cc5bbdf7f56151ec6dce055cb7dfe11a-688x1028.jpg" alt="Portrait with feathers" />
  </Frame>

  <Frame caption="'Replace all the feathers with rose petals'">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/3cc63c124d2a504a6f1e021948bc69db41b05731-688x1024.jpg" alt="Portrait with rose petals" />
  </Frame>
</Columns>

### Multi-Reference Editing

Combine multiple input images for style transfer and complex edits. When using multiple references, specify the role of each.

<Columns cols={3}>
  <Frame caption="Input image 1">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/180cc9fd3e9f0eec754ef37589b684a40bcc0b9d-928x1160.jpg" alt="Original portrait" />
  </Frame>

  <Frame caption="Input image 2">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/e6cad35aca762e8366936aeb5db0c59066e18f7e-776x1163.jpg" alt="Style reference portrait" />
  </Frame>

  <Frame caption="'Change image 1 to match the style of image 2. Make the woman's hair just as fluffy'">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/7188619d7197dc221a16b7714b5437a669538889-928x1152.jpg" alt="Styled portrait with fluffy hair" />
  </Frame>
</Columns>

<Columns cols={3}>
  <Frame caption="Style reference 1">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/842d103f8ab340c59f7712f31e8b577164a59669-624x886.jpg" alt="Style reference image 1" />
  </Frame>

  <Frame caption="Style reference 2">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/30b6023828796bda6ee7fa00573fa2ec10cdd5fd-442x882.jpg" alt="Style reference image 2" />
  </Frame>

  <Frame caption="'Image of the Black Forest. Use the style from the reference images.'">
    <img src="https://cdn.sanity.io/images/2gpum2i6/production/d54cbfb55aedda4ed947e8076b965a510be852ab-950x676.jpg" alt="Black Forest in combined style" />
  </Frame>
</Columns>

### Writing Effective Prompts

<Tip>
  Be **specific** about what changes and **clear** about the target state. Reference image locations when needed (e.g., "image 1", "image 2") and let the base image provide context.
</Tip>

<CardGroup cols={2}>
  <Card title="Good prompts">
    * "Add dramatic storm clouds to the sky"
    * "Change her dress from blue to deep burgundy"
    * "Age this portrait by 30 years"
    * "Change image 1 to match the style of image 2"
  </Card>

  <Card title="Avoid">
    * "Make it better"
    * "Improve the lighting"
    * "Make it more professional"
    * "Fix the image"
  </Card>
</CardGroup>

## Model Variants

| Variant         | Speed      | License             | Best For                                              |
| --------------- | ---------- | ------------------- | ----------------------------------------------------- |
| **\[klein] 4B** | Sub-second | Apache 2.0          | High-volume workflows, local deployment (\~13GB VRAM) |
| **\[klein] 9B** | Sub-second | FLUX Non-Commercial | Production work, best prompt understanding            |
| **Base 4B/9B**  | Standard   | Same as above       | Fine-tuning, research (undistilled, higher diversity) |

<Info>
  **Try \[klein] via API** — Get started in minutes with sub-second generation. No GPU required. [View API docs →](/flux_2/flux2_text_to_image#klein-integration)
</Info>

<Note>
  API models (4B, 9B) are step-distilled for speed. Base variants preserve full training signal for customization.
</Note>

## Best Practices Summary

<AccordionGroup>
  <Accordion title="Write in Prose, Not Keywords">
    Describe scenes as flowing paragraphs. "A weathered leather journal lies open on an oak desk, morning light revealing handwritten entries in faded ink" works better than "journal, leather, oak desk, morning light, handwriting."
  </Accordion>

  <Accordion title="Lead with Your Subject">
    Put the most important element first. Word order signals priority to the model.
  </Accordion>

  <Accordion title="Describe Light Explicitly">
    Specify light source, quality, direction, and how it interacts with surfaces. Lighting descriptions have the highest impact on output quality.
  </Accordion>

  <Accordion title="Use Sensory Details">
    Include textures, reflections, and atmospheric elements. "Flaky croissant layers catching soft diffused light" is more evocative than "croissant on table."
  </Accordion>

  <Accordion title="Add Style/Mood Tags (Optional)">
    End prompts with explicit style or mood annotations when you want consistent aesthetic results across multiple generations.
  </Accordion>

  <Accordion title="Simplify Multi-Reference Prompts">
    When using reference images, describe relationships and context—let the images provide visual details.
  </Accordion>

  <Accordion title="Be Specific with Transformations">
    For i2i editing, clearly state what should change and the target result. Avoid vague instructions.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="Try [klein] via API" icon="rocket" href="/flux_2/flux2_text_to_image">
    Sub-second generation from \$0.014/image. No GPU required—start generating in minutes.
  </Card>

  <Card title="Download Weights" icon="download" href="https://huggingface.co/black-forest-labs">
    Run locally with open weights. 4B (Apache 2.0) or 9B (FLUX Non-Commercial).
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.bfl.ml/llms.txt