# Borrower Reliability Research: Credit Risk Analysis
## Business Intelligence Report

**Author:** Arina Fedorova  
**Data Source:** Credit Database  
**Analysis Period:** Historical Data  

---

## Executive Summary

This analysis examines credit risk factors using a dataset of 21,525 borrower records, applying statistical hypothesis testing to understand the relationship between demographic characteristics and credit repayment behavior. The study reveals complex patterns that challenge traditional credit scoring assumptions and provide actionable intelligence for financial institutions.

### Key Findings
- **Family Size Impact**: Non-linear relationship with peak risk at 1-2 children (9.5-9.7%), suggesting transition to parenthood creates maximum financial strain
- **Marital Status Patterns**: Single individuals face highest risk (10%), while widowed individuals show lowest risk (6.5%)
- **Income Level Relationships**: Non-linear pattern where middle-income category D shows lowest risk (6%), defying traditional income-based assumptions
- **Credit Purpose Influence**: Automotive and education loans carry highest risk (8.8%), while real estate and wedding loans show lower risk (7.5%)

### Business Implications
- **High-Risk Segments**: Single individuals, families with 1-2 children, lowest income category E, automotive/education loan applicants
- **Low-Risk Segments**: Widowed individuals, middle-income category D, real estate/wedding loan applicants
- **Risk-Based Pricing**: Implement 2-3% interest rate differentials between risk categories

---

## Introduction

### Project Overview
In the complex landscape of credit risk assessment, understanding the factors that influence borrower reliability is crucial for financial institutions. This analysis examines how demographic characteristics, family circumstances, and financial profiles correlate with credit repayment behavior.

The data comes from a comprehensive credit database containing information about borrowers' personal characteristics, financial situations, and credit history. What emerges is not just a collection of statistics, but a portrait of credit risk written in the language of human behavior and financial patterns.

### Research Questions
Four key questions guide this investigation:
1. Does the number of children in a family influence credit repayment reliability?
2. How does marital status affect credit risk and repayment behavior?
3. What is the relationship between income level and credit reliability?
4. How do different credit purposes impact repayment success rates?

### Methodology
The analysis employs comprehensive data quality assessment, exploratory data analysis, and statistical hypothesis testing using chi-square tests. The dataset contains 21,525 records of borrower information, processed to 19,240 clean records for analysis.

---

## Data Overview

### Dataset Characteristics
- **Total Records**: 21,525 original, 19,240 after cleaning
- **Borrower Profiles**: Complete demographic and financial information
- **Risk Categories**: Family size, marital status, income levels, credit purposes
- **Data Quality**: 10.1% missing values in critical employment/income fields
- **Sample Representativeness**: Flagged categories with insufficient sample sizes

### Data Quality Assessment
- **Missing Values**: Employment days (10.1%), Total income (10.1%)
- **Anomalous Data**: Removed biologically impossible values (-1 and 20 children)
- **Data Completeness**: 100% after cleaning and preprocessing
- **Statistical Validation**: All four hypotheses confirmed with p < 0.05

---

## Key Findings

### 1. Family Size and Credit Risk

#### Risk Distribution by Children Count

![Credit Risk by Family Size](images\credit-risk-analysis-family-size.png)
*Figure 1: Credit risk patterns by family size showing non-linear relationship with peak risk at 1-2 children*

The data reveals a complex relationship between family size and credit risk:

- **Peak Risk**: Families with 1-2 children show highest risk (9.5-9.7%)
- **Moderate Risk**: Families with 0 children show moderate risk (7.5%)
- **Lower Risk**: Families with 3 children show moderate risk (7.5%)
- **Data Limitations**: 5+ children families show 0% risk but sample size too small (8 records)

This non-linear pattern suggests that the transition to parenthood creates maximum financial strain, with risk peaking at 1-2 children before stabilizing. The pattern reflects the economic reality of childcare costs, reduced work flexibility, and increased living expenses that accompany family expansion.

### 2. Marital Status and Credit Risk

#### Risk Distribution by Marital Status

![Credit Risk by Marital Status](images\credit-risk-analysis-marital-status.png)
*Figure 2: Credit risk patterns by marital status showing single individuals at highest risk*

Marital status reveals striking differences in credit risk profiles:

- **Highest Risk**: Single individuals (10%) and civil partnerships (9%)
- **Lowest Risk**: Widowed individuals (6.5%) and divorced individuals (7%)
- **Moderate Risk**: Married individuals (7.7%)

Single individuals face the highest risk, suggesting that the absence of shared financial responsibilities and dual income streams creates vulnerability. Civil partnerships show similarly high risk, indicating that informal arrangements may not provide the same financial stability as formal marriage. Widowed individuals show the lowest risk, possibly due to insurance settlements, inheritance, or more conservative financial behavior.

### 3. Income Level and Credit Risk

#### Risk Distribution by Income Category

![Credit Risk by Income Level](images\credit-risk-analysis-income-level.png)
*Figure 3: Credit risk patterns by income level showing non-linear relationship*

The income-risk relationship defies conventional wisdom:

- **Highest Risk**: Income category E (8.5%) and category C (8.2%)
- **Lowest Risk**: Income category D (6%) and category B (7%)
- **Moderate Risk**: Income category A (8%)

This non-linear pattern suggests that income level alone is insufficient to predict credit risk. Higher-income individuals may take larger loans or engage in riskier financial behaviors, while some middle-income groups may demonstrate more conservative financial management. The relationship appears driven by spending patterns and financial discipline rather than pure income levels.

### 4. Credit Purpose and Risk

#### Risk Distribution by Loan Purpose

![Credit Risk by Purpose](images\credit-risk-analysis-purpose.png)
*Figure 4: Credit risk patterns by loan purpose showing automotive and education loans at highest risk*

Loan purpose reveals clear risk stratification:

- **Highest Risk**: Automotive and education loans (8.8%)
- **Lowest Risk**: Real estate and wedding loans (7.5%)

Automotive and educational loans carry the highest risk, suggesting that these purposes may indicate financial strain or represent investments with uncertain returns. Educational loans, while potentially beneficial long-term, create immediate financial pressure without guaranteed income increases. Real estate and wedding loans show lower risk, possibly because these purposes often involve more careful planning, longer-term thinking, and family support systems.

### 5. Statistical Validation

#### Hypothesis Testing Results

**Hypothesis 1: Family size significantly influences credit risk**
- **Rationale**: Family size impacts financial stability and credit repayment capacity
- **Null Hypothesis**: There is no significant relationship between children count and credit risk
- **Result**: Confirmed (p = 0.000466) - significant relationship between family size and credit risk
- **Analysis**: Non-linear pattern suggests transition to parenthood creates maximum financial strain

**Hypothesis 2: Marital status significantly influences credit risk**
- **Rationale**: Marital status correlates with financial stability and risk tolerance
- **Null Hypothesis**: There is no significant relationship between marital status and credit risk
- **Result**: Confirmed (p = 0.000037) - strong relationship between marital status and credit risk
- **Analysis**: Single individuals face highest risk, widowed individuals lowest risk

**Hypothesis 3: Income level significantly influences credit risk**
- **Rationale**: Income level is fundamental to credit risk assessment
- **Null Hypothesis**: There is no significant relationship between income level and credit risk
- **Result**: Confirmed (p = 0.010774) - significant relationship between income categories and credit risk
- **Analysis**: Non-linear pattern defies traditional income-based assumptions

**Hypothesis 4: Credit purpose significantly influences credit risk**
- **Rationale**: Different credit purposes carry different risk profiles
- **Null Hypothesis**: There is no significant relationship between credit purpose and credit risk
- **Result**: Confirmed (p = 0.000031) - strong relationship between loan purpose and credit risk
- **Analysis**: Automotive and education loans show highest risk, real estate and wedding loans lowest

---

## Business Insights and Recommendations

### Risk Management Strategy

#### High-Risk Segment Management
**Single Individuals**: Implement stricter lending criteria, require additional documentation, and consider higher interest rates for this 10% risk segment.

**Families with 1-2 Children**: Apply enhanced verification processes and consider shorter loan terms for families in the peak risk period of child-rearing.

**Automotive/Education Loans**: Implement stricter collateral requirements and consider specialized risk assessment models for these high-risk purposes.

#### Low-Risk Segment Optimization
**Widowed Individuals**: Offer preferential terms and streamlined approval processes for this 6.5% risk segment to capture market share.

**Middle-Income Category D**: Develop targeted products and competitive rates for this financially disciplined segment.

**Real Estate/Wedding Loans**: Leverage lower risk profiles to offer competitive terms and expand market presence.

### Product Development

#### Risk-Based Pricing Models
Implement tiered interest rate structures with 2-3% differentials between risk categories:
- **High-Risk Segments**: Standard rates + 2-3%
- **Low-Risk Segments**: Standard rates - 1-2%
- **Moderate-Risk Segments**: Standard rates

#### Specialized Products
- **Family Transition Loans**: Specialized products for families with young children
- **Widow/Widower Programs**: Preferential terms for low-risk widowed individuals
- **Real Estate Advantage**: Competitive rates for lower-risk real estate loans

#### Enhanced Documentation Requirements
- **High-Risk Segments**: Additional income verification, employment history, and financial planning documentation
- **Low-Risk Segments**: Streamlined approval processes with reduced documentation requirements

### Data Quality Improvements

#### Sample Size Validation
Flag categories with insufficient sample sizes for reliable analysis:
- **5+ Children Families**: Only 8 records - insufficient for statistical analysis
- **Income Category A**: Only 25 records - requires additional data collection

#### Risk Factor Integration
Incorporate life stage transitions into risk assessment models:
- **Family Planning Indicators**: Consider family size trends and life stage transitions
- **Marital Status Changes**: Monitor changes in marital status as risk indicators
- **Income Stability**: Track income stability patterns beyond simple income levels

#### Behavioral Scoring
Develop models that capture financial discipline patterns:
- **Spending Pattern Analysis**: Incorporate spending behavior data
- **Financial Planning Indicators**: Assess long-term financial planning behavior
- **Risk Tolerance Assessment**: Evaluate individual risk tolerance levels

---

## Advanced Analytics Opportunities

### Machine Learning Implementation
- **Predictive Risk Models**: Develop ML models incorporating identified risk factors and behavioral patterns
- **Behavioral Scoring**: Create models that capture financial discipline patterns beyond demographic factors
- **Real-time Risk Assessment**: Implement dynamic risk scoring systems that adapt to changing borrower circumstances

### Future Research
- **Life Stage Analysis**: Investigate how life transitions affect credit risk over time
- **Economic Factor Integration**: Incorporate macroeconomic indicators into risk models
- **Geographic Risk Analysis**: Explore regional variations in credit risk factors

---

## Technical Achievements

### Data Processing
- Comprehensive data quality assessment and preprocessing
- Anomalous value detection and removal
- Data categorization and standardization
- Statistical validation through hypothesis testing

### Analytical Methods
- Exploratory data analysis with comprehensive examination of data quality
- Statistical hypothesis testing using chi-square contingency analysis
- Risk stratification and borrower profile identification
- Business intelligence translation of statistical findings

### Visualization Portfolio
- Risk dashboard with four-panel visualization
- Statistical validation presentation
- Business intelligence charts
- Comprehensive risk analysis visualization

---

## Conclusion

The analysis successfully identifies statistically validated credit risk patterns that provide a clear framework for risk-based lending decisions. The findings challenge traditional credit scoring models and offer actionable intelligence for financial institutions to optimize their lending portfolios while minimizing default risk.

### Key Takeaways
1. **Non-Linear Risk Patterns**: Credit risk follows complex patterns that defy simple demographic assumptions
2. **Life Stage Impact**: Family transitions and life circumstances significantly influence credit risk
3. **Behavioral Factors**: Financial discipline and planning behavior matter more than income alone
4. **Business Value**: The insights provide actionable strategies for risk management, product development, and pricing

### Project Status
**Successfully Completed**  
- Data Quality: 19,240 clean records analyzed after removing missing values and anomalous data
- Statistical Significance: All four hypotheses confirmed with p < 0.05
- Business Value: Clear risk stratification framework with specific recommendations
- Technical Quality: Professional documentation and comprehensive analysis

---

## Appendices

### Appendix A: Data Dictionary
- **children**: Number of children in family
- **days_employed**: Employment duration in days
- **dob_years**: Age in years
- **education**: Education level
- **family_status**: Marital status
- **gender**: Gender (M/F)
- **income_type**: Type of income source
- **debt**: Credit repayment status (0=no debt, 1=has debt)
- **total_income**: Total income amount
- **purpose**: Credit purpose

### Appendix B: Statistical Test Details
- **Chi-square tests**: Used for categorical variable relationships
- **Significance level**: α = 0.05
- **Degrees of freedom**: Calculated based on contingency table dimensions
- **Sample sizes**: Validated for statistical reliability

### Appendix C: Data Quality Metrics
- **Completeness**: 100% after cleaning and preprocessing
- **Accuracy**: Anomalous values identified and removed
- **Consistency**: Data format standardized across all variables
- **Representativeness**: Sample sizes validated for statistical analysis

---

**Report End**

*This report was generated from comprehensive analysis of credit database records, providing business intelligence for strategic decision-making in credit risk management and financial services.*
