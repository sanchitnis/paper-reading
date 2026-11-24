---
tags: [master-vault, moc, ai-architecture, overview]
aliases: [Master AI Knowledge Graph, Master Index]
---
# Master AI & ML Research Knowledge Graph

> Welcome to the Master Knowledge Graph of modern machine learning. This vault connects the landmark architectural foundations and top-venue award-winning papers into an interconnected semantic web.

## The Evolutionary Map
- [[01 Evolutionary Map]]: The 6 historical lineages connecting ResNet to modern Transformers, Diffusion, and Alignment.
- [[02 Taxonomy and Comparison Matrix]]: Comparative metrics on inductive bias, computational complexity, memory footprints, and optimization paradigms.
- [[03 How to Add Future Papers]]: The automated pipeline for ingesting, analyzing, and slotting any future research paper into this graph.

---

## The Paper Network (16 Foundations & Award Winners)

### 1. Architectures, Residuals & Continuous Depth
- [[../02_deep_residual_learning_resnet-vault/00 Index|ResNet]] *(CVPR 2016 Best Paper)* — Identity skip connections $y = \mathcal{F}(x) + x$
- [[../13_densenet_cvpr2017_best-vault/00 Index|DenseNet]] *(CVPR 2017 Best Paper)* — Feature map concatenation $x_\ell = H([x_0, \dots, x_{\ell-1}])$
- [[../11_neural_odes_neurips2018_best-vault/00 Index|Neural ODEs]] *(NeurIPS 2018 Best Paper)* — Continuous-depth states via ODE solvers with $O(1)$ memory

### 2. Attention & Pre-training Foundations
- [[../01_attention_is_all_you_need-vault/00 Index|Attention Is All You Need (Transformer)]] — Multi-head self-attention with $O(1)$ path length
- [[../03_bert_bidirectional_transformers-vault/00 Index|BERT]] *(NAACL 2019 Best Paper)* — Bidirectional masked language modeling (MLM)

### 3. Scaling Laws & In-Context Learning
- [[../09_scaling_laws_neural_language_models-vault/00 Index|Scaling Laws for Neural LMs]] — Empirical power-law frontiers $L(C) = (C_c/C)^{\alpha_C}$
- [[../04_gpt3_language_models_few_shot-vault/00 Index|GPT-3 (175B)]] *(NeurIPS 2020 Outstanding Paper)* — Emergence of in-context few-shot learning
- [[../15_emergent_abilities_mirage_neurips2023_best-vault/00 Index|Are Emergent Abilities a Mirage?]] *(NeurIPS 2023 Outstanding Paper)* — Non-linear metric artifacts vs smooth capabilities

### 4. Vision Transformers
- [[../06_vision_transformer_vit-vault/00 Index|Vision Transformer (ViT)]] — Image patches as tokens; discarding convolutional biases at scale
- [[../14_swin_transformer_iccv2021_best-vault/00 Index|Swin Transformer]] *(ICCV 2021 Marr Prize)* — Shifted window attention with linear $O(HW)$ compute

### 5. Efficiency, Sparsity & Hardware Co-Design
- [[../12_lottery_ticket_iclr2019_best-vault/00 Index|The Lottery Ticket Hypothesis]] *(ICLR 2019 Best Paper)* — Sparse winning tickets $m \odot \theta_0$
- [[../08_lora_low_rank_adaptation-vault/00 Index|LoRA]] — Low-rank adapter updates $\Delta W = BA$ ($r \ll d$)
- [[../10_flashattention_io_aware-vault/00 Index|FlashAttention]] — IO-aware on-chip SRAM tiling & online softmax

### 6. Post-Training, Alignment & Generative Models
- [[../05_ddpm_diffusion_models-vault/00 Index|DDPM]] — Variational diffusion & Langevin score matching
- [[../07_instructgpt_rlhf-vault/00 Index|InstructGPT (RLHF)]] — SFT + Reward Model + PPO alignment loop
- [[../16_dpo_direct_preference_optimization-vault/00 Index|Direct Preference Optimization (DPO)]] — Exact closed-form preference optimization

---

> [!TIP] Navigation Note
> Click any link above to jump directly into that paper's dedicated 15-note explainer vault!
