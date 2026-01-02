# Oil Well Location Selection

Choosing the most profitable oil drilling region using Bootstrap analysis and Linear Regression.

## Quick Results

| Metric | Region 0 | Region 1 | Region 2 |
|--------|----------|----------|----------|
| RMSE | 37.76 | **0.89** | 40.15 |
| Avg Reserves | 92.40 | 68.71 | **94.77** |
| Profit (B RUB) | **3.37** | 2.42 | 2.56 |
| 95% CI | [3.04, 3.74] | [2.42, 2.42] | [2.17, 2.92] |
| Loss Risk | 0% | 0% | 0% |

**Recommendation: Region 0** — Highest profit with zero risk.

## Problem Statement

An oil extraction company needs to decide where to drill new wells. Given geological data from three regions (100,000 samples each), the task is to:

1. Build a model to predict oil reserve volumes
2. Select the region with maximum profit potential
3. Assess financial risks using Bootstrap analysis

### Business Constraints

- **Budget:** 10 billion rubles for 200 wells
- **Revenue:** 450,000 rubles per thousand barrels
- **Break-even volume:** 111.11 thousand barrels per well
- **Maximum acceptable loss risk:** 2.5%

## Solution

### Model Training
- **Algorithm:** Linear Regression
- **Features:** 3 geological measurements (f0, f1, f2)
- **Target:** Oil reserve volume (thousand barrels)

### Profit Calculation
- Select 200 wells with highest predicted reserves
- Calculate actual profit using true reserve values
- Apply Bootstrap (1000 simulations) for confidence intervals

### Key Finding
Despite Region 1 having the most accurate predictions (RMSE = 0.89), **Region 0 delivers the highest profit** due to larger reserve volumes.

## Project Structure

```
oil_well_selection/
├── Oil_Well_Selection.ipynb  # Main analysis
├── README.md
├── requirements.txt
└── reports/
    ├── business_report.md
    └── images/
        ├── reserve_distribution.png
        ├── model_comparison.png
        └── bootstrap_profit.png
```

## Tech Stack

- **Python 3.8+**
- **pandas, numpy** — data manipulation
- **scikit-learn** — Linear Regression model
- **matplotlib, seaborn** — visualization

## Key Visualizations

### Reserve Distribution
![Reserve Distribution](reports/images/reserve_distribution.png)

### Model Performance
![Model Comparison](reports/images/model_comparison.png)

### Bootstrap Profit Analysis
![Bootstrap Profit](reports/images/bootstrap_profit.png)

## Author

**Arina Fedorova** — [GitHub](https://github.com/ArinaKorshunova)
