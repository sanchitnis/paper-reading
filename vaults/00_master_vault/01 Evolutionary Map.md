---
tags: [master-vault, evolutionary-map, lineage]
---
# The Evolutionary Map of Modern AI

```mermaid
flowchart TD
    ResNet["ResNet (CVPR'16 Best)<br/>y = F(x) + x"] --> DenseNet["DenseNet (CVPR'17 Best)<br/>Concatenation"]
    ResNet --> NeuralODE["Neural ODEs (NeurIPS'18 Best)<br/>Continuous Depth"]
    ResNet --> Trans["Transformer (NeurIPS'17)<br/>Self-Attention"]
    
    Trans --> BERT["BERT (NAACL'19 Best)<br/>Bidirectional MLM"]
    Trans --> GPT3["GPT-3 (NeurIPS'20)<br/>Few-Shot Emergence"]
    Trans --> ScalingLaws["Scaling Laws (2020)<br/>Power-Law Scaling"]
    
    Trans --> ViT["ViT (ICLR'21)<br/>Patches as Tokens"]
    ViT --> Swin["Swin (ICCV'21 Best)<br/>Shifted Windows"]
    
    Trans --> FlashAttn["FlashAttention (NeurIPS'22)<br/>IO-Aware SRAM Tiling"]
    
    Lottery["Lottery Ticket (ICLR'19 Best)<br/>Sparse Subnetworks"] --> LoRA["LoRA (ICLR'22)<br/>Low-Rank Updates"]
    GPT3 --> LoRA
    
    GPT3 --> InstructGPT["InstructGPT (NeurIPS'22)<br/>RLHF (PPO)"]
    InstructGPT --> DPO["DPO (NeurIPS'23)<br/>Closed-Form Preference"]
    GPT3 --> Mirage["Emergent Mirage (NeurIPS'23 Best)<br/>Metric Geometry"]
    
    NeuralODE -.-> DDPM["DDPM (NeurIPS'20)<br/>Generative Diffusion"]
```

## How the Pieces Fit Together
1. **Residual Connections** enabled deep Transformers to train stably.
2. **Self-Attention** replaced recurrent bottlenecks with $O(1)$ path lengths.
3. **Scaling Laws** gave confidence to train 175B+ parameter models like GPT-3.
4. **ViT and Swin** generalized the Transformer from 1D text to 2D dense vision.
5. **FlashAttention and LoRA** made training and serving long-context models computationally practical.
6. **InstructGPT and DPO** transformed raw autocomplete models into aligned, instruction-following AI assistants.
