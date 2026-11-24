---
layout: default
title: Autonomous Research Paper Reading Playbook
---

# Research Paper Reading Playbook & Master AI Knowledge Graph

> An autonomous, multi-agent research exploration system that transforms dense academic papers into **interconnected Obsidian wiki vaults**, **NotebookLM-style two-host audio overviews**, **explainer video storyboards**, **technical reports**, and an **interactive Socratic AI tutor**.

---

## Quick Navigation

- 🗺️ **[Master Top-Level Explainer](MASTER_EXPLAINER.md)**: The unifying architectural synthesis linking all 17 foundation and award-winning papers along 6 intellectual lineages.
- 🏛️ **[Master Obsidian Knowledge Graph](vaults/00_master_vault/00%20Master%20Index.md)**: The overarching Map of Content (MOC) interconnecting all individual paper vaults.
- 📚 **[The 17 Foundation & Award-Winning Papers](papers/README.md)**: Curated deconstructions of Transformers, ResNet, BERT, GPT-3, Diffusion, ViT, LoRA, FlashAttention, and NeurIPS/CVPR Best Paper winners.
- 🚀 **[Getting Started Guide](GETTING_STARTED.md)**: Step-by-step setup, configuration, CLI usage, and Obsidian vault walkthrough.
- 🤖 **[Multi-Agent Architecture (agents.md)](agents.md)**: Comprehensive specification of the 6 specialized agent skills and coordination protocols.

---

## The Master Catalog: 17 Seminal & Best Paper Award Winners

| # | Paper Title | Venue & Award | Core Breakthrough | Vault & Study Assets |
| :--- | :--- | :--- | :--- | :--- |
| **00** | [VP ≠ VNP over Every Field](papers/00_vp_vs_vnp_valiant.md) | **Valiant Complexity Challenge** | Separates VP and VNP over every field via tensor price metric dichotomy. | [Vault](vaults/00_vp_vs_vnp_valiant-vault/00%20Index.md) &bull; [Report](outputs/00_vp_vs_vnp_valiant/EXPLAINER_REPORT.md) |
| **01** | [Attention Is All You Need](papers/01_attention_is_all_you_need.md) | NeurIPS 2017 Landmark | Dispensed with recurrence/convolutions; introduced Multi-Head Self-Attention. | [Vault](vaults/01_attention_is_all_you_need-vault/00%20Index.md) &bull; [Report](outputs/01_attention_is_all_you_need/EXPLAINER_REPORT.md) |
| **02** | [Deep Residual Learning (ResNet)](papers/02_deep_residual_learning_resnet.md) | **CVPR 2016 Best Paper** | Identity skip connections ($y = \mathcal{F}(x) + x$), overcoming vanishing gradients. | [Vault](vaults/02_deep_residual_learning_resnet-vault/00%20Index.md) &bull; [Report](outputs/02_deep_residual_learning_resnet/EXPLAINER_REPORT.md) |
| **03** | [BERT: Bidirectional Transformers](papers/03_bert_bidirectional_transformers.md) | **NAACL 2019 Best Paper** | Masked Language Modeling (MLM) and deep bidirectional pre-training for NLU transfer. | [Vault](vaults/03_bert_bidirectional_transformers-vault/00%20Index.md) &bull; [Report](outputs/03_bert_bidirectional_transformers/EXPLAINER_REPORT.md) |
| **04** | [GPT-3: Few-Shot Learners](papers/04_gpt3_language_models_few_shot.md) | **NeurIPS 2020 Outstanding** | Scaled to 175B parameters; unlocked in-context zero- and few-shot learning. | [Vault](vaults/04_gpt3_language_models_few_shot-vault/00%20Index.md) &bull; [Report](outputs/04_gpt3_language_models_few_shot/EXPLAINER_REPORT.md) |
| **05** | [DDPM: Diffusion Models](papers/05_ddpm_diffusion_models.md) | NeurIPS 2020 Landmark | Formulated tractable score-matching diffusion, powering modern visual generative AI. | [Vault](vaults/05_ddpm_diffusion_models-vault/00%20Index.md) &bull; [Report](outputs/05_ddpm_diffusion_models/EXPLAINER_REPORT.md) |
| **06** | [Vision Transformer (ViT)](papers/06_vision_transformer_vit.md) | ICLR 2021 Landmark | Pure Transformer encoders applied to image patch tokens, replacing CNN inductive biases. | [Vault](vaults/06_vision_transformer_vit-vault/00%20Index.md) &bull; [Report](outputs/06_vision_transformer_vit/EXPLAINER_REPORT.md) |
| **07** | [InstructGPT: RLHF Alignment](papers/07_instructgpt_rlhf.md) | NeurIPS 2022 Landmark | SFT + Reward Model + PPO alignment loop; resolved alignment tax, creating basis of ChatGPT. | [Vault](vaults/07_instructgpt_rlhf-vault/00%20Index.md) &bull; [Report](outputs/07_instructgpt_rlhf/EXPLAINER_REPORT.md) |
| **08** | [LoRA: Low-Rank Adaptation](papers/08_lora_low_rank_adaptation.md) | ICLR 2022 Landmark | Decomposed weight updates as low-rank $BA$ ($r \ll d$); slashed VRAM by 3x with zero added latency. | [Vault](vaults/08_lora_low_rank_adaptation-vault/00%20Index.md) &bull; [Report](outputs/08_lora_low_rank_adaptation/EXPLAINER_REPORT.md) |
| **09** | [Scaling Laws for Neural LMs](papers/09_scaling_laws_neural_language_models.md) | arXiv 2020 Landmark | Discovered empirical power laws governing compute budget ($C$), data ($D$), and parameters ($N$). | [Vault](vaults/09_scaling_laws_neural_language_models-vault/00%20Index.md) &bull; [Report](outputs/09_scaling_laws_neural_language_models/EXPLAINER_REPORT.md) |
| **10** | [FlashAttention: IO-Aware Attention](papers/10_flashattention_io_aware.md) | NeurIPS 2022 Landmark | GPU SRAM tiling and online softmax; 2–4x speedup eliminating HBM memory bottleneck. | [Vault](vaults/10_flashattention_io_aware-vault/00%20Index.md) &bull; [Report](outputs/10_flashattention_io_aware/EXPLAINER_REPORT.md) |
| **11** | [Neural Ordinary Differential Equations](papers/11_neural_odes_neurips2018_best.md) | **NeurIPS 2018 Best Paper** | Continuous-depth models via ODE solvers with $O(1)$ memory backpropagation. | [Vault](vaults/11_neural_odes_neurips2018_best-vault/00%20Index.md) &bull; [Report](outputs/11_neural_odes_neurips2018_best/EXPLAINER_REPORT.md) |
| **12** | [The Lottery Ticket Hypothesis](papers/12_lottery_ticket_iclr2019_best.md) | **ICLR 2019 Best Paper** | Dense random networks contain sparse winning tickets ($m \odot \theta_0$) trainable in isolation. | [Vault](vaults/12_lottery_ticket_iclr2019_best-vault/00%20Index.md) &bull; [Report](outputs/12_lottery_ticket_iclr2019_best/EXPLAINER_REPORT.md) |
| **13** | [DenseNet](papers/13_densenet_cvpr2017_best.md) | **CVPR 2017 Best Paper** | Connected all layers via channel-wise concatenation ($x_\ell = H([x_0, \dots, x_{\ell-1}])$), maximizing feature reuse. | [Vault](vaults/13_densenet_cvpr2017_best-vault/00%20Index.md) &bull; [Report](outputs/13_densenet_cvpr2017_best/EXPLAINER_REPORT.md) |
| **14** | [Swin Transformer](papers/14_swin_transformer_iccv2021_best.md) | **ICCV 2021 Marr Prize (Best)** | Hierarchical vision transformer with linear $O(HW)$ complexity via Shifted Windows. | [Vault](vaults/14_swin_transformer_iccv2021_best-vault/00%20Index.md) &bull; [Report](outputs/14_swin_transformer_iccv2021_best/EXPLAINER_REPORT.md) |
| **15** | [Are Emergent Abilities a Mirage?](papers/15_emergent_abilities_mirage_neurips2023_best.md) | **NeurIPS 2023 Outstanding** | Proved emergent capability jumps are mathematical mirages of non-linear metrics. | [Vault](vaults/15_emergent_abilities_mirage_neurips2023_best-vault/00%20Index.md) &bull; [Report](outputs/15_emergent_abilities_mirage_neurips2023_best/EXPLAINER_REPORT.md) |
| **16** | [Direct Preference Optimization (DPO)](papers/16_dpo_direct_preference_optimization.md) | **NeurIPS 2023 Landmark** | Exact closed-form RLHF solution; eliminated reward models and PPO loops. | [Vault](vaults/16_dpo_direct_preference_optimization-vault/00%20Index.md) &bull; [Report](outputs/16_dpo_direct_preference_optimization/EXPLAINER_REPORT.md) |

---

## Enabling GitHub Pages in Your Repository

To host this live on GitHub Pages:
1. Go to your repository settings at [https://github.com/sanchitnis/paper-reading/settings/pages](https://github.com/sanchitnis/paper-reading/settings/pages).
2. Under **Build and deployment > Source**, select **Deploy from a branch**.
3. Under **Branch**, select `main` and folder `/ (root)`.
4. Click **Save**. Your site will be published at `https://sanchitnis.github.io/paper-reading/` with all links functional!
