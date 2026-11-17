---
name: headlamp-prompt-template
description: Generate structured TikTok AI video prompts for headlamps or wearable lights using a 5-part director-level template. Use when the user asks for headlamp video scripts, AI video prompts, or localizes a lighting product for e-commerce.
---
# 头灯提示词模板 (Headlamp Prompt Template)

This skill generates highly structured, director-level AI video generation prompts for headlamps or wearable lighting products, optimized for TikTok e-commerce and AI video generators (like Jimeng/Sora). 

## When to Use
- The user asks to write an AI video script or prompt for a headlamp or similar lighting product.
- The user wants to adapt the "Headlamp" template to a new target market, scenario, or specific product variant.

## Steps
Always structure your response using these exact 5 sections:

### 01 - 参考拆解 (Reference Breakdown)
Define the global context and constraints.
- **规格 (Specs):** e.g., 15 秒，9:16，30fps，TikTok [Target Market] 电商专供。
- **全新本土化场景 (Localized Scenario):** Describe a highly specific, local work or outdoor scenario (e.g., Thailand tea picking, fishing, mining) that justifies the product.
- **核心痛点 (Core Pain Points):** List 4-5 user pain points in this scenario and how the product solves them (e.g., hands are dirty so needs motion sensor, needs wide light + spotlight).
- **设定 (Global Settings):** Pure hands-only (纯手部特写), no text/subtitles, reserve negative space (e.g., bottom right) for digital human overlay, strict motion binding.

### 02 - 产品锁定卡 (Product Lock Card)
Provide absolute visual anchors to prevent AI hallucination. Break down into:
1. **灯体基材 (Base Material):** Texture, shape, material.
2. **发光单元 (Light Units):** Exact number, arrangement, and color of lights (e.g., 3 COB strips, 1 spotlight).
3. **控制区域 (Control Area):** Button layout, icons, charging ports, sensors.
4. **头带组件 (Headband):** Material, buckles, connection points.
5. **配色锁定 (Colors):** Main body, lights, buttons, strap.
6. **功能对应外观 (Function-to-Appearance):** How features look (e.g., sensor window).
7. **构图摆放规则 (Framing Rules):** Position in frame, hands-only, no faces.
8. **禁止项 (Negative Prompts):** What the AI must NOT generate (wrong light count, wrong buttons, text, faces).

### 03 - 分镜脚本表 (Storyboard Table)
Create a **Markdown Table** outlining the narrative (usually 6 shots).
- **Columns:** 镜号 (Shot #) | 画面内容 (Visual Context) | 核心动作 (Core Action) | 本土化口播 (Localized VO - e.g., Thai/English/etc.) | 音效 (SFX)
- Progress through: Setup/Hook -> Detail display -> Sensor activation -> Wide light effect -> Mode switch -> Headband stretch.

### 04 - AI 视频提示词 (AI Video Prompts)
Write the actual prompts for the AI video generator (e.g., 即梦/Jimeng).
- **全局规则 (Global Rules):** Hands-only, negative space, no text.
- **For each Shot (1 to 6):**
  - @参考视频 (Reference video/image binding)
  - **产品外观特征 (Product Features):** Reiterate the exact visual description.
  - **物理动作 (Physical Action):** Explicit motion instructions.
  - **背景 (Background):** Scenario lighting and environment.
  - **构图与约束 (Framing):** Center-top, right-bottom blank, hands-only.
  - **负面 (Negative Prompts):** Text, subtitles, three hands, extra limbs, faces, wrong product specs.

### 05 - 一致性核验清单 (Consistency Check List)
A bulleted checklist to ensure the prompt meets all commercial needs:
- 高溢价特色场景 (Premium localized scenario).
- 功能痛点精准咬合 (Pain points matched).
- 视觉锚点无损继承 (Visual anchors locked).
- 合成通道严格预留 (Negative space for digital humans).
- 动作轨迹 100% 绑定 (Motion tracking bound).
- 负面词统一 (Negative prompts consistent).

## Gotchas
- **Crucial:** Section 03 MUST be a Markdown table.
- **Negative Space:** Always emphasize the reserved space (usually bottom right) for the localized digital human (画中画合成).
- **Hands-Only:** Strictly forbid human faces (`真人脸部`) in the video prompts to maintain the POV/hands-only style.
- Ensure the VO matches the requested target market language (e.g., Thai, English, Indonesian).