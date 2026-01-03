# Multimodal Image-Text Matching

Predicting the probability that an image matches a given text description using ResNet50 and BERT embeddings.

## Quick Results

| Metric | Value |
|--------|-------|
| Best Model | XGBoost |
| Test MAE | 0.18 |
| Test R² | 0.24 |
| Training Pairs | 4,161 |
| Image Features | 300-dim (ResNet50 + PCA) |
| Text Features | 100-dim (BERT + PCA) |

## Problem Statement

Build a multimodal model to predict image-text correspondence probability:
1. Given an image and text description
2. Predict probability (0-1) that they match
3. Handle legal restrictions on child content
4. Enable image search by text query

### Business Context

A search service needs to match images with text queries while complying with child protection laws. The model should:
- Predict match probability for any image-text pair
- Filter content containing children
- Support real-time image search

## Solution

### Data Pipeline
1. **Expert Annotations** — 3 specialists rated each image-text pair (1-4 scale)
2. **Crowdsourcing** — Workers voted on match/no-match
3. **Target Variable** — Weighted combination (60% expert + 40% crowd)

### Feature Engineering
- **Images**: ResNet50 pretrained on ImageNet → 2048-dim → PCA to 300-dim
- **Text**: BERT (bert-base-uncased) → 768-dim → PCA to 100-dim
- **Combined**: 400-dimensional feature vectors

### Model Training
- **Split**: GroupShuffleSplit by image (80/20) to prevent data leakage
- **Scaling**: StandardScaler fitted only on training data
- **Models**: Ridge, Random Forest, XGBoost, MLP

## Key Findings

1. **Child Content**: 28.5% of data filtered per legal requirements
2. **Expert Agreement**: All 3 experts tended toward low scores (avg 1.44-1.88)
3. **XGBoost Best**: Outperformed other models on combined features
4. **BERT Superior**: 87.75% explained variance vs 54.10% for TF-IDF

## Project Structure

```
multimodal_image_text_matching/
├── machine-vision.ipynb    # Main analysis
├── README.md
├── requirements.txt
└── reports/
    └── business_report.md
```

## Tech Stack

- **Python 3.8+**
- **TensorFlow/Keras** — ResNet50 feature extraction
- **Transformers** — BERT embeddings
- **scikit-learn** — ML models, PCA, scaling
- **XGBoost** — Gradient boosting
- **pandas, numpy** — Data manipulation
- **matplotlib, seaborn** — Visualization

## Usage

```python
# Search for image by text query
results = search_image_by_text("a cat sitting on a couch")
# Returns: [("image_001.jpg", 0.85), ("image_042.jpg", 0.72), ...]
```

## Legal Compliance

The model filters content with child-related keywords:
- child, children, kid, baby, toddler
- boy, girl, teen, school, playground

When detected, returns:
> "This image is unavailable in your country in compliance with local laws"

## Author

**Arina Fedorova** — [GitHub](https://github.com/ArinaKorshunova)
