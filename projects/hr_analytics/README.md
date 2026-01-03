# HR Analytics: Employee Satisfaction and Turnover Prediction

Dual-model ML system for HR optimization: predicting employee satisfaction and turnover risk.

## Results

| Task | Model | Metric | Target | Result |
|------|-------|--------|--------|--------|
| Satisfaction Prediction | DecisionTreeRegressor | SMAPE | <15% | **13.6%** |
| Turnover Prediction | DecisionTreeClassifier | ROC-AUC | >=0.91 | **0.928** |

## Key Findings

- **Job satisfaction is the strongest turnover predictor** - employees with low predicted satisfaction have 3x higher quit rates
- **Supervisor evaluation matters most** - highest impact on satisfaction level across all features
- **Salary outliers are happier** - employees earning above 75th percentile show higher satisfaction
- **Workload balance is critical** - both overworked and underworked employees show lower satisfaction
- **Department patterns exist** - Sales and HR departments have higher turnover rates

## Business Impact

The dual-model approach enables HR to:
1. **Predict satisfaction** before issues arise (SMAPE 13.6%)
2. **Identify turnover risk** with 93% accuracy (ROC-AUC 0.928)
3. **Intervene early** based on key drivers identified via SHAP analysis

## Project Structure

```
hr_analytics/
├── hr_analytics.ipynb      # Main analysis notebook
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── reports/
    ├── business_report.md  # Business-focused summary
    └── images/             # Visualizations
```

## Methodology

1. **Data Preprocessing**: Missing value imputation, duplicate removal, typo fixes
2. **EDA**: Distribution analysis, correlation study with phik coefficient
3. **Feature Engineering**: Predicted satisfaction as input for turnover model
4. **Model Selection**: RandomizedSearchCV across multiple algorithms
5. **Interpretation**: SHAP analysis for feature importance

## Technologies

- Python 3.10+
- scikit-learn (pipelines, RandomizedSearchCV)
- SHAP (model interpretation)
- phik (correlation analysis)
- pandas, matplotlib, seaborn

## Author

Arina Fedorova
