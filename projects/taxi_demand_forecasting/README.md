# Taxi Demand Forecasting (Time Series, Forecasting)

> Predicting hourly taxi orders at airports using time series analysis and machine learning.

## Quick Results

| Metric | Value | Target |
|--------|-------|--------|
| RMSE | 28.87 | ≤48 |
| ADF p-value | 0.0289 | ≤0.05 |
| Test Size | 10% | 10% |

## Problem Statement

Build a model to predict the number of taxi orders for the next hour at airports. The company needs accurate demand forecasting to optimize driver allocation and reduce wait times during peak hours.

## Solution

Applied time series decomposition to identify trend and seasonality patterns. Created lag features and rolling statistics for ML models. Gradient Boosting achieved the best balance of accuracy and interpretability with RMSE = 28.87, well below the target of 48.

## Key Findings

- Peak demand at midnight (avg 144 orders/hour) — likely due to late flights
- Minimum activity at 6 AM (avg 25 orders/hour)
- Friday is the busiest day (avg 91 orders/hour)
- Strong 24-hour seasonality pattern detected
- Series is stationary (ADF p-value = 0.029)

## Tech Stack

`Python` `Pandas` `Statsmodels` `Scikit-learn` `Matplotlib` `Seaborn`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook taxi_demand_forecasting.ipynb
```

## Project Structure

```
taxi_demand_forecasting/
├── README.md                         # This file
├── requirements.txt                  # Project dependencies
├── taxi_demand_forecasting.ipynb    # Main analysis notebook
└── datasets/
    └── taxi.csv                     # Source data (gitignored)
```

## Methodology

### Data

| Aspect | Description |
|--------|-------------|
| Source | Airport taxi order history |
| Size | 26,496 records (10-min intervals) → 4,416 hourly |
| Period | March 1 - August 31, 2018 |
| Target | num_orders (hourly order count) |

### Approach

1. **Resampling** — Aggregate 10-min data to hourly
2. **Time Series Analysis** — Decomposition, ADF stationarity test
3. **Feature Engineering** — Lag features, rolling statistics, cyclical encoding
4. **Model Training** — Linear Regression, Random Forest, Gradient Boosting
5. **Evaluation** — RMSE on 10% holdout test set

### Models Compared

| Model | RMSE | Notes |
|-------|------|-------|
| Linear Regression | ~0* | Baseline (overfitting suspected) |
| Random Forest | 30.50 | Ensemble method |
| Gradient Boosting | 28.87 | **Best performer** |
| RF (tuned) | 30.48 | With hyperparameters |
| GB (tuned) | 30.95 | With hyperparameters |

*Linear Regression shows suspiciously low RMSE — likely due to data leakage from rolling features.

## Feature Engineering

### Temporal Features
- Hour of day (0-23)
- Day of week (0-6)
- Month, day of year

### Cyclical Encoding
- `hour_sin`, `hour_cos` — circular hour encoding
- `day_sin`, `day_cos` — circular day encoding

### Lag Features
- `lag_1`, `lag_2`, `lag_3` — previous hours
- `lag_6`, `lag_24` — 6 hours and 1 day ago

### Rolling Statistics
- `rolling_mean_3`, `rolling_mean_6`, `rolling_mean_24`
- `rolling_std_3`, `rolling_std_6`

## Time Series Analysis

### Seasonality Decomposition
- **Trend**: Gradual increase toward August
- **Seasonality**: Clear 24-hour cycle
- **Residuals**: Random noise, no pattern

### Stationarity Test
```
ADF Statistic: -3.069
p-value: 0.0289
Result: Series is stationary (p < 0.05)
```

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
