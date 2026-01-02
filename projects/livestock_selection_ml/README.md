# Livestock Selection ML (Regression + Classification)

> Dual-model system for data-driven cow selection: predicting milk yield and quality to minimize purchasing risks.

## Quick Results

| Task | Metric | Value | Target |
|------|--------|-------|--------|
| Milk Yield | R² | 0.83 | High accuracy |
| Milk Yield | RMSE | 188 kg | Low error |
| Milk Quality | Precision | 0.92 | Minimize false positives |
| Selection | Cows Selected | Based on both criteria | ≥6000 kg + tasty |

## Problem Statement

A dairy farm needs to make objective purchasing decisions when selecting new cows. The farmer wants to minimize risk by predicting both the quantity (annual milk yield) and quality (taste) of milk before purchase. Manual assessment is subjective and error-prone.

## Solution

Built a dual-model ML system:
1. **Regression model** predicts annual milk yield with R² = 0.83
2. **Classification model** predicts milk taste with 92% precision

Together, these models identify cows meeting both criteria: minimum 6,000 kg annual yield AND tasty milk.

## Key Findings

- Cow breed and father's breed are strong predictors of milk yield
- Feed nutrition (protein, energy) significantly impacts production
- Pasture type affects both yield and milk quality
- Age and current fat/protein content inform quality predictions

## Tech Stack

`Python` `Pandas` `Scikit-learn` `Statsmodels` `Matplotlib` `Seaborn`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook livestock_selection_ml.ipynb
```

## Project Structure

```
livestock_selection_ml/
├── README.md                        # This file
├── requirements.txt                 # Project dependencies
├── livestock_selection_ml.ipynb    # Main analysis notebook
└── reports/
    └── business_report.md          # Business recommendations
```

## Methodology

### Data

| Dataset | Description | Records |
|---------|-------------|---------|
| ferma_main.csv | Current herd data | ~600 cows |
| ferma_dad.csv | Father information | Breeding data |
| cow_buy.csv | Purchase candidates | New cows to evaluate |

### Features

**Numerical:**
- milk_yield_kg: Annual milk production
- energy_feed: Feed energy content (EKE)
- raw_protein: Protein in feed (g)
- sugar_protein_ratio: Feed composition
- fat_content: Milk fat percentage
- protein_content: Milk protein percentage

**Categorical:**
- breed: Cow breed
- pasture_type: Grazing landscape
- father_breed: Father's breed
- age: Young (<2 years) / Mature (>2 years)

### Approach

1. **Data Integration** — Merge herd, father, and purchase datasets
2. **EDA** — Analyze distributions, correlations, breed effects
3. **Feature Engineering** — Encode categoricals, handle multicollinearity
4. **Regression Model** — Predict annual milk yield
5. **Classification Model** — Predict milk taste probability
6. **Selection System** — Apply both models to purchase candidates

### Models

**Regression (Milk Yield):**

| Model | R² (Test) | RMSE | Notes |
|-------|-----------|------|-------|
| Linear Regression | 0.75 | 227 kg | Baseline |
| Ridge Regression | 0.79 | 205 kg | Regularized |
| Gradient Boosting | 0.83 | 188 kg | **Best** |

**Classification (Milk Quality):**

| Threshold | Precision | Recall | Notes |
|-----------|-----------|--------|-------|
| 0.60 | 0.71 | 0.74 | Balanced |
| 0.79 | 0.92 | 0.12 | High precision |
| 0.84 | 1.00 | 0.05 | Perfect precision |

## Selection Criteria

A cow is recommended for purchase if:
1. **Predicted yield ≥ 6,000 kg/year** (with 95% confidence)
2. **Predicted probability of tasty milk > threshold** (precision-optimized)

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
