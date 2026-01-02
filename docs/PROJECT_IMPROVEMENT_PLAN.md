# Portfolio Projects Improvement Plan

> Context document for bringing Yandex Practicum DS projects to production-ready status.

**Created:** 2026-01-02
**Status:** Planning Phase
**Target:** 5 key portfolio projects

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Current State Analysis](#current-state-analysis)
3. [Best Practices Research](#best-practices-research)
4. [Improved Template](#improved-template)
5. [Project-Specific Plans](#project-specific-plans)
6. [Prioritization](#prioritization)
7. [Work Format Options](#work-format-options)
8. [Open Questions](#open-questions)

---

## Executive Summary

### Goal
Transform 5 educational Data Science projects into portfolio-ready presentations that demonstrate:
- End-to-end ML capabilities
- Production-ready code organization
- Clear documentation for recruiters (30-second scan)
- Relevance to H1OX position requirements

### Key Projects (CV-Listed)

| # | Project | H1OX Relevance |
|---|---------|----------------|
| 22 | Time Series Prediction | Wearable device metrics, trend analysis |
| 18 | Customer Behavior Analysis | User tracking, personalization, SHAP |
| 19 | Cow Selection ML | Baseline establishment methodology |
| 24 | Toxic Comments Processing | NLP/LLM integration capability |
| 29 | Machine Vision | Multimodal learning (ResNet50 + BERT) |

---

## Current State Analysis

### Summary Table

| Aspect | Project 22 | Project 18 | Project 19 | Project 24 | Project 29 |
|--------|-----------|-----------|-----------|-----------|-----------|
| **README.md** | No | Yes (RU) | Yes (RU) | No | No |
| **requirements.txt** | No | No | No | No | No |
| **Notebooks** | 5 (chaotic) | 1 | 1 | 1 | 2 |
| **data/ folder** | No | No | No | No | No |
| **src/ folder** | No | No | No | No | No |
| **Pre-trained Models** | No | No | No | No | Yes (14) |
| **Documentation Quality** | None | Good (RU) | Good (RU) | Basic | None |
| **Production Readiness** | LOW | MEDIUM-HIGH | MEDIUM-HIGH | LOW-MEDIUM | MEDIUM |

### Detailed Project Analysis

#### Project 22: Time Series Prediction (Taxi Forecasting)

**Location:** `projects/22_time_series_prediction`

**Current Structure:**
```
22_time_series_prediction/
├── create_notebook.py (5.4 KB)
├── test.py (16 bytes - minimal)
├── TaxiForecast_Complete.ipynb (440 bytes - empty)
├── TaxiForecast_Complete_Full.ipynb (119 bytes - empty)
├── TaxiForecast_Fixed.ipynb (772 KB - main)
├── TaxiForecast_Fixed_Final.ipynb (776 KB - final)
└── TimeForecast.ipynb (50 KB)
```

**Issues:**
- 5 notebooks with unclear naming (which is final?)
- No README documentation
- No requirements.txt
- No organized folder structure
- Empty/placeholder notebooks mixed with working ones

**Key Metrics (from analysis):**
- RMSE: Below target of 48
- ADF test p-value: 0.0289 (stationary)
- Peak patterns: midnight (144 orders), minimum at 6 AM (25 orders)
- Dataset: 26,496 records (March-August 2018)

---

#### Project 18: Customer Behavior Analysis

**Location:** `projects/18_customer_behavior_analysis`

**Current Structure:**
```
18_customer_behavior_analysis/
├── README.md (4035 bytes - well-documented, Russian)
└── Activity_improvement_strategy.ipynb (1.1 MB)
```

**Strengths:**
- Comprehensive README in Russian
- Clear project goals (3 items)
- Data sources documented (4 CSV files)
- Execution steps listed (9 stages)
- Results section with checkmarks

**Issues:**
- README in Russian only (needs EN translation)
- No requirements.txt
- No Quick Results / Executive Summary section
- No folder structure (notebooks/, data/, etc.)

---

#### Project 19: Cow Selection ML

**Location:** `projects/19_cow_selection_ml`

**Current Structure:**
```
19_cow_selection_ml/
├── README.md (2697 bytes - well-documented, Russian)
└── ML_Modeling_Cow_Farm.ipynb (1.7 MB)
```

**Strengths:**
- Well-structured README with data dictionary
- Clear project goals (3 main objectives)
- Detailed data description for 3 datasets
- All CSV fields documented

**Issues:**
- README in Russian only
- No requirements.txt
- Project name doesn't highlight "baseline establishment" (key for H1OX)
- No folder structure

---

#### Project 24: Toxic Comments Processing

**Location:** `projects/24_toxic_comments_processing`

**Current Structure:**
```
24_toxic_comments_processing/
├── project.md (4181 bytes - requirements/guidelines)
└── Toxic_Comments_Processing.ipynb (577 KB)
```

**Issues:**
- No README.md (only project.md with task requirements)
- No requirements.txt
- No documentation of results achieved
- No folder structure

**Key Metrics (from analysis):**
- Test F1-score: 0.7783 (exceeded 0.75 target)
- Test Accuracy: 95.64%
- Dataset: 159,292 comments (10.16% toxic - imbalanced)
- Best model: Logistic Regression (C=2.0)

---

#### Project 29: Machine Vision

**Location:** `projects/29_machine_vision`

**Current Structure:**
```
29_machine_vision/
├── env/ (virtual environment)
├── machine-vision.ipynb (2.5 MB)
├── Арина_Федорова_v1.ipynb (2.6 MB)
├── [14 .pkl model files]
│   ├── bert_model.pkl (438 MB)
│   ├── bert_tokenizer.pkl (629 KB)
│   ├── rf_model.pkl (2.4 MB)
│   ├── mlp_model.pkl (1.2 MB)
│   └── ... (other models)
├── X_image.npy (7 MB)
├── X_text.npy (2.3 MB)
└── y.npy (410 KB)
```

**Strengths:**
- Most mature in terms of ML artifacts
- 14 pre-trained models saved
- Virtual environment present
- Multimodal approach (image + text)

**Issues:**
- No README documentation
- No requirements.txt (would need extraction from env/)
- Large files in repository (BERT model 438 MB)
- Two notebooks with unclear purpose
- No explanation of what each model does

---

## Best Practices Research

### Sources Consulted

1. [KDnuggets - Data Science Portfolio](https://www.kdnuggets.com/develop-stand-out-data-science-portfolio-github)
2. [Dataquest - Share Portfolio on GitHub](https://www.dataquest.io/blog/how-to-share-data-science-portfolio/)
3. [GitHub DS README Template](https://github.com/KalyanM45/Data-Science-Project-Readme-Template)
4. [Medium/Practicum - GitHub Portfolio](https://medium.com/practicum-by-yandex/data-science-portfolio-making-the-most-out-of-github-dac98c536ffc)
5. [GitHub - Python DS Project Organization](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510)

### Key Takeaways

#### Project Structure
- Organize with clear folders: `data/`, `notebooks/`, `src/`, `reports/`
- Number notebooks logically (01_, 02_, etc.)
- Use `requirements.txt` or `environment.yml` for dependencies
- Add `.gitignore` for large files and virtual environments

#### README Requirements
- Must be readable by "average technically competent stranger"
- Include: project name, description, setup/usage instructions
- Add **Quick Results** section for 30-second recruiter scan
- Explain the "why" (context) not just the "what"
- Include both code and non-technical explanations

#### Portfolio Presentation
- Pin important projects on GitHub profile
- Make code easy to run (one-command setup ideal)
- Include end-to-end workflow demonstration
- Add visualizations and key findings prominently

---

## Improved Template

### Recommended Folder Structure

```
project_name/
├── README.md                 # Executive summary + full documentation
├── requirements.txt          # Dependencies (pip freeze)
├── .gitignore               # Exclude data, models, env
│
├── notebooks/               # Jupyter notebooks (numbered)
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/                     # Production-ready Python code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   └── utils.py
│
├── data/                    # Data files (NOT in git)
│   ├── raw/
│   ├── processed/
│   └── README.md            # Data sources & dictionary
│
├── models/                  # Trained models (NOT in git for large files)
│   └── README.md            # Model descriptions
│
└── reports/                 # Generated outputs
    ├── figures/
    └── results.md
```

### README Template

```markdown
# Project Name

> One-line description of what this project does and the business problem it solves.

## Quick Results

| Metric | Value | Target |
|--------|-------|--------|
| F1-Score | 0.778 | ≥0.75 |
| Accuracy | 95.6% | - |
| RMSE | 42.3 | <48 |

## Problem Statement

[2-3 sentences about the business problem and why it matters]

## Solution

[2-3 sentences about the approach taken and key techniques used]

## Key Findings

- Finding 1 with specific numbers
- Finding 2 with business impact
- Finding 3 with actionable insight

## Tech Stack

`Python` `Pandas` `Scikit-learn` `XGBoost` `Statsmodels`

## Quick Start

```bash
# Clone repository
git clone <repo-url>
cd project_name

# Install dependencies
pip install -r requirements.txt

# Run analysis
jupyter notebook notebooks/01_data_exploration.ipynb
```

## Project Structure

```
project_name/
├── README.md
├── requirements.txt
├── notebooks/
├── src/
├── data/
└── reports/
```

## Methodology

### Data
- Source: [description]
- Size: X records, Y features
- Target: [description]

### Approach
1. Step 1: Data exploration and cleaning
2. Step 2: Feature engineering
3. Step 3: Model selection and training
4. Step 4: Evaluation and optimization

### Models Compared
| Model | Metric | Training Time |
|-------|--------|---------------|
| Model A | 0.75 | 10s |
| Model B | 0.78 | 45s |

## Results & Visualizations

### Key Visualization 1
[Description of what the chart shows]

### Key Visualization 2
[Description of what the chart shows]

## Future Improvements

- [ ] Improvement 1
- [ ] Improvement 2

## Author

**Arina Fedorova** - Data Scientist
[GitHub](link) | [LinkedIn](link)

---

*Educational project completed during Yandex Practicum Data Science program*
```

---

## Project-Specific Plans

### Project 22: Time Series Prediction

| # | Task | Priority | Description |
|---|------|----------|-------------|
| 1 | Select final notebook | HIGH | Keep TaxiForecast_Fixed_Final.ipynb, rename to main |
| 2 | Remove redundant files | HIGH | Delete 4 extra notebooks |
| 3 | Create README.md (EN) | HIGH | Include RMSE, ADF test, patterns found |
| 4 | Add requirements.txt | HIGH | pandas, numpy, statsmodels, sklearn, matplotlib |
| 5 | Reorganize structure | MEDIUM | Create notebooks/, src/, data/ folders |
| 6 | Extract functions to src/ | LOW | time_series_utils.py with reusable code |

**Estimated effort:** 2-3 hours

---

### Project 18: Customer Behavior Analysis

| # | Task | Priority | Description |
|---|------|----------|-------------|
| 1 | Translate README to EN | HIGH | Preserve structure, improve formatting |
| 2 | Add Quick Results section | HIGH | Key metrics, business findings |
| 3 | Add requirements.txt | HIGH | pandas, sklearn, shap, matplotlib, seaborn |
| 4 | Create folder structure | MEDIUM | notebooks/, data/README.md |
| 5 | Export key visualizations | LOW | Save to reports/figures/ |

**Estimated effort:** 1-2 hours

---

### Project 19: Cow Selection ML

| # | Task | Priority | Description |
|---|------|----------|-------------|
| 1 | Translate README to EN | HIGH | Data dictionary translation important |
| 2 | Add Quick Results section | HIGH | Regression and classification metrics |
| 3 | Add requirements.txt | HIGH | pandas, sklearn, matplotlib |
| 4 | Consider renaming project | MEDIUM | "Baseline Establishment ML" more relevant for H1OX |
| 5 | Create folder structure | MEDIUM | notebooks/, data/README.md |

**Estimated effort:** 1-2 hours

---

### Project 24: Toxic Comments Processing

| # | Task | Priority | Description |
|---|------|----------|-------------|
| 1 | Create README.md (EN) | HIGH | Based on project.md + actual results |
| 2 | Add Quick Results section | HIGH | F1: 0.778, Accuracy: 95.6% |
| 3 | Add requirements.txt | HIGH | pandas, nltk, sklearn, (transformers if BERT used) |
| 4 | Document preprocessing pipeline | MEDIUM | NLP steps are important to showcase |
| 5 | Create folder structure | MEDIUM | notebooks/, src/preprocessing.py |

**Estimated effort:** 2-3 hours

---

### Project 29: Machine Vision

| # | Task | Priority | Description |
|---|------|----------|-------------|
| 1 | Create README.md (EN) | HIGH | Explain multimodal approach |
| 2 | Document models | HIGH | What each .pkl file does, metrics |
| 3 | Create requirements.txt | HIGH | Extract from env/ |
| 4 | Add .gitignore | HIGH | Exclude large models, env/, .npy files |
| 5 | Reorganize structure | MEDIUM | models/, notebooks/, data/ |
| 6 | Select final notebook | MEDIUM | Keep one, remove duplicate |
| 7 | Add model card | LOW | BERT, ResNet50 usage documentation |

**Estimated effort:** 3-4 hours

---

## Prioritization

### Phase 1: Critical Projects (Highest H1OX Relevance)

**Priority:** Time Series + NLP (core H1OX requirements)

1. **22_time_series_prediction**
   - Most relevant for wearable device metrics
   - Currently in worst state (needs most work)
   - High impact on CV credibility

2. **24_toxic_comments_processing**
   - Demonstrates NLP/LLM capability
   - Has concrete metrics to showcase
   - Missing basic documentation

### Phase 2: Well-Documented Projects (Translation + Enhancement)

**Priority:** Already good, need English translation

3. **18_customer_behavior_analysis**
   - Good README exists (Russian)
   - SHAP interpretability showcase
   - Quick win with translation

4. **19_cow_selection_ml**
   - Good README exists (Russian)
   - Baseline establishment methodology
   - Consider renaming for relevance

### Phase 3: Advanced Project (Most Complex)

**Priority:** Shows advanced skills but requires most work

5. **29_machine_vision**
   - Multimodal learning (ResNet50 + BERT)
   - Most artifacts to document
   - Large file management needed

---

## Work Format Options

### Option A: Sequential (Project by Project)

```
Project 22 → Project 24 → Project 18 → Project 19 → Project 29
```

**Pros:**
- Complete focus on one project
- Easier quality control
- Clear progress milestones

**Cons:**
- Slower visible progress
- Learnings not applied immediately to other projects

---

### Option B: Parallel (Task by Task)

```
All READMEs → All requirements.txt → All folder structures → ...
```

**Pros:**
- Faster visible progress
- Consistent approach across projects
- Batch similar tasks

**Cons:**
- Context switching
- Harder to track per-project progress

---

### Option C: Template First

```
Create ideal template on Project 22 → Apply to all others
```

**Pros:**
- Establish gold standard first
- Learn from one project
- Consistent quality

**Cons:**
- Delayed start on other projects
- May need template adjustments

---

## Open Questions

### To Be Decided Before Starting

1. **Work format preference?** (A / B / C)

2. **README language?**
   - English only
   - Bilingual (EN primary, RU secondary)

3. **Code extraction to src/?**
   - Full extraction (production-style)
   - Keep everything in notebooks (simpler)
   - Hybrid (extract only reusable functions)

4. **Large files handling?**
   - Delete from git history (clean but complex)
   - Add to .gitignore for future commits only
   - Use Git LFS

5. **Project renaming?**
   - Keep original names (22_time_series_prediction)
   - Rename for clarity (taxi_demand_forecasting)
   - Add H1OX-relevant subtitles

---

## Next Steps

1. [ ] Review this plan
2. [ ] Answer open questions
3. [ ] Decide on work format
4. [ ] Begin implementation (no commits until reviewed)

---

*Document created as context storage for portfolio improvement project.*
