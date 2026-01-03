# Russian Cinema Market Analysis

Comprehensive analysis of film distribution trends and government support effectiveness in Russian cinema.

## Results

| Metric | Value |
|--------|-------|
| Films Analyzed | 2,000+ |
| Time Period | 2010-2019 |
| Government-Supported Films | 500+ |
| Supported vs Unsupported | Higher box office for supported |

## Key Findings

- **Government support correlates with higher box office** - supported films show better commercial performance
- **Family-friendly films dominate** - 6+ and 12+ age ratings generate highest revenue
- **Genre matters** - comedies and action films lead box office returns
- **Russian films gaining ground** - domestic productions increasingly competitive

## Project Structure

```
russian_cinema_analysis/
├── russian_cinema_analysis.ipynb  # Main analysis notebook
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
└── reports/
    ├── business_report.md         # Business-focused summary
    └── images/                    # Visualizations
```

## Methodology

1. **Data Integration**: Merged film registry with box office data
2. **Data Cleaning**: Handled missing values, standardized categories
3. **Feature Engineering**: Created support ratio, profitability metrics
4. **EDA**: Analyzed trends by year, genre, age rating
5. **Government Support Analysis**: Compared supported vs unsupported films

## Data Description

**mkrf_movies** - Film registry with distribution certificates:
- `title` — film title
- `puNumber` — distribution certificate number
- `show_start_date` — premiere date
- `type` — film type
- `film_studio` — production studio
- `production_country` — country of origin
- `director` — director
- `producer` — producer
- `age_restriction` — age rating
- `refundable_support` — refundable government support amount
- `nonrefundable_support` — non-refundable government support amount
- `financing_source` — government financing source
- `budget` — total film budget (includes government support)
- `ratings` — Kinopoisk rating
- `genres` — film genre

**mkrf_shows** - Box office data from Russian theaters:
- `puNumber` — distribution certificate number
- `box_office` — revenue in rubles

## Technologies

- Python 3.10+
- pandas, numpy
- matplotlib, seaborn

## Author

Arina Fedorova
