---
name: gemini-notebook-media
description: Leverages Gemini APIs and NotebookLM workflows to generate audio overview scripts, video storyboards, slide presentations, and multimedia study assets.
---

# Gemini Notebook & Media Skill

## Overview
Generates engaging multimodal learning artifacts modeled after Google NotebookLM and Gemini Audio/Video workflows:
1. **Two-Host Deep-Dive Audio Script** ("NotebookLM Audio Overview" style podcast discussion).
2. **Synchronized Video Storyboard & Presentation Slides** (SVG / HTML5 / Markdown reveal presentation).
3. **Automated Narration & Video Rendering Pipeline** (combining speech synthesis with visual slides into an MP4/WebM video).
4. **NotebookLM Study Guide Package** (Briefing doc, FAQ, timeline, study guide, and interactive quiz).

## 1. Two-Host Podcast Script Generator
Generates a dynamic, conversational script between two AI hosts:
- **Alex (The Analytical Skeptic / Technical Host)**: Probes mathematical rigor, checks assumptions, relates concepts to systems and engineering reality.
- **Jordan (The Intuitive Synthesizer / Conceptual Host)**: Brings high-level clarity, vivid metaphors, historical context, and "aha!" moments.
- **Tone**: Professional yet approachable, energetic, intellectual curiosity, zero condescension.

### Audio Script Template
```markdown
# Audio Overview: [Paper Title]
*Hosts: Alex & Jordan*
*Estimated runtime: 8-12 minutes*

**Alex:** "Welcome back. Today we are digging into a paper that has been sending shockwaves through the community..."
**Jordan:** "Yeah, and if the claims hold up, it settles a question that's been standing for nearly half a century. We're talking about..."
...
```

## 2. Explainer Video Storyboard & Slide Generator
Creates visual presentation slides optimized for video explainer rendering:
- Slide 1: Title, Authors, Status, and Big Question.
- Slide 2: The Core Problem & Historical Obstacle.
- Slide 3: The Breakthrough Insight / Bifurcation.
- Slide 4: Architectural Blueprint / Proof Topology (Mermaid/SVG).
- Slide 5: Deep Dive: Branch 1 / Core Mechanism.
- Slide 6: Deep Dive: Branch 2 / Complexity Analysis.
- Slide 7: Critical Nuances & What It Does NOT Claim.
- Slide 8: Real-World Implications & Takeaways for Engineers.

## 3. Video Rendering Engine
Outputs an interactive HTML5 presentation bundle (`slides.html`) and an automated video build script (`render_video.py`) that uses `matplotlib`, `PIL`, and Gemini audio/TTS outputs to produce an MP4 video or interactive web explainer.
