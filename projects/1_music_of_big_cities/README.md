# Music of Big Cities: Moscow vs. Saint Petersburg Analysis

## Project Overview

This project analyzes user behavior patterns on Yandex Music platform across Russia's two largest cities - Moscow and Saint Petersburg. The analysis explores how cultural differences, urban lifestyles, and weekly rhythms influence musical preferences and listening habits.

## Business Objectives

**Primary Goal**: Understand user behavior patterns to optimize music recommendations and marketing strategies for different urban markets.

**Key Research Questions**:
1. How does day-of-week affect user activity patterns in different cities?
2. Do musical preferences vary by time of day and city?
3. What are the distinct genre preferences that differentiate Moscow and Saint Petersburg users?

## Key Findings

### Activity Patterns
- **Moscow**: Peak activity on Mondays (15,740 tracks) and Fridays (15,945 tracks)
- **Saint Petersburg**: More consistent activity throughout the week, with Wednesday peak (7,003 tracks)
- **Urban Rhythm Impact**: Moscow shows stronger workweek patterns, while Saint Petersburg maintains more balanced activity

### Genre Preferences
- **Pop dominates** both cities with 13.6% of total streaming activity
- **Dance and Rock** follow as second and third most popular genres
- **Cultural Distinction**: Saint Petersburg shows slightly higher classical and alternative preferences
- **Local Music**: Russian pop and rap maintain cultural relevance in both cities

### Temporal Patterns
- **Friday leads** with 35.7% of weekly activity
- **Monday follows** with 34.9% of weekly activity
- **Wednesday lags** with 29.5% of weekly activity
- **Consistent preferences**: Genre choices remain stable across different days

## Project Structure

```
1_music_of_big_cities/
├── README.md
├── music_of_big_cities.ipynb
└── reports/
    ├── music_of_big_cities.md
    └── images/
```

## Data Description

### Dataset: yandex_music_project.csv
- **Size**: 4.8MB
- **Records**: 65,079 user interactions
- **Features**: 7 columns
- **Time Period**: Historical data (Monday, Wednesday, Friday only)

### Data Schema
| Column | Type | Description | Quality |
|--------|------|-------------|---------|
| `userID` | object | Unique user identifier | Complete |
| `Track` | object | Song title | 1,231 missing |
| `artist` | object | Artist name | 7,203 missing |
| `genre` | object | Music genre | 1,198 missing |
| `City` | object | User city (Moscow/SPb) | Complete |
| `time` | object | Listening timestamp | Complete |
| `Day` | object | Day of week | Complete |

### Data Quality Issues Identified
- **Missing Values**: 1.2-11.1% missing data in key columns
- **Duplicates**: 3,826 duplicate records removed
- **Genre Standardization**: Hip-hop variants consolidated
- **Time Coverage**: Limited to three specific weekdays

## Methodology

### 1. Data Exploration and Quality Assessment
- Comprehensive data profiling and quality metrics
- Missing value analysis and impact assessment
- Duplicate detection and removal
- Data type optimization and validation

### 2. Exploratory Data Analysis (EDA)
- Temporal pattern analysis by city and day
- Genre preference mapping and visualization
- User behavior clustering and segmentation
- Statistical significance testing for hypotheses

### 3. Hypothesis Testing
- **Hypothesis 1**: Day-of-week activity patterns differ by city
- **Hypothesis 2**: Genre preferences vary by time and city
- **Hypothesis 3**: Distinct genre preferences between cities

### 4. Advanced Analytics
- Statistical significance testing (chi-square tests)
- Correlation analysis between variables
- Time series analysis of listening patterns
- User segmentation based on behavior patterns

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
- **Statistical Significance**: p < 0.001
- **Moscow**: Strong Monday-Friday pattern (workweek rhythm)
- **Saint Petersburg**: More balanced weekly distribution
- **Business Impact**: Different marketing strategies needed for each city

### Hypothesis 2: Partially confirmed
- **Time-based Variation**: Minimal differences by day of week
- **City-based Variation**: More pronounced in morning hours
- **Data Quality Impact**: Missing genre data may affect results

### Hypothesis 3: Confirmed
- **Genre Similarity**: More common preferences than differences
- **Cultural Convergence**: Urban centers show similar mainstream tastes
- **Niche Markets**: Differences exist in classical/alternative genres

## Business Recommendations

### Marketing Strategy
1. **Moscow**: Focus on Monday and Friday campaigns, emphasize workweek rhythm
2. **Saint Petersburg**: Consistent messaging throughout week, highlight cultural diversity
3. **Genre Targeting**: Pop music for Moscow, classical/alternative for Saint Petersburg

### Product Development
1. **Recommendation Engine**: City-specific algorithms based on temporal patterns
2. **Content Curation**: Localized playlists reflecting urban cultural differences
3. **Feature Timing**: Release new features aligned with city-specific activity peaks

### Data Quality Improvements
1. **Genre Classification**: Reduce missing genre data through better tagging
2. **User Segmentation**: Implement behavior-based user clustering
3. **Real-time Analytics**: Monitor temporal patterns for dynamic optimization

## Future Work

### Advanced Analytics
- **Machine Learning**: User behavior prediction models
- **Time Series Forecasting**: Activity pattern prediction
- **A/B Testing**: Validate recommendation improvements

### Data Enhancement
- **User Demographics**: Age, gender, occupation data
- **Listening Context**: Device, location, social sharing
- **External Data**: Weather, events, cultural factors

### Business Applications
- **Dynamic Pricing**: Peak-time premium features
- **Content Strategy**: City-specific content creation
- **Partnership Opportunities**: Local artist and venue collaborations

## References and Sources

- **Data Source**: Yandex Music platform
- **Statistical Methods**: Hypothesis testing, correlation analysis
- **Urban Studies**: Cultural differences in Russian cities
- **Music Industry Research**: Regional preference patterns

## Author and Contact

**Data Scientist**: Arina Fedorova  
**Project Date**: 2024  
**Repository**: Yandex Practicum Projects  
**Contact**: [Professional Profile]

---

## Project Impact

This analysis demonstrates:
- **Data Science Skills**: Statistical testing, data quality assessment
- **Business Understanding**: Actionable insights and recommendations
- **Technical Proficiency**: Modern Python practices and visualization
- **Professional Communication**: Clear methodology and results presentation

**Project Status**: Completed - Shows end-to-end data science project with business impact
