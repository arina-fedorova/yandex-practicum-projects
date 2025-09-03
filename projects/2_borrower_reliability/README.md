# Borrower Reliability Research: Credit Risk Analysis

## Project Overview

This project analyzes credit risk factors using a comprehensive dataset of 21,525 borrower records, applying statistical hypothesis testing to understand the relationship between demographic characteristics and credit repayment behavior. The analysis reveals complex patterns that challenge traditional credit scoring assumptions and provide actionable intelligence for financial institutions.

## Business Objectives

**Primary Goal**: Identify statistically validated credit risk patterns to optimize lending decisions and minimize default risk.

**Key Research Questions**:
1. Does the number of children in a family influence credit repayment reliability?
2. How does marital status affect credit risk and repayment behavior?
3. What is the relationship between income level and credit reliability?
4. How do different credit purposes impact repayment success rates?

## Key Findings

### Family Size Impact
- **Peak Risk**: Families with 1-2 children show highest risk (9.5-9.7%)
- **Moderate Risk**: Families with 0 children show moderate risk (7.5%)
- **Lower Risk**: Families with 3 children show moderate risk (7.5%)
- **Non-linear Pattern**: Transition to parenthood creates maximum financial strain

### Marital Status Patterns
- **Highest Risk**: Single individuals (10%) and civil partnerships (9%)
- **Lowest Risk**: Widowed individuals (6.5%) and divorced individuals (7%)
- **Moderate Risk**: Married individuals (7.7%)
- **Financial Stability**: Marital status correlates with financial support systems

### Income Level Relationships
- **Highest Risk**: Income category E (8.5%) and category C (8.2%)
- **Lowest Risk**: Income category D (6%) and category B (7%)
- **Moderate Risk**: Income category A (8%)
- **Non-linear Pattern**: Income level alone insufficient to predict credit risk

### Credit Purpose Influence
- **Highest Risk**: Automotive and education loans (8.8%)
- **Lowest Risk**: Real estate and wedding loans (7.5%)
- **Investment Uncertainty**: Educational loans create immediate pressure without guaranteed returns

## Project Structure

```
2_borrower_reliability/
├── README.md
├── borrower_reliability.ipynb
└── reports/
    ├── credit_risk_analysis.md
    └── images/
```

## Data Description

### Dataset: credit_data.csv
- **Size**: 2.1MB
- **Records**: 21,525 borrower profiles
- **Features**: 12 columns
- **Time Period**: Historical credit data

### Data Schema
| Column | Type | Description | Quality |
|--------|------|-------------|---------|
| `children` | int64 | Number of children in family | Complete |
| `days_employed` | float64 | Employment duration in days | 2,174 missing |
| `dob_years` | int64 | Age in years | Complete |
| `education` | object | Education level | Complete |
| `family_status` | object | Marital status | Complete |
| `gender` | object | Gender (M/F) | Complete |
| `income_type` | object | Type of income source | Complete |
| `debt` | int64 | Credit repayment status (0=no debt, 1=has debt) | Complete |
| `total_income` | float64 | Total income amount | 2,174 missing |
| `purpose` | object | Credit purpose | Complete |

### Data Quality Issues Identified
- **Missing Values**: 10.1% missing data in employment/income fields
- **Anomalous Data**: Removed biologically impossible values (-1 and 20 children)
- **Data Completeness**: 100% after cleaning and preprocessing
- **Sample Representativeness**: Flagged categories with insufficient sample sizes

## Methodology

### 1. Data Exploration and Quality Assessment
- Comprehensive data profiling and quality metrics
- Missing value analysis and impact assessment
- Anomalous value detection and removal
- Data type optimization and validation

### 2. Exploratory Data Analysis (EDA)
- Risk pattern analysis by demographic factors
- Borrower profile mapping and visualization
- Statistical significance testing for hypotheses
- Business intelligence translation of findings

### 3. Hypothesis Testing
- **Hypothesis 1**: Family size significantly influences credit risk
- **Hypothesis 2**: Marital status significantly influences credit risk
- **Hypothesis 3**: Income level significantly influences credit risk
- **Hypothesis 4**: Credit purpose significantly influences credit risk

### 4. Advanced Analytics
- Statistical significance testing (chi-square tests)
- Risk stratification and borrower profile identification
- Business intelligence translation of statistical findings
- Actionable recommendations for risk management

## Technologies and Tools

### Core Libraries
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Static visualizations
- **Plotly**: Interactive visualizations
- **SciPy**: Statistical testing

### Data Science Practices
- **Data Validation**: Comprehensive quality checks
- **Statistical Testing**: Hypothesis validation
- **Visualization**: Professional charting and storytelling
- **Documentation**: Clear methodology and results

## Results and Insights

### Hypothesis 1: Confirmed
- **Statistical Significance**: p = 0.000466
- **Family Size Impact**: Non-linear relationship with peak risk at 1-2 children
- **Business Impact**: Transition to parenthood creates maximum financial strain

### Hypothesis 2: Confirmed
- **Statistical Significance**: p = 0.000037
- **Marital Status Patterns**: Single individuals face highest risk, widowed individuals lowest
- **Business Impact**: Marital status correlates with financial stability

### Hypothesis 3: Confirmed
- **Statistical Significance**: p = 0.010774
- **Income Level Relationships**: Non-linear pattern defies traditional assumptions
- **Business Impact**: Income level alone insufficient to predict credit risk

### Hypothesis 4: Confirmed
- **Statistical Significance**: p = 0.000031
- **Credit Purpose Influence**: Automotive and education loans show highest risk
- **Business Impact**: Loan purpose reveals clear risk stratification

## Business Recommendations

### Risk Management Strategy
1. **High-Risk Segments**: Implement stricter lending criteria for single individuals, families with 1-2 children, and automotive/education loan applicants
2. **Low-Risk Segments**: Offer preferential terms for widowed individuals, middle-income category D, and real estate/wedding loan applicants
3. **Risk-Based Pricing**: Implement 2-3% interest rate differentials between risk categories

### Product Development
1. **Specialized Products**: Family transition loans, widow/widower programs, real estate advantage loans
2. **Enhanced Documentation**: Additional verification for high-risk segments, streamlined processes for low-risk segments
3. **Behavioral Scoring**: Develop models capturing financial discipline patterns beyond demographic factors

### Data Quality Improvements
1. **Sample Size Validation**: Flag categories with insufficient sample sizes for reliable analysis
2. **Risk Factor Integration**: Incorporate life stage transitions into risk assessment models
3. **Behavioral Scoring**: Develop models that capture financial discipline patterns

## Future Work

### Advanced Analytics
- **Machine Learning**: Predictive risk models incorporating identified risk factors
- **Behavioral Scoring**: Models capturing financial discipline patterns
- **Real-time Risk Assessment**: Dynamic risk scoring systems

### Data Enhancement
- **Life Stage Analysis**: Investigate how life transitions affect credit risk over time
- **Economic Factor Integration**: Incorporate macroeconomic indicators into risk models
- **Geographic Risk Analysis**: Explore regional variations in credit risk factors

### Business Applications
- **Dynamic Pricing**: Risk-based interest rate structures
- **Product Strategy**: Specialized products for different risk segments
- **Partnership Opportunities**: Collaboration with financial planning services

## References and Sources

- **Data Source**: Credit database
- **Statistical Methods**: Hypothesis testing, chi-square contingency analysis
- **Credit Risk Research**: Demographic factors in credit assessment
- **Financial Services**: Risk-based lending practices

## Author and Contact

**Data Scientist**: Arina Fedorova  
**Project Date**: 2024  
**Repository**: Yandex Practicum Projects  
**Contact**: afedorova.dev@gmail.com

---

## Project Impact

This analysis demonstrates:
- **Data Science Skills**: Statistical testing, data quality assessment, risk analysis
- **Business Understanding**: Actionable insights and recommendations for financial institutions
- **Technical Proficiency**: Modern Python practices and professional visualization
- **Professional Communication**: Clear methodology and results presentation

**Project Status**: Completed - Shows end-to-end data science project with business impact
