# Livestock Selection ML (Regression + Classification)

> Dual-model system for data-driven cow selection: predicting milk quality and yield to minimize purchasing risks.

## Quick Results

| Task | Model | Status | Notes |
|------|-------|--------|-------|
| Milk Quality | Logistic Regression | Ready | Precision-optimized |
| Milk Yield | Gradient Boosting | Needs work | Negative R² on test |
| Selection | Quality-based | Operational | Manual yield assessment |

## Problem Statement

A dairy farm needs to make objective purchasing decisions when selecting new cows. The farmer wants to minimize risk by predicting both the quantity (annual milk yield) and quality (taste) of milk before purchase. Manual assessment is subjective and error-prone.

## Solution

Built a dual-model ML system with mixed results:
1. **Classification model** predicts milk taste successfully
2. **Regression model** requires additional feature engineering

The quality model enables selection based on taste prediction, while yield assessment remains manual pending model improvement.

## Key Findings

- Milk taste can be predicted from fat content, protein content, and breed
- Simple features are insufficient for accurate yield prediction
- Feature engineering and breed genetics data would improve yield model
- The quality classification threshold can be tuned for precision vs recall

## Tech Stack

`Python` `Pandas` `Scikit-learn` `Matplotlib` `Seaborn`

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

1. **Data Integration** - Merge herd and father datasets
2. **EDA** - Analyze distributions, correlations, breed effects
3. **Feature Engineering** - Encode categoricals, handle outliers
4. **Regression Model** - Attempt to predict annual milk yield
5. **Classification Model** - Predict milk taste probability
6. **Selection System** - Quality-based selection with manual yield check

### Models

**Regression (Milk Yield):**

Current models show poor generalization (negative test R²). Additional work needed:
- Outlier removal (filter extreme yield values)
- Feature engineering (squared terms, interactions)
- Breed genetics integration

**Classification (Milk Quality):**

Logistic Regression with threshold optimization for precision.

## Selection Approach

A cow is recommended for purchase if:
1. **Predicted probability of tasty milk > threshold** (quality model)
2. **Manual yield assessment** based on breed, age, feed history

## Future Improvements

1. Improve regression with better features and outlier handling
2. Add father's milk production records as predictor
3. Integrate seasonal and age-specific yield patterns
4. Test ensemble methods for quality classification

## Author

**Arina Fedorova** - Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
