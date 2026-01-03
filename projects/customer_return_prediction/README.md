# Customer Return Prediction from Marketing Campaigns

Predicting customer repeat purchases within 90 days after marketing message interaction using XGBoost classification.

## Business Problem

An apparel e-commerce company wants to identify customers most likely to make repeat purchases after receiving marketing communications. This enables:
- **Targeted campaigns** - Focus resources on high-potential customers
- **Channel optimization** - Allocate budget between email and push notifications
- **Retention strategies** - Proactive engagement with at-risk customers

## Results

| Metric | Value |
|--------|-------|
| ROC AUC (CV) | 0.9457 |
| ROC AUC (Test) | 0.9496 |
| Best Model | XGBoost |

### Key Findings

1. **Push notifications outperform email** - 4.2% vs 3.6% conversion rate
2. **Returning customers buy cheaper** - Lower average order value correlates with repeat purchases
3. **Category diversity matters** - More categories purchased = higher return probability
4. **Response speed predicts returns** - Faster reactions to messages indicate loyal customers

## Data

- **Messages**: 12.7M marketing interactions (email, push notifications)
- **Purchases**: 202K transactions with product categories
- **Target**: Binary label for 90-day return (49K customers)

## Features Engineered

| Feature | Description | Correlation |
|---------|-------------|-------------|
| `last_purchase_gap` | Days since last purchase | -0.15 |
| `total_spent` | Cumulative spending | +0.19 |
| `n_categories` | Unique categories purchased | +0.20 |
| `click_rate` | Clicks / messages received | +0.12 |
| `reaction_delay` | Hours from message to purchase | -0.16 |

## Methods

- **Preprocessing**: Date parsing, duplicate removal, category list parsing
- **EDA**: Distribution analysis, temporal patterns, customer segmentation
- **Models tested**: Logistic Regression, Random Forest, XGBoost, LightGBM
- **Hyperparameter tuning**: RandomizedSearchCV with 5-fold CV
- **Interpretability**: SHAP analysis for feature importance

## Project Structure

```
customer_return_prediction/
├── customer_return_prediction.ipynb  # Main analysis notebook
├── README.md
├── requirements.txt
└── reports/
    └── business_report.md
```

## Technologies

- Python 3.10+
- pandas, numpy
- scikit-learn
- XGBoost, LightGBM
- SHAP
- matplotlib, seaborn
