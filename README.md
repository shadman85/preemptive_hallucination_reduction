# Preemptive Hallucination Reduction

Research code accompanying **“Visual Hallucination Reduction: An Input-Level Approach for Multimodal Language Models”** (Arif, Rabby, Papon, and Ahmed; submitted to *Multimedia Systems*, Springer — [pre-print](https://www.researchsquare.com/article/rs-7167438/v1)).

## Problem

Multimodal LLMs frequently hallucinate details that aren't present in an input image, and most mitigations require retraining or fine-tuning the model itself.

## Approach

This project explores a model-agnostic, **input-level** alternative: instead of changing the model, adapt the image before it reaches the model. The core idea is that different question types benefit from different image treatments, so the pipeline:

1. **Categorizes questions** by type (e.g. "what" / "which" / "where") to decide which preprocessing branch an image–question pair should take.
2. **Transforms the image** accordingly — Laplacian-based edge sharpening or median-filter denoising — producing a noise-reduced, edge-enhanced, or original version of the image depending on the question category.
3. Feeds the selected image variant to the downstream vision-language model, without any retraining or architecture changes.

In the paper's evaluation, this adaptive selection reduced hallucinations by **44.3%** compared to always using the original image, improving factual grounding.

## Repository structure

```
Question_categorize/
  extract_category.py   # Filters/categorizes questions by keyword patterns
preprocessing/
  preprocess.py          # Laplacian sharpening / median-blur image transforms
```

## Status

This repository holds the exploratory research scripts used to develop and validate the method described in the paper above — it is not packaged as an installable library, and file paths in the scripts reflect the original experimental setup rather than a portable configuration. It's shared for transparency and reproducibility of the reported approach rather than as production tooling.

## Citation

If you build on this work, please cite the pre-print:

> Arif, N. H., Rabby, S., Papon, M. H. H., & Ahmed, S. "Visual Hallucination Reduction: An Input-Level Approach for Multimodal Language Model." (2025).

## Contact

Shadman Rabby — [shadmanrabby.cse@gmail.com](mailto:shadmanrabby.cse@gmail.com) · [shadman85.github.io](https://shadman85.github.io/)
