# Toxic Comment Detection (NLP, Classification)

> Automated moderation system for detecting toxic comments using text classification and NLP preprocessing.

## Quick Results

| Metric | Value | Target |
|--------|-------|--------|
| F1 Score | 0.778 | ≥0.75 |
| Accuracy | 95.6% | High |
| Precision | 0.81 | — |
| Recall | 0.75 | — |

## Problem Statement

An e-commerce platform allows users to edit product descriptions and comment on changes. To maintain a healthy community, the platform needs an automated tool to identify toxic comments and flag them for moderation before publication.

## Solution

Built a text classification model using TF-IDF vectorization and Logistic Regression. The pipeline includes comprehensive text preprocessing (lemmatization, cleaning, normalization) achieving F1 = 0.778, exceeding the target of 0.75.

## Key Findings

- Toxic comments represent ~10% of the dataset (class imbalance)
- Text length is not a strong predictor of toxicity
- Logistic Regression outperforms Random Forest and Naive Bayes
- Threshold optimization improves precision-recall balance

## Tech Stack

`Python` `Pandas` `Scikit-learn` `NLTK` `TF-IDF` `Matplotlib`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('wordnet'); nltk.download('stopwords')"

# Run analysis
jupyter notebook toxic_comment_detection.ipynb
```

## Project Structure

```
toxic_comment_detection/
├── README.md                          # This file
├── requirements.txt                   # Project dependencies
├── toxic_comment_detection.ipynb     # Main analysis notebook
└── reports/
    └── business_report.md            # Business recommendations
```

## Methodology

### Data

| Aspect | Description |
|--------|-------------|
| Source | User comments from e-commerce platform |
| Size | ~160,000 comments |
| Target | toxic (binary: 0=normal, 1=toxic) |
| Imbalance | ~10% toxic comments |

### Text Preprocessing

1. **Lowercasing** — Normalize case
2. **HTML Removal** — Strip markup tags
3. **Non-letter Removal** — Keep only alphabetic characters
4. **Lemmatization** — Reduce words to base form
5. **Length Filtering** — Remove very short/long texts

### Feature Engineering

- **TF-IDF Vectorization** — Convert text to numerical features
- **N-grams** — Capture word combinations
- **Vocabulary Limiting** — Focus on most informative terms

### Models Compared

| Model | F1 Score | Training Time |
|-------|----------|---------------|
| Logistic Regression | 0.778 | 39s |
| Multinomial NB | 0.738 | <1s |
| Random Forest | 0.725 | 664s |

### Threshold Optimization

Default threshold (0.5) optimized to 0.78 for better precision-recall balance on the validation set.

## Classification Report

```
              precision    recall  f1-score   support
           0      0.97      0.98      0.98     27889
           1      0.81      0.75      0.78      3164
    accuracy                          0.96     31053
```

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
