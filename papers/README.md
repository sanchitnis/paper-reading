# The 10 Seminal Modern Machine Learning Papers

This directory contains curated, structured deconstructions of the **10 most influential foundation papers** in modern machine learning. Each paper has been processed through the **Paper Reading Playbook**, producing:
- In-depth architectural and mathematical breakdown.
- Dedicated 15-note modular **Obsidian Vault** (`vaults/<paper_id>-vault/`).
- **NotebookLM-Style Audio Podcast Script** (`outputs/<paper_id>/AUDIO_OVERVIEW_SCRIPT.md`).
- **Interactive Presentation Deck** (`outputs/<paper_id>/slides.html`).
- **Rendered Storyboard Frames** (`outputs/<paper_id>/video_frames/`).
- **Technical Explainer Report** (`outputs/<paper_id>/EXPLAINER_REPORT.md`).

---

## The Master Catalog

| # | Paper Title & Focus | Venue & Year | Core Innovation | Study Artifacts |
| :--- | :--- | :--- | :--- | :--- |
| **01** | [Attention Is All You Need](01_attention_is_all_you_need.md) | NeurIPS 2017 | Dispensed with recurrence and convolutions; introduced pure Multi-Head Self-Attention. | [Vault](file:///d:/sanjay/paper-reading/vaults/01_attention_is_all_you_need-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/01_attention_is_all_you_need/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/01_attention_is_all_you_need/AUDIO_OVERVIEW_SCRIPT.md) |
| **02** | [Deep Residual Learning (ResNet)](02_deep_residual_learning_resnet.md) | CVPR 2016 | Solved degradation and vanishing gradients using skip/identity connections ($y = \mathcal{F}(x) + x$). | [Vault](file:///d:/sanjay/paper-reading/vaults/02_deep_residual_learning_resnet-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/02_deep_residual_learning_resnet/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/02_deep_residual_learning_resnet/AUDIO_OVERVIEW_SCRIPT.md) |
| **03** | [BERT: Bidirectional Transformers](03_bert_bidirectional_transformers.md) | NAACL 2019 | Masked Language Modeling (MLM) and deep bidirectional pre-training for NLU transfer. | [Vault](file:///d:/sanjay/paper-reading/vaults/03_bert_bidirectional_transformers-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/03_bert_bidirectional_transformers/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/03_bert_bidirectional_transformers/AUDIO_OVERVIEW_SCRIPT.md) |
| **04** | [GPT-3: Language Models are Few-Shot Learners](04_gpt3_language_models_few_shot.md) | NeurIPS 2020 | Scaled autoregressive models to 175B parameters; unlocked zero- and few-shot in-context learning. | [Vault](file:///d:/sanjay/paper-reading/vaults/04_gpt3_language_models_few_shot-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/04_gpt3_language_models_few_shot/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/04_gpt3_language_models_few_shot/AUDIO_OVERVIEW_SCRIPT.md) |
| **05** | [DDPM: Diffusion Probabilistic Models](05_ddpm_diffusion_models.md) | NeurIPS 2020 | Formulated tractable variational diffusion with score matching, powering modern generative visual AI. | [Vault](file:///d:/sanjay/paper-reading/vaults/05_ddpm_diffusion_models-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/05_ddpm_diffusion_models/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/05_ddpm_diffusion_models/AUDIO_OVERVIEW_SCRIPT.md) |
| **06** | [Vision Transformer (ViT)](06_vision_transformer_vit.md) | ICLR 2021 | Applied pure Transformer encoders to linear projections of image patches, beating SOTA CNNs. | [Vault](file:///d:/sanjay/paper-reading/vaults/06_vision_transformer_vit-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/06_vision_transformer_vit/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/06_vision_transformer_vit/AUDIO_OVERVIEW_SCRIPT.md) |
| **07** | [InstructGPT: RLHF Alignment](07_instructgpt_rlhf.md) | NeurIPS 2022 | SFT + Reward Model + PPO alignment loop, solving alignment tax and creating foundation for ChatGPT. | [Vault](file:///d:/sanjay/paper-reading/vaults/07_instructgpt_rlhf-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/07_instructgpt_rlhf/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/07_instructgpt_rlhf/AUDIO_OVERVIEW_SCRIPT.md) |
| **08** | [LoRA: Low-Rank Adaptation](08_lora_low_rank_adaptation.md) | ICLR 2022 | Decomposed weight updates into low-rank matrices $BA$ ($r \ll d$); slashed VRAM with zero latency penalty. | [Vault](file:///d:/sanjay/paper-reading/vaults/08_lora_low_rank_adaptation-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/08_lora_low_rank_adaptation/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/08_lora_low_rank_adaptation/AUDIO_OVERVIEW_SCRIPT.md) |
| **09** | [Scaling Laws for Neural Language Models](09_scaling_laws_neural_language_models.md) | arXiv 2020 | Discovered empirical power-law relationships between loss and compute, data, and parameters. | [Vault](file:///d:/sanjay/paper-reading/vaults/09_scaling_laws_neural_language_models-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/09_scaling_laws_neural_language_models/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/09_scaling_laws_neural_language_models/AUDIO_OVERVIEW_SCRIPT.md) |
| **10** | [FlashAttention: IO-Aware Attention](10_flashattention_io_aware.md) | NeurIPS 2022 | Leveraged GPU SRAM tiling and online softmax to avoid HBM memory traffic; 2-4x speedup. | [Vault](file:///d:/sanjay/paper-reading/vaults/10_flashattention_io_aware-vault/00%20Index.md) &bull; [Report](file:///d:/sanjay/paper-reading/outputs/10_flashattention_io_aware/EXPLAINER_REPORT.md) &bull; [Audio](file:///d:/sanjay/paper-reading/outputs/10_flashattention_io_aware/AUDIO_OVERVIEW_SCRIPT.md) |

---

## Machine-Readable Index
A structured JSON representation of this catalog is available at [`papers/catalog.json`](file:///d:/sanjay/paper-reading/papers/catalog.json).

## Exploring Interactively
To launch the Socratic AI Chatbot tutor on any of these papers:
```bash
python -m src.cli chat "papers/01_attention_is_all_you_need.md"
python -m src.cli chat "papers/10_flashattention_io_aware.md"
```
