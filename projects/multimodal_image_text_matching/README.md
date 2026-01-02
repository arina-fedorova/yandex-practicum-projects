# Multimodal Image-Text Matching (Computer Vision, BERT, Ensemble)

> Combining visual and textual features using ResNet50 and BERT for age prediction.

## Quick Results

| Metric | Value | Target |
|--------|-------|--------|
| MAE (Ensemble) | 5.4 | ≤6.0 |
| Best Model | XGBoost | - |
| Dataset Size | 7,591 images | - |

## Problem Statement

Build a multimodal model that predicts age categories using both image and text features. The challenge involves processing images through computer vision models and text through NLP models, then combining these modalities effectively.

## Solution

Combined visual features from ResNet50 with textual embeddings from BERT to create a unified feature representation. Applied PCA for dimensionality reduction and trained ensemble models (XGBoost, RandomForest, MLP, Ridge) to achieve robust predictions.

## Key Findings

- ResNet50 features capture visual patterns effectively (2048 dimensions)
- BERT embeddings provide complementary textual information (768 dimensions)
- XGBoost performs best with combined modalities
- Ensemble approach improves robustness across different data types

## Tech Stack

`Python` `PyTorch` `Transformers (BERT)` `ResNet50` `XGBoost` `Scikit-learn` `NumPy` `Pandas`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook machine_vision_final.ipynb
```

## Project Structure

```
multimodal_image_text_matching/
├── README.md                     # This file
├── requirements.txt              # Project dependencies
├── machine_vision_final.ipynb    # Main analysis notebook
├── machine-vision.ipynb          # Alternative notebook version
└── *.pkl                         # Trained model artifacts (gitignored)
```

## Methodology

### Data

| Aspect | Description |
|--------|-------------|
| Source | Image-text pairs dataset |
| Size | 7,591 records |
| Modalities | Images (visual) + Descriptions (text) |
| Target | Age category prediction |

### Approach

1. **Image Feature Extraction** — ResNet50 pretrained on ImageNet
2. **Text Vectorization** — BERT transformer model (bert-base-uncased)
3. **Dimensionality Reduction** — PCA for feature compression
4. **Model Training** — Ensemble of XGBoost, RandomForest, MLP, Ridge
5. **Evaluation** — MAE for regression, cross-validation

### Models Compared

| Model | MAE | Notes |
|-------|-----|-------|
| Ridge | 6.2 | Simple baseline |
| RandomForest | 5.8 | Tree-based ensemble |
| XGBoost | 5.4 | Gradient boosting |
| MLP | 5.6 | Neural network |

## Feature Engineering

### Visual Features
- **ResNet50** — 2048-dimensional feature vectors
- **PCA Reduction** — Compressed to 256 components

### Text Features
- **BERT Embeddings** — 768-dimensional vectors
- **SVD Reduction** — Compressed to 64 components

### Combined Features
- Concatenated visual + text vectors
- Standard scaling applied

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
