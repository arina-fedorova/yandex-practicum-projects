# Portfolio Projects Improvement Plan

> Comprehensive roadmap for transforming ALL Yandex Practicum DS projects into production-ready portfolio.

**Created:** 2026-01-02
**Updated:** 2026-01-02
**Status:** Planning Phase
**Scope:** ALL 24 projects in repository

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Naming Convention](#naming-convention)
3. [Complete Project Renaming Plan](#complete-project-renaming-plan)
4. [Priority Order](#priority-order)
5. [Project Template Specification](#project-template-specification)
6. [Detailed Project Plans](#detailed-project-plans)
7. [Implementation Checklist](#implementation-checklist)

---

## Executive Summary

### Goal

Transform ALL educational Data Science projects into a cohesive, professional portfolio that:
- Demonstrates end-to-end ML capabilities
- Uses consistent naming reflecting skills demonstrated
- Follows production-ready organization
- Provides quick overview capability (30-second scan)

---

## Naming Convention

### Format

| Location | Format | Example |
|----------|--------|---------|
| **Folder** | `snake_case` (no skills) | `taxi_demand_forecasting/` |
| **README title** | Title Case + skills in parentheses | `# Taxi Demand Forecasting (Time Series, Forecasting)` |

### Rules

1. **No numeric prefixes** — remove all `01_`, `22_`, etc.
2. **Descriptive folder name** — reflects the business problem or domain
3. **Skills in README title** — 2-4 key skills in parentheses
4. **Snake_case** — for folder names (no spaces, no special characters)
5. **English only** — all names in English

### Examples

| Current Folder | New Folder | README Title |
|----------------|------------|--------------|
| `22_time_series_prediction` | `taxi_demand_forecasting` | `# Taxi Demand Forecasting (Time Series, Forecasting)` |
| `24_toxic_comments_processing` | `toxic_comment_detection` | `# Toxic Comment Detection (NLP, Text Classification, BERT)` |
| `29_machine_vision` | `multimodal_image_text_matching` | `# Multimodal Image-Text Matching (Computer Vision, BERT, Ensemble)` |

---

## Complete Project Renaming Plan

### All Projects Mapping

| # | Current Folder | New Folder | README Title (with skills) |
|---|----------------|------------|----------------------------|
| 1 | `01_project_template` | `project_template` | Project Template (Template) |
| 2 | `1_music_of_big_cities` | `music_preference_analysis` | Music Preference Analysis (EDA, Statistical Testing) |
| 3 | `2_borrower_reliability` | `credit_risk_analysis` | Credit Risk Analysis (Statistical Testing, Risk Modeling) |
| 4 | `2_children_and_loan` | **DELETE** - duplicate | N/A |
| 5 | `3_russian_cinema_analysis` | `russian_cinema_market` | Russian Cinema Market (EDA, Financial Analysis) |
| 6 | `6_ml_farm` | `dairy_herd_optimization` | Dairy Herd Optimization (Regression, Classification) |
| 7 | `8_ml_hr` | `hr_employee_analytics` | HR Employee Analytics (Classification, HR Analytics) |
| 8 | `9_geo_bootstrap` | `oil_well_location_selection` | Oil Well Location Selection (Regression, Bootstrap, Risk Analysis) |
| 9 | `10_ml_oneclick` | `automated_ml_pipeline` | Automated ML Pipeline (AutoML, Pipeline) |
| 10 | `11_sideproject_accord` | `music_genre_classification` | Music Genre Classification (Classification, Audio Features) |
| 11 | `12_sideproject_expresstrip` | `trip_prediction_trees` | Trip Prediction Trees (Decision Trees, Classification) |
| 12 | `13_sideproject_seatreats` | `order_cancellation_prediction` | Order Cancellation Prediction (Classification, SVM) |
| 13 | `14_marketing_analysis` | `marketing_campaign_forecasting` | Marketing Campaign Forecasting (Forecasting, Segmentation) |
| 14 | `16_startup_success_prediction` | **REVIEW** - check if empty | TBD |
| 15 | `17_housing_price_prediction` | **REVIEW** - check if empty | TBD |
| 16 | `18_customer_behavior_analysis` | `customer_churn_prediction` | Customer Churn Prediction (Classification, SHAP, Segmentation) |
| 17 | `19_cow_selection_ml` | `baseline_establishment_ml` | Baseline Establishment ML (Regression, Classification, Multi-objective) |
| 18 | `20_car_price_determination` | `car_price_prediction` | Car Price Prediction (Regression, Gradient Boosting) |
| 19 | `21_star_temperature_prediction` | **REVIEW** - check if template only | TBD |
| 20 | `22_time_series_prediction` | `taxi_demand_forecasting` | Taxi Demand Forecasting (Time Series, Forecasting) |
| 21 | `23_text_processing` | `text_sentiment_classification` | Text Sentiment Classification (NLP, Text Classification) |
| 22 | `24_toxic_comments_processing` | `toxic_comment_detection` | Toxic Comment Detection (NLP, BERT, Text Classification) |
| 23 | `25_scooter_rental_analysis` | `scooter_rental_analytics` | Scooter Rental Analytics (EDA, Statistical Testing) |
| 24 | `29_machine_vision` | `multimodal_image_text_matching` | Multimodal Image-Text Matching (Computer Vision, BERT, Ensemble) |

### Projects to Delete/Review

| Project | Issue | Action |
|---------|-------|--------|
| `2_children_and_loan` | Duplicate of `2_borrower_reliability` | DELETE |
| `16_startup_success_prediction` | Possibly empty | REVIEW → DELETE if empty |
| `17_housing_price_prediction` | Possibly empty | REVIEW → DELETE if empty |
| `21_star_temperature_prediction` | Template only | REVIEW → DELETE if no content |

---

## Priority Order

### Execution Sequence

```
Phase 0: Template
    └── project_template

Phase 1: Foundation Projects
    ├── music_preference_analysis
    ├── credit_risk_analysis
    └── multimodal_image_text_matching

Phase 2: Featured Portfolio Projects
    ├── taxi_demand_forecasting
    ├── customer_churn_prediction
    ├── baseline_establishment_ml
    └── toxic_comment_detection

Phase 3: Secondary Projects
    ├── russian_cinema_market
    ├── car_price_prediction
    ├── scooter_rental_analytics
    ├── oil_well_location_selection
    └── text_sentiment_classification

Phase 4: Remaining Projects
    ├── dairy_herd_optimization
    ├── hr_employee_analytics
    ├── automated_ml_pipeline
    ├── music_genre_classification
    ├── trip_prediction_trees
    ├── order_cancellation_prediction
    └── marketing_campaign_forecasting
```

### Priority Rationale

| Phase | Rationale |
|-------|-----------|
| 0 | Template defines standards for all other projects |
| 1 | Foundation projects + most complex (multimodal) |
| 2 | Featured projects, highest visibility |
| 3 | Good projects with clear business value |
| 4 | Supporting projects, lower priority |

---

## Project Template Specification

### Folder Structure (Standard)

```
project_name/
├── README.md                 # Required: Executive summary + documentation
├── requirements.txt          # Required: Dependencies
├── notebooks/
│   └── analysis.ipynb       # Main analysis notebook
├── data/
│   └── README.md            # Data sources documentation
└── reports/
    └── figures/             # Key visualizations
```

### README Template

```markdown
# Project Name (Skill1, Skill2)

> One-line description of business problem solved.

## Quick Results

| Metric | Value | Target |
|--------|-------|--------|
| Key Metric | X.XX | ≥Y.YY |

## Problem Statement

[2-3 sentences about the business problem]

## Solution

[2-3 sentences about the approach]

## Key Findings

- Finding 1 with numbers
- Finding 2 with impact
- Finding 3 with insight

## Tech Stack

`Python` `Pandas` `Scikit-learn` `[Other]`

## Quick Start

\`\`\`bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
\`\`\`

## Project Structure

[Folder tree]

## Methodology

### Data
- Source: [description]
- Size: X records

### Approach
1. Step 1
2. Step 2
3. Step 3

## Author

**Arina Fedorova** - Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
```

---

## Detailed Project Plans

### Phase 0: Template

#### project_template

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `01_project_template` → `project_template` |
| Update README | HIGH | Apply new template format |
| Add skills tag | HIGH | Add "(Template)" to title |
| Update references | MEDIUM | Fix links in main README |

---

### Phase 1: Foundation Projects

#### music_preference_analysis (EDA, Statistical Testing)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `1_music_of_big_cities` → `music_preference_analysis` |
| Create README (EN) | HIGH | Yandex Music user behavior analysis |
| Add requirements.txt | HIGH | pandas, matplotlib, scipy |
| Rename notebook | MEDIUM | Descriptive name (e.g., `analysis.ipynb`) |
| Create folder structure | MEDIUM | notebooks/, data/, reports/ |

**Key Metrics to Document:**
- Hypothesis testing results
- City comparison statistics
- User behavior patterns

---

#### credit_risk_analysis (Statistical Testing, Risk Modeling)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `2_borrower_reliability` → `credit_risk_analysis` |
| Create README (EN) | HIGH | Credit scoring, loan default prediction |
| Add requirements.txt | HIGH | pandas, scipy, matplotlib |
| Document findings | HIGH | Risk factors, statistical significance |
| Delete duplicate | HIGH | Remove `2_children_and_loan` |

**Key Metrics to Document:**
- Default rates by category
- Statistical test results
- Risk factor importance

---

#### multimodal_image_text_matching (Computer Vision, BERT, Ensemble)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `29_machine_vision` → `multimodal_image_text_matching` |
| Create README (EN) | HIGH | Explain ResNet50 + BERT approach |
| Create requirements.txt | HIGH | Extract from env/ |
| Document models | HIGH | What each .pkl does |
| Select final notebook | HIGH | Keep one, document choice |
| Rename notebook | MEDIUM | `multimodal_analysis.ipynb` |
| Add model cards | MEDIUM | BERT, ResNet50 documentation |

**Key Metrics to Document:**
- Ensemble model performance
- Individual model comparison
- Feature extraction methodology

---

### Phase 2: Featured Portfolio Projects

#### taxi_demand_forecasting (Time Series, Forecasting)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `22_time_series_prediction` → `taxi_demand_forecasting` |
| Create README (EN) | HIGH | RMSE, ADF test, patterns |
| Delete extra notebooks | HIGH | Keep only final version |
| Add requirements.txt | HIGH | pandas, statsmodels, sklearn |
| Rename notebook | MEDIUM | `time_series_analysis.ipynb` |

**Key Metrics:**
- RMSE: Below 48 target
- ADF p-value: 0.0289
- Peak patterns identified

---

#### customer_churn_prediction (Classification, SHAP, Segmentation)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `18_customer_behavior_analysis` → `customer_churn_prediction` |
| Translate README | HIGH | Russian → English |
| Add Quick Results | HIGH | Classification metrics |
| Add requirements.txt | HIGH | pandas, sklearn, shap |
| Rename notebook | MEDIUM | `churn_analysis.ipynb` |

---

#### baseline_establishment_ml (Regression, Classification, Multi-objective)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `19_cow_selection_ml` → `baseline_establishment_ml` |
| Translate README | HIGH | Russian → English |
| Add Quick Results | HIGH | Regression + classification metrics |
| Add requirements.txt | HIGH | pandas, sklearn |
| Rename notebook | MEDIUM | `baseline_modeling.ipynb` |

---

#### toxic_comment_detection (NLP, BERT, Text Classification)

| Task | Priority | Description |
|------|----------|-------------|
| Rename folder | HIGH | `24_toxic_comments_processing` → `toxic_comment_detection` |
| Create README (EN) | HIGH | F1: 0.778, methodology |
| Add requirements.txt | HIGH | pandas, nltk, sklearn, transformers |
| Rename notebook | MEDIUM | `nlp_classification.ipynb` |

**Key Metrics:**
- F1-score: 0.7783
- Accuracy: 95.64%
- Dataset: 159,292 comments

---

### Phase 3: Secondary Projects

| Project | Key Tasks |
|---------|-----------|
| `russian_cinema_market` | Rename, README, requirements |
| `car_price_prediction` | Rename, README (LightGBM vs CatBoost comparison) |
| `scooter_rental_analytics` | Rename, README, statistical findings |
| `oil_well_location_selection` | Rename, README (bootstrap methodology) |
| `text_sentiment_classification` | Rename, README (TF-IDF approach) |

---

### Phase 4: Remaining Projects

| Project | Key Tasks |
|---------|-----------|
| `dairy_herd_optimization` | Rename, README, requirements |
| `hr_employee_analytics` | Rename, README |
| `automated_ml_pipeline` | Rename, README |
| `music_genre_classification` | Rename, README |
| `trip_prediction_trees` | Rename, README |
| `order_cancellation_prediction` | Rename, README |
| `marketing_campaign_forecasting` | Rename, README |

---

## Implementation Checklist

### Per-Project Checklist

- [ ] Rename folder (remove numbers, add descriptive name)
- [ ] Rename notebook (reflect content + skills)
- [ ] Create/Update README.md (English, with Quick Results)
- [ ] Add requirements.txt
- [ ] Create folder structure (notebooks/, data/, reports/)
- [ ] Delete redundant files
- [ ] Update main repository README references

### Global Tasks

- [ ] Update main README.md with new project names
- [ ] Update Featured Projects section
- [ ] Delete empty/duplicate projects
- [ ] Verify all links work
- [ ] Final review pass

---

## Git Strategy

### Rename Approach

```bash
# For each project:
git mv old_folder_name new_folder_name
git add .
git commit -m "Rename: old_name → new_name (Skills)"
```

### Commit Convention

```
Rename: 22_time_series_prediction → taxi_demand_forecasting (Time Series, Forecasting)

- Rename folder to reflect business problem
- Add skills tag to project name
- [Additional changes if any]
```

---

## Timeline Estimate

| Phase | Projects | Est. Effort |
|-------|----------|-------------|
| Phase 0 | 1 template | 1 hour |
| Phase 1 | 3 projects | 4-5 hours |
| Phase 2 | 4 projects | 6-8 hours |
| Phase 3 | 5 projects | 5-6 hours |
| Phase 4 | 7 projects | 5-6 hours |
| **Total** | **20 projects** | **21-26 hours** |

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-01-02 | Remove all numeric prefixes | Cleaner, more professional look |
| 2026-01-02 | Add skills in parentheses | Immediate visibility of demonstrated capabilities |
| 2026-01-02 | Template first priority | Establishes standard for all projects |
| 2026-01-02 | English only | Target audience is international |

---

*Document updated: 2026-01-02*
*Next action: Review and approve, then begin Phase 0*
