# Customer Churn Prediction

Predicting customer activity decline for an e-commerce store using machine learning and customer segmentation.

## Quick Results

| Metric | Value |
|--------|-------|
| Best Model | SVC (Support Vector Classifier) |
| F1 Score | 0.91 (weighted) |
| Baseline F1 | 0.48 |
| Improvement | **90% over baseline** |
| Customer Segments | 3 (via K-Means) |

## Problem Statement

An e-commerce store noticed declining purchase activity among regular customers. The business needed:
1. A model to predict which customers are likely to reduce activity in the next 3 months
2. Customer segmentation for targeted retention campaigns
3. Actionable insights for personalized marketing

## Solution

### Prediction Model
- Tested 4 classifiers: KNN, Decision Tree, Logistic Regression, **SVC**
- SVC achieved F1 = 0.91 on test data (90% better than random baseline)
- SHAP analysis identified top predictors:
  - Pages viewed per session
  - Time spent on site
  - Marketing communication frequency

### Customer Segmentation
- K-Means clustering identified 3 distinct segments
- Segment 0 (premium, long-term): 42% churn risk - **high priority**
- Segment 1 (standard, mid-term): 34% churn risk - medium priority
- Segment 2 (mixed, shorter-term): 39% churn risk - medium priority

## Project Structure

```
customer_churn_prediction/
├── Customer_Churn_Prediction.ipynb  # Main analysis
├── README.md
├── requirements.txt
└── reports/
    ├── business_report.md
    └── images/
        ├── marketing_by_activity.png
        ├── pages_by_activity.png
        ├── service_type_distribution.png
        ├── category_churn.png
        ├── correlation_matrix.png
        ├── shap_importance.png
        └── segment_activity.png
```

## Tech Stack

- **Python 3.8+**
- **pandas, numpy** - data manipulation
- **scikit-learn** - ML models and pipelines
- **matplotlib, seaborn** - visualization
- **SHAP** - model interpretability
- **phik** - correlation analysis

## Key Findings

1. **Engagement metrics matter most**: Pages viewed and time on site are top predictors
2. **Premium users churn more**: 50% of premium subscribers show declining activity
3. **Promotions signal risk**: Heavy promo shoppers tend to have lower loyalty
4. **Cart abandonment**: Higher in declining customers

## Business Recommendations

| Segment | Strategy |
|---------|----------|
| Premium at-risk | Loyalty programs, exclusive offers |
| Standard declining | Re-engagement email campaigns |
| Engaged stable | Maintain current approach, upsell |

## Author

**Arina Fedorova** - [GitHub](https://github.com/ArinaKorshunova)
