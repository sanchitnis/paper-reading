---
tags: [master-vault, moc, ai-architecture, overview]
aliases: [Master AI Knowledge Graph, Master Index]
---
# Master AI & ML Research Knowledge Graph

> Welcome to the Master Knowledge Graph of modern machine learning. This vault connects the landmark architectural foundations and top-venue award-winning papers into an interconnected semantic web.

## The Evolutionary Map
- [01 Evolutionary Map](01%20Evolutionary%20Map.md): The 6 historical lineages connecting ResNet to modern Transformers, Diffusion, and Alignment.
- [02 Taxonomy and Comparison Matrix](02%20Taxonomy%20and%20Comparison%20Matrix.md): Comparative metrics on inductive bias, computational complexity, memory footprints, and optimization paradigms.
- [03 How to Add Future Papers](03%20How%20to%20Add%20Future%20Papers.md): The automated pipeline for ingesting, analyzing, and slotting any future research paper into this graph.

---

## The Paper Network (18 Foundations & Award Winners)

### 0. Theoretical Complexity & Foundational Lower Bounds
- [VP ≠ VNP over Every Field](../00_vp_vs_vnp_valiant-vault/00%20Index.md) *(Valiant 1979 Conjecture)* — Permanent vs Determinant lower bound over arbitrary fields
- [Arithmetic Circuits: A Chasm at Depth Four](../17_agrawal_vinay_chasm_depth_four-vault/00%20Index.md) *(Agrawal & Vinay 2008)* — Proves depth-4 lower bounds imply unrestricted circuit lower bounds (collapsing the VP vs VNP quest to depth 4)

### 1. Architectures, Residuals & Continuous Depth
- [ResNet](../02_deep_residual_learning_resnet-vault/00%20Index.md) *(CVPR 2016 Best Paper)* — Identity skip connections $y = \mathcal{F}(x) + x$
- [DenseNet](../13_densenet_cvpr2017_best-vault/00%20Index.md) *(CVPR 2017 Best Paper)* — Feature map concatenation $x_\ell = H([x_0, \dots, x_{\ell-1}])$
- [Neural ODEs](../11_neural_odes_neurips2018_best-vault/00%20Index.md) *(NeurIPS 2018 Best Paper)* — Continuous-depth states via ODE solvers with $O(1)$ memory

### 2. Attention & Pre-training Foundations
- [Attention Is All You Need (Transformer)](../01_attention_is_all_you_need-vault/00%20Index.md) — Multi-head self-attention with $O(1)$ path length
- [BERT](../03_bert_bidirectional_transformers-vault/00%20Index.md) *(NAACL 2019 Best Paper)* — Bidirectional masked language modeling (MLM)

### 3. Scaling Laws & In-Context Learning
- [Scaling Laws for Neural LMs](../09_scaling_laws_neural_language_models-vault/00%20Index.md) — Empirical power-law frontiers $L(C) = (C_c/C)^{\alpha_C}$
- [GPT-3 (175B)](../04_gpt3_language_models_few_shot-vault/00%20Index.md) *(NeurIPS 2020 Outstanding Paper)* — Emergence of in-context few-shot learning
- [Are Emergent Abilities a Mirage?](../15_emergent_abilities_mirage_neurips2023_best-vault/00%20Index.md) *(NeurIPS 2023 Outstanding Paper)* — Non-linear metric artifacts vs smooth capabilities

### 4. Vision Transformers
- [Vision Transformer (ViT)](../06_vision_transformer_vit-vault/00%20Index.md) — Image patches as tokens; discarding convolutional biases at scale
- [Swin Transformer](../14_swin_transformer_iccv2021_best-vault/00%20Index.md) *(ICCV 2021 Marr Prize)* — Shifted window attention with linear $O(HW)$ compute

### 5. Efficiency, Sparsity & Hardware Co-Design
- [The Lottery Ticket Hypothesis](../12_lottery_ticket_iclr2019_best-vault/00%20Index.md) *(ICLR 2019 Best Paper)* — Sparse winning tickets $m \odot \theta_0$
- [LoRA](../08_lora_low_rank_adaptation-vault/00%20Index.md) — Low-rank adapter updates $\Delta W = BA$ ($r \ll d$)
- [FlashAttention](../10_flashattention_io_aware-vault/00%20Index.md) — IO-aware on-chip SRAM tiling & online softmax

### 6. Post-Training, Alignment & Generative Models
- [DDPM](../05_ddpm_diffusion_models-vault/00%20Index.md) — Variational diffusion & Langevin score matching
- [InstructGPT (RLHF)](../07_instructgpt_rlhf-vault/00%20Index.md) — SFT + Reward Model + PPO alignment loop
- [Direct Preference Optimization (DPO)](../16_dpo_direct_preference_optimization-vault/00%20Index.md) — Exact closed-form preference optimization

---

> [!TIP] Navigation Note
> Click any link above to jump directly into that paper's dedicated 15-note explainer vault!
