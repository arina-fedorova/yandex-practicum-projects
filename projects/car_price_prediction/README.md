# Car Price Prediction (Regression, Gradient Boosting)

> Building a real-time pricing engine for a used car marketplace.

## Quick Results

| Metric | Value | Context |
|--------|-------|---------|
| **Test RMSE** | 1,820€ | 61% better than baseline |
| **Training Time** | 4 sec | Enables hourly retraining |
| **Prediction Latency** | 0.01 ms | Real-time capable |

## Problem Statement

A used car marketplace needs to instantly estimate vehicle prices for customers. The model must balance three priorities:
1. **Prediction quality** — accurate estimates build trust
2. **Prediction speed** — users expect instant results
3. **Training speed** — market prices shift, model needs frequent updates

## Solution

Compared three approaches on 239K German car listings:

| Model | RMSE (€) | Train Time | Prediction |
|-------|----------|------------|------------|
| **LightGBM** | **1,840** | **4 sec** | 0.6 sec |
| CatBoost | 1,802 | 115 sec | 0.4 sec |
| Linear Regression | 2,772 | 10 sec | 0.3 sec |

**Winner: LightGBM** — nearly matches CatBoost accuracy but trains 30x faster.

## Key Findings

- **Age is king**: Registration year has 0.59 correlation with price
- **Power matters**: Engine HP shows 0.37 correlation with price
- **Mileage less important**: Only -0.16 correlation (surprising!)
- **Automatic premium**: Cars with automatic transmission command higher prices

## Tech Stack

`Python` `Pandas` `Scikit-learn` `LightGBM` `CatBoost` `Matplotlib` `Seaborn`

## Project Structure

```
car_price_prediction/
├── README.md
├── requirements.txt
├── Car_Price_Prediction.ipynb
└── reports/
    ├── business_report.md
    └── images/
        ├── price_distribution.png
        ├── price_factors.png
        ├── correlation_matrix.png
        └── model_comparison.png
```

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
