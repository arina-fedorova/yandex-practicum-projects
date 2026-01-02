# Scooter Rental Analytics (Statistical Testing, Revenue Analysis)

> Statistical analysis of GoFast electric scooter service to optimize revenue and marketing strategies.

## Quick Results

| Metric | Value | Insight |
|--------|-------|---------|
| Subscriber Revenue | ~400₽/month | 2x higher than free users |
| Subscription Rate | 46% | Room for conversion growth |
| Core Demographic | 20-30 years | Young urban professionals |
| Trip Duration | ~17 minutes avg | Consistent across users |

## Problem Statement

GoFast operates electric scooter rentals with two user types: free users (pay-per-ride) and Ultra subscribers (monthly fee + lower rates). The business needed to understand:
- Who generates more revenue?
- How do subscriber behaviors differ?
- What marketing strategies should be prioritized?

## Solution

Conducted comprehensive statistical analysis including:
- Exploratory data analysis of 18,000+ rides across 1,500+ users
- Hypothesis testing (t-tests) to validate business assumptions
- Probability calculations for marketing campaign planning
- Seasonal revenue pattern analysis

## Key Findings

1. **Subscribers are 2x more valuable** — Despite lower per-minute rates, they generate ~400₽ vs ~200₽ monthly
2. **Geographic opportunity** — Pyatigorsk outperforms Moscow, suggesting untapped potential in large cities
3. **Seasonal patterns** — Peak revenue in April (spring) and September (back-to-work)
4. **Subscribers ride longer, not farther** — More time per trip, same average distance

## Hypothesis Testing Results

| Hypothesis | Result | p-value |
|------------|--------|---------|
| Subscribers ride longer | Confirmed | <0.001 |
| Subscriber distance > 3130m | Not confirmed | 0.92 |
| Subscribers generate more revenue | Confirmed | <0.001 |

## Tech Stack

`Python` `Pandas` `SciPy` `Matplotlib` `Seaborn` `Statistical Testing`

## Project Structure

```
scooter_rental_analytics/
├── README.md
├── requirements.txt
├── scooter_rental_analysis.ipynb
└── reports/
    ├── business_report.md
    └── images/
        ├── users_by_city.png
        ├── subscription_split.png
        ├── age_distribution.png
        └── ...
```

## Key Visualizations

- User distribution by city
- Subscription split (46% Ultra vs 54% Free)
- Age demographics
- Trip distance and duration distributions
- Revenue comparison by subscription type
- Seasonal revenue trends

## Author

**Arina Fedorova** — Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
