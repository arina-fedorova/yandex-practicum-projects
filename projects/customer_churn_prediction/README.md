# Customer Churn Prediction (Classification, Segmentation)

> Predicting customer activity decline and developing personalized retention strategies for an e-commerce platform.

## Quick Results

| Metric | Value | Baseline |
|--------|-------|----------|
| F1 Score (Test) | 0.906 | 0.475 |
| F1 Score (CV) | 0.881 | — |
| Improvement | +91% | vs DummyClassifier |
| Segments | 3 | K-Means clustering |

## Problem Statement

An online store experienced declining purchase activity among regular customers. The business needed to identify customers at risk of reducing their activity and develop targeted retention strategies before losing them.

## Solution

Built a classification model using SVC (Support Vector Classifier) that predicts customer activity decline with 90.6% F1 score. Combined with K-Means segmentation and SHAP analysis to create actionable, personalized recommendations for each customer segment.

## Key Findings

- SVC outperformed Decision Tree, KNN, and Logistic Regression
- Average session pages and marketing engagement are top predictors of churn
- Three distinct customer segments identified with different intervention needs
- 35-42% of customers in each segment show declining activity

## Tech Stack

`Python` `Pandas` `Scikit-learn` `SHAP` `Matplotlib` `Seaborn`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook customer_churn_prediction.ipynb
```

## Project Structure

```
customer_churn_prediction/
├── README.md                           # This file
├── requirements.txt                    # Project dependencies
├── customer_churn_prediction.ipynb    # Main analysis notebook
└── reports/
    └── business_report.md             # Business recommendations
```

## Methodology

### Data

| Aspect | Description |
|--------|-------------|
| Source | E-commerce customer behavior data |
| Size | 4 datasets merged into single view |
| Features | Behavioral, transactional, engagement metrics |
| Target | buying_activity (binary: normal/declining) |

### Approach

1. **Data Integration** — Merge customer, revenue, time, and profit data
2. **EDA** — Analyze distributions, correlations, activity patterns
3. **Feature Engineering** — Handle multicollinearity, encode categoricals
4. **Model Selection** — Compare KNN, Decision Tree, Logistic Regression, SVC
5. **Interpretation** — SHAP values for feature importance
6. **Segmentation** — K-Means clustering for targeted strategies

### Models Compared

| Model | F1 Score | Notes |
|-------|----------|-------|
| DummyClassifier | 0.475 | Baseline |
| SVC | 0.906 | **Best performer** |

## Customer Segments

| Segment | Size | Declining Activity | Profile |
|---------|------|-------------------|---------|
| 0 | 497 | 42% | Moderate engagement |
| 1 | 540 | 35% | High engagement |
| 2 | 547 | 40% | Mixed engagement |

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
