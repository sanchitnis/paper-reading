# Research Paper Reading Playbook for the Autonomous Learner

> A personalized, multi-agent AI system that transforms dense academic papers into interconnected Obsidian wiki vaults, NotebookLM-style explainer podcasts, video storyboards, detailed technical reports, and an interactive Socratic AI tutor.

---

## 1. System Vision & Architecture

Reading modern research papers is challenging: notation is dense, background context is implicit, and authors condense critical derivations. For engineers and researchers bridging from applied domains to foundational theory, the cognitive hurdle can be daunting.

The **Paper Reading Playbook** solves this by coupling **Keshav's 3-Pass Methodology** with an autonomous multi-agent pipeline tailored to a **Specific Learner Profile**.

```mermaid
flowchart TD
    Paper["Research Paper<br/>(PDF / arXiv / Text / HTML)"] --> Ingest["1. Paper Ingest Agent<br/>(Extracts Sections, Math, Figures)"]
    Ingest --> Manifest[("Paper Manifest JSON")]
    
    Manifest --> MP["2. Multipass Reader Agent<br/>(Pass 1 Triage &bull; Pass 2 Grasp &bull; Pass 3 Deep Dive)"]
    Profile[("learner_profile.json<br/>(Alex Rivera)")] -.->|"Personalizes"| MP
    
    MP --> VaultGen["3. Obsidian Vault Builder"]
    MP --> MediaGen["4. Gemini Notebook Media Producer"]
    MP --> ReportGen["5. Explainer Report Synthesizer"]
    MP <--> Chatbot["6. Interactive Socratic AI Tutor<br/>(/feynman &bull; /math &bull; /drill &bull; /code)"]

    VaultGen --> Vault["Interconnected Obsidian Vault<br/>(15 Modular Linked Notes)"]
    MediaGen --> Media["NotebookLM Audio Script<br/>+ Video Storyboard & Slides"]
    ReportGen --> Report["Comprehensive Explainer Report<br/>(EXPLAINER_REPORT.md)"]
```

---

## 2. Core Methodological Pillars

### 2.1 The Multipass Reading Framework
Adapted from S. Keshav's canonical paper-reading approach and modernized for deep technical evaluation:

```mermaid
flowchart LR
    P1["Pass 1: Triage<br/>(10-15 mins)<br/>Title, Abstract, Headings, Figures<br/>5 C's Assessment"] -->|"Gate: Proceed"| P2["Pass 2: Conceptual Grasp<br/>(1-2 hours)<br/>Read Arguments, Skip Proofs<br/>Flag Bottlenecks & Glossary"]
    P2 -->|"Gate: Mastered"| P3["Pass 3: Deep Deconstruction<br/>(3-5 hours)<br/>Virtual Re-creation, Proof Audit<br/>Challenge Hidden Assumptions"]
```

- **Pass 1: Triage & Reconnaissance (10-15 minutes)**:
  - Scans title, abstract, introduction, section headings, figures, and conclusions.
  - Applies the **5 C's**: *Category, Context, Correctness, Contributions, Clarity*.
  - Determines whether to read further, file for later, or discard.
- **Pass 2: Conceptual Grasp & Structural Inspection (1-2 hours)**:
  - Reads through main arguments without getting bogged down in complex lemmas or appendices.
  - Inspects every diagram and benchmark axis.
  - Automatically flags unfamiliar terms matching the learner's `developing` knowledge list.
  - Engages the AI Chatbot tutor for Socratic clarification.
- **Pass 3: Deep Technical Deconstruction & Virtual Walk-Through (3-5 hours)**:
  - Mentally re-implements the paper from first principles.
  - Uncovers hidden assumptions, computational complexity bounds, and non-claims.
  - Reconstructs minimal toy code and verifies formal proof scripts.

---

## 3. Key Capabilities & Generated Deliverables

### 3.1 Interconnected Obsidian Knowledge Vault
Generates an Obsidian vault formatted to the gold-standard topology (as demonstrated in `vp-vnp-vault/`):
- `00 Index.md`: Map of Content (MOC), audience context, and sequential reading path.
- `01 Big picture.md`: Mermaid concept graph and 1-paragraph synthesis.
- `02 Foundations and context.md`: Historical obstacles and why prior art failed.
- `03 Core objects and definitions.md`: Formal definitions and notation tables.
- `04 What the paper claims.md`: Precise theorem statements and claimed bounds.
- `05 Proof architecture.md`: Top-down argument flowchart and bifurcation.
- `06 Primary mechanism - Branch A.md` & `07 Primary mechanism - Branch B.md`: Deep dive into proof branches.
- `08 What the result does not say.md`: Boundaries, caveats, and non-claims.
- `09 Relevance and consequences.md`: Theoretical and engineering implications.
- `10 Formalization and code verification.md`: Minimal Python simulations and proof audits.
- `11 Reception and valid comments.md`: Community scrutiny and review consensus.
- `12 How to evaluate it yourself.md`: Active-recall exercises and self-checks.
- `13 Glossary.md` & `14 References.md`: Alphabetical cross-linked definitions and bibliography.

### 3.2 Gemini Notebook & Multimedia Explainer Pipeline
- **NotebookLM-Style Audio Overview Script (`AUDIO_OVERVIEW_SCRIPT.md`)**: A two-host podcast conversation featuring **Alex** (the skeptical systems engineer) and **Jordan** (the intuitive synthesizer) breaking down the paper with wit, depth, and clarity.
- **Interactive Presentation Deck (`slides.html`)**: HTML5/SVG presentation with presenter notes, math blocks, and visual diagrams.
- **Video Storyboard Frames (`video_frames/`)**: High-resolution visual frames generated automatically for video production.

### 3.3 Publication-Grade Technical Explainer Report (`EXPLAINER_REPORT.md`)
- Executive summary with the core breakthrough distilled into 3 sentences.
- Rigorous mathematical formulations (e.g. Permanent vs Determinant complexity).
- Detailed proof architecture and bifurcation analysis.
- Critical evaluation, failure modes, and reproduction checklist.

### 3.4 Interactive Socratic & Feynman AI Tutor
- Grounded strictly in the paper manifest and generated vault.
- Supports 4 interactive modes:
  - `/feynman`: High-level systems and software architecture analogies.
  - `/math`: Step-by-step mathematical derivations and index expansions.
  - `/drill`: Active-recall questions testing comprehension of assumptions.
  - `/code`: Minimal runnable Python scripts demonstrating the concept.

---

## 4. The 10 Seminal Modern ML Papers

The repository includes curated deconstructions, manifests, and pre-generated Obsidian vaults for the 10 foundational papers of modern AI in [`papers/`](file:///d:/sanjay/paper-reading/papers/):

| # | Paper Title | Venue / Year | Core Breakthrough | Vault & Report |
| :--- | :--- | :--- | :--- | :--- |
| **01** | [Attention Is All You Need](papers/01_attention_is_all_you_need.md) | NeurIPS 2017 | Dispensed with recurrence/convolutions; introduced multi-head self-attention. | [Vault](file:///d:/sanjay/paper-reading/vaults/01_attention_is_all_you_need-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/01_attention_is_all_you_need/EXPLAINER_REPORT.md) |
| **02** | [Deep Residual Learning (ResNet)](papers/02_deep_residual_learning_resnet.md) | CVPR 2016 | Overcame vanishing gradients via identity skip connections ($y = \mathcal{F}(x) + x$). | [Vault](file:///d:/sanjay/paper-reading/vaults/02_deep_residual_learning_resnet-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/02_deep_residual_learning_resnet/EXPLAINER_REPORT.md) |
| **03** | [BERT: Bidirectional Transformers](papers/03_bert_bidirectional_transformers.md) | NAACL 2019 | Masked Language Modeling (MLM) and deep bidirectional pre-training. | [Vault](file:///d:/sanjay/paper-reading/vaults/03_bert_bidirectional_transformers-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/03_bert_bidirectional_transformers/EXPLAINER_REPORT.md) |
| **04** | [GPT-3: Language Models are Few-Shot Learners](papers/04_gpt3_language_models_few_shot.md) | NeurIPS 2020 | 175B parameter scaling; unlocked in-context zero- and few-shot learning. | [Vault](file:///d:/sanjay/paper-reading/vaults/04_gpt3_language_models_few_shot-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/04_gpt3_language_models_few_shot/EXPLAINER_REPORT.md) |
| **05** | [DDPM: Diffusion Probabilistic Models](papers/05_ddpm_diffusion_models.md) | NeurIPS 2020 | Variational diffusion with score matching, establishing modern visual generative AI. | [Vault](file:///d:/sanjay/paper-reading/vaults/05_ddpm_diffusion_models-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/05_ddpm_diffusion_models/EXPLAINER_REPORT.md) |
| **06** | [Vision Transformer (ViT)](papers/06_vision_transformer_vit.md) | ICLR 2021 | Applied pure Transformer encoders to linear projections of image patches. | [Vault](file:///d:/sanjay/paper-reading/vaults/06_vision_transformer_vit-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/06_vision_transformer_vit/EXPLAINER_REPORT.md) |
| **07** | [InstructGPT: RLHF Alignment](papers/07_instructgpt_rlhf.md) | NeurIPS 2022 | SFT + Reward Model + PPO alignment loop; direct predecessor to ChatGPT. | [Vault](file:///d:/sanjay/paper-reading/vaults/07_instructgpt_rlhf-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/07_instructgpt_rlhf/EXPLAINER_REPORT.md) |
| **08** | [LoRA: Low-Rank Adaptation](papers/08_lora_low_rank_adaptation.md) | ICLR 2022 | Decomposed weight updates into low-rank matrices $BA$; slashed VRAM by 3x. | [Vault](file:///d:/sanjay/paper-reading/vaults/08_lora_low_rank_adaptation-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/08_lora_low_rank_adaptation/EXPLAINER_REPORT.md) |
| **09** | [Scaling Laws for Neural Language Models](papers/09_scaling_laws_neural_language_models.md) | arXiv 2020 | Empirical power-law relationships governing compute ($C$), data ($D$), and parameters ($N$). | [Vault](file:///d:/sanjay/paper-reading/vaults/09_scaling_laws_neural_language_models-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/09_scaling_laws_neural_language_models/EXPLAINER_REPORT.md) |
| **10** | [FlashAttention: IO-Aware Attention](papers/10_flashattention_io_aware.md) | NeurIPS 2022 | GPU SRAM tiling and online softmax; 2-4x speedup enabling long contexts. | [Vault](file:///d:/sanjay/paper-reading/vaults/10_flashattention_io_aware-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/10_flashattention_io_aware/EXPLAINER_REPORT.md) |

Detailed catalog with mathematical summaries is available in [`papers/README.md`](file:///d:/sanjay/paper-reading/papers/README.md) and [`papers/catalog.json`](file:///d:/sanjay/paper-reading/papers/catalog.json).

---

## 5. Persona & Learner Scaffolding

The playbook is personalized via [`learner_profile.json`](file:///d:/sanjay/paper-reading/learner_profile.json):

| Dimension | Profile Configuration (Alex Rivera) |
| :--- | :--- |
| **Role** | Senior AI Systems Engineer & Applied ML Researcher |
| **Strong Areas** | Python, PyTorch, Linear Algebra, Distributed Systems, P vs NP basics |
| **Intermediate** | Information Theory, Reinforcement Learning, Probabilistic Models |
| **Developing** | Algebraic Complexity (VP vs VNP), Differential Geometry, Lean 4 |
| **Analogy Domain** | Distributed systems, caching mechanics, RPC batching, microservices |
| **Math Rule** | Step-by-step index tracking; no hand-waving |
| **Truth Marker** | Strict distinction between `*(paper)*` facts and `*(analogy)*` heuristics |

---

## 6. Agent Skills in `.agents/skills/`

The system provides 6 production-grade agent skills:
1. [`.agents/skills/paper-ingest`](file:///d:/sanjay/paper-reading/.agents/skills/paper-ingest/SKILL.md): Ingests PDF, arXiv, HTML, and text papers into structured JSON.
2. [`.agents/skills/multipass-reader`](file:///d:/sanjay/paper-reading/.agents/skills/multipass-reader/SKILL.md): Orchestrates Pass 1, Pass 2, and Pass 3 reading gates.
3. [`.agents/skills/concept-explainer`](file:///d:/sanjay/paper-reading/.agents/skills/concept-explainer/SKILL.md): AI Chatbot tutor for Socratic and Feynman dialogue.
4. [`.agents/skills/obsidian-vault-builder`](file:///d:/sanjay/paper-reading/.agents/skills/obsidian-vault-builder/SKILL.md): Generates 15-note interconnected Obsidian vaults.
5. [`.agents/skills/gemini-notebook-media`](file:///d:/sanjay/paper-reading/.agents/skills/gemini-notebook-media/SKILL.md): Produces NotebookLM podcast scripts, slides, and video assets.
6. [`.agents/skills/explainer-report-generator`](file:///d:/sanjay/paper-reading/.agents/skills/explainer-report-generator/SKILL.md): Synthesizes comprehensive technical reports.

Detailed system specifications are documented in [`agents.md`](file:///d:/sanjay/paper-reading/agents.md).

---

## 7. Quick Start

To get started right away:
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the end-to-end pipeline on any paper
python -m src.cli run-all "vp-vnp-vault/00 Index.md"

# 3. Launch the interactive AI tutor
python -m src.cli chat "vp-vnp-vault/00 Index.md"
```

For detailed instructions, see [`GETTING_STARTED.md`](file:///d:/sanjay/paper-reading/GETTING_STARTED.md).
