# Portfolio Projects Improvement Plan

> Comprehensive roadmap for transforming ALL Yandex Practicum DS projects into production-ready portfolio.

**Created:** 2026-01-02
**Updated:** 2026-01-02
**Status:** Phase 2 Complete
**Scope:** ALL 24 projects in repository

---

## Progress Overview

### Completion Status

| Phase | Status | Projects Done |
|-------|--------|---------------|
| Phase 0 | ✅ Complete | 1/1 |
| Phase 1 | ✅ Complete | 3/3 |
| Phase 2 | ✅ Complete | 4/4 |
| Phase 3 | ⏳ Pending | 0/5 |
| Phase 4 | ⏳ Pending | 0/7 |

### Completed Projects

| Project | Folder | Status |
|---------|--------|--------|
| Project Template | `project_template` | ✅ README template for all projects |
| Music Preference Analysis | `music_preference_analysis` | ✅ README, requirements, business report |
| Credit Risk Analysis | `credit_risk_analysis` | ✅ README, requirements, business report |
| Multimodal Image-Text Matching | `multimodal_image_text_matching` | ✅ README, requirements, cleaned up |
| Taxi Demand Forecasting | `taxi_demand_forecasting` | ✅ Full refactor with business report |
| Customer Churn Prediction | `customer_churn_prediction` | ✅ Full refactor with business report |
| Livestock Selection ML | `livestock_selection_ml` | ✅ Full refactor with business report |
| Toxic Comment Detection | `toxic_comment_detection` | ✅ Full refactor, word clouds, POS-lemmatization |

### Deleted/Merged

| Original | Action | Reason |
|----------|--------|--------|
| `24_toxic_comments_processing` | DELETED | Merged into `toxic_comment_detection` |
| `2_children_and_loan` | TO DELETE | Duplicate of credit_risk_analysis |

---

## Table of Contents

1. [Project Improvement Requirements](#project-improvement-requirements)
2. [Naming Convention](#naming-convention)
3. [Complete Project Renaming Plan](#complete-project-renaming-plan)
4. [Priority Order](#priority-order)
5. [Project Template Specification](#project-template-specification)
6. [Detailed Project Plans](#detailed-project-plans)
7. [Implementation Checklist](#implementation-checklist)

---

## Project Improvement Requirements

### Business Report Requirements

Each featured project MUST have a `reports/business_report.md` with:

#### Structure
```
reports/
├── business_report.md      # Main report in storytelling style
└── images/                  # All visualizations referenced in report
    ├── figure1.png
    ├── figure2.png
    └── ...
```

#### Writing Style
- **Storytelling approach** — write like explaining to a business stakeholder
- **No technical jargon** without explanation
- **Start with the problem** — why does this matter?
- **Show, don't tell** — use visualizations to support claims
- **Honest assessment** — acknowledge limitations and failures

#### Required Sections
1. **Executive Summary** — key numbers, one-paragraph summary
2. **The Data/Problem** — what we're working with, class distributions, data quality
3. **Key Visualizations** — 3-5 figures with captions explaining insights
4. **Model Performance** — metrics table, confusion matrix if classification
5. **Business Recommendations** — actionable next steps
6. **Technical Notes** — brief methodology for technical readers

#### Image Requirements
- All images saved via `plt.savefig('reports/images/filename.png', dpi=150, bbox_inches='tight')`
- Image references in markdown: `![Caption](images/filename.png)`
- Figure captions with interpretation: `*Figure 1: What this shows and why it matters*`
- Verify all image paths match actual files before commit

### Notebook Requirements

#### Cell Structure
1. **Markdown intro cell** — project title, objectives, author
2. **Imports cell** — all imports in one place
3. **Data loading** — with shape/info output
4. **EDA section** — visualizations with `savefig` calls
5. **Preprocessing** — documented transformations
6. **Modeling** — clear comparison of approaches
7. **Conclusions** — markdown summary of results

#### Code Quality
- Remove empty output cells before commit
- Clear variable names
- Comments for non-obvious logic
- No hardcoded paths (use relative `../../datasets/`)

#### Visualization Standards
- Always include `savefig` for key plots
- Use `figsize` appropriate for report (min 10x6 for single, 14x10 for subplots)
- Include titles, labels, legends
- Use consistent color schemes

### Pre-Commit Checklist

Before committing any project:

- [ ] Run all notebook cells — verify no errors
- [ ] Check all `savefig` paths create files in `reports/images/`
- [ ] Verify report image references match actual files
- [ ] Confirm metrics in report match notebook outputs
- [ ] Remove temporary/debug cells

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

---

## Complete Project Renaming Plan

### All Projects Mapping

| # | Current Folder | New Folder | Status |
|---|----------------|------------|--------|
| 1 | `01_project_template` | `project_template` | ✅ Done |
| 2 | `1_music_of_big_cities` | `music_preference_analysis` | ✅ Done |
| 3 | `2_borrower_reliability` | `credit_risk_analysis` | ✅ Done |
| 4 | `2_children_and_loan` | **DELETE** | ⏳ To delete |
| 5 | `3_russian_cinema_analysis` | `russian_cinema_market` | ⏳ Pending |
| 6 | `6_ml_farm` | `dairy_herd_optimization` | ⏳ Pending |
| 7 | `8_ml_hr` | `hr_employee_analytics` | ⏳ Pending |
| 8 | `9_geo_bootstrap` | `oil_well_location_selection` | ⏳ Pending |
| 9 | `10_ml_oneclick` | `automated_ml_pipeline` | ⏳ Pending |
| 10 | `11_sideproject_accord` | `music_genre_classification` | ⏳ Pending |
| 11 | `12_sideproject_expresstrip` | `trip_prediction_trees` | ⏳ Pending |
| 12 | `13_sideproject_seatreats` | `order_cancellation_prediction` | ⏳ Pending |
| 13 | `14_marketing_analysis` | `marketing_campaign_forecasting` | ⏳ Pending |
| 14 | `18_customer_behavior_analysis` | `customer_churn_prediction` | ✅ Done |
| 15 | `19_cow_selection_ml` | `livestock_selection_ml` | ✅ Done |
| 16 | `20_car_price_determination` | `car_price_prediction` | ⏳ Pending |
| 17 | `21_star_temperature_prediction` | **REVIEW** | ⏳ Check if empty |
| 18 | `22_time_series_prediction` | `taxi_demand_forecasting` | ✅ Done |
| 19 | `23_text_processing` | `text_sentiment_classification` | ⏳ Pending |
| 20 | `24_toxic_comments_processing` | ~~`toxic_comment_detection`~~ | 🗑️ DELETED (merged) |
| 21 | `25_scooter_rental_analysis` | `scooter_rental_analytics` | ⏳ Pending |
| 22 | `29_machine_vision` | `multimodal_image_text_matching` | ✅ Done |

### Projects to Delete/Review

| Project | Issue | Action | Status |
|---------|-------|--------|--------|
| `2_children_and_loan` | Duplicate of credit_risk_analysis | DELETE | ⏳ Pending |
| `16_startup_success_prediction` | Possibly empty | REVIEW → DELETE if empty | ⏳ Pending |
| `17_housing_price_prediction` | Possibly empty | REVIEW → DELETE if empty | ⏳ Pending |
| `21_star_temperature_prediction` | Template only | REVIEW → DELETE if no content | ⏳ Pending |
| `24_toxic_comments_processing` | Merged into toxic_comment_detection | DELETE | ✅ DELETED |

---

## Priority Order

### Execution Sequence

```
Phase 0: Template ✅ COMPLETE
    └── project_template ✅

Phase 1: Foundation Projects ✅ COMPLETE
    ├── music_preference_analysis ✅
    ├── credit_risk_analysis ✅
    └── multimodal_image_text_matching ✅

Phase 2: Featured Portfolio Projects ✅ COMPLETE
    ├── taxi_demand_forecasting ✅
    ├── customer_churn_prediction ✅
    ├── livestock_selection_ml ✅
    └── toxic_comment_detection ✅

Phase 3: Secondary Projects ⏳ PENDING
    ├── russian_cinema_market
    ├── car_price_prediction
    ├── scooter_rental_analytics
    ├── oil_well_location_selection
    └── text_sentiment_classification

Phase 4: Remaining Projects ⏳ PENDING
    ├── dairy_herd_optimization
    ├── hr_employee_analytics
    ├── automated_ml_pipeline
    ├── music_genre_classification
    ├── trip_prediction_trees
    ├── order_cancellation_prediction
    └── marketing_campaign_forecasting
```

---

## Project Template Specification

### Folder Structure (Standard)

```
project_name/
├── README.md                 # Required: Executive summary
├── requirements.txt          # Required: Dependencies
├── project_name.ipynb        # Main analysis notebook
└── reports/
    ├── business_report.md    # Storytelling report
    └── images/               # All visualizations
        ├── figure1.png
        └── figure2.png
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

## Project Structure

[Folder tree]

## Author

**Arina Fedorova** - Data Scientist

---

*Educational project | Yandex Practicum Data Science Program*
```

---

## Detailed Project Plans

### Phase 3: Secondary Projects (Next Up)

#### russian_cinema_market

| Task | Priority | Status |
|------|----------|--------|
| Rename folder | HIGH | ⏳ |
| Create README (EN) | HIGH | ⏳ |
| Add requirements.txt | HIGH | ⏳ |
| Create business report | HIGH | ⏳ |
| Add visualizations | MEDIUM | ⏳ |

#### car_price_prediction

| Task | Priority | Status |
|------|----------|--------|
| Rename folder | HIGH | ⏳ |
| Create README (EN) | HIGH | ⏳ |
| Add requirements.txt | HIGH | ⏳ |
| Create business report | HIGH | ⏳ |
| Document model comparison | MEDIUM | ⏳ |

#### scooter_rental_analytics

| Task | Priority | Status |
|------|----------|--------|
| Rename folder | HIGH | ⏳ |
| Create README (EN) | HIGH | ⏳ |
| Add requirements.txt | HIGH | ⏳ |
| Create business report | HIGH | ⏳ |

#### oil_well_location_selection

| Task | Priority | Status |
|------|----------|--------|
| Rename folder | HIGH | ⏳ |
| Create README (EN) | HIGH | ⏳ |
| Add requirements.txt | HIGH | ⏳ |
| Create business report | HIGH | ⏳ |
| Document bootstrap methodology | MEDIUM | ⏳ |

#### text_sentiment_classification

| Task | Priority | Status |
|------|----------|--------|
| Rename folder | HIGH | ⏳ |
| Create README (EN) | HIGH | ⏳ |
| Add requirements.txt | HIGH | ⏳ |
| Create business report | HIGH | ⏳ |

---

## Implementation Checklist

### Per-Project Checklist

- [ ] Rename folder (remove numbers, add descriptive name)
- [ ] Create/Update README.md (English, with Quick Results)
- [ ] Add requirements.txt
- [ ] Create folder structure (reports/images/)
- [ ] Write business_report.md in storytelling style
- [ ] Add savefig calls to notebook for all key visualizations
- [ ] Run notebook and save all images
- [ ] Verify all image references in report match files
- [ ] Verify metrics in report match notebook outputs
- [ ] Delete redundant files
- [ ] Commit with descriptive message

### Global Tasks

- [ ] Update main README.md with new project names
- [ ] Update Featured Projects section
- [ ] Delete empty/duplicate projects
- [ ] Verify all links work
- [ ] Final review pass

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-01-02 | Remove all numeric prefixes | Cleaner, more professional look |
| 2026-01-02 | Add skills in parentheses | Immediate visibility of demonstrated capabilities |
| 2026-01-02 | Business reports in storytelling style | More engaging for recruiters/stakeholders |
| 2026-01-02 | Merged 24_toxic_comments_processing into toxic_comment_detection | Better content (word clouds, POS-lemmatization) |
| 2026-01-02 | Renamed baseline_establishment_ml → livestock_selection_ml | More descriptive of actual problem |

---

*Document updated: 2026-01-02*
*Next action: Phase 3 — Secondary Projects*
