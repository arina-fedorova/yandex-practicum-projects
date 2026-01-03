# Yandex Practicum Data Science Projects

A collection of data science projects completed during the Yandex Practicum Data Science program. Projects cover the full ML lifecycle: data exploration, preprocessing, modeling, and evaluation.

## Featured Portfolio Projects

| Project | Description | Key Skills | Results |
|---------|-------------|------------|---------|
| [Time Series Prediction](./projects/22_time_series_prediction) | Taxi demand forecasting | Time series, statsmodels, feature engineering | RMSE below target |
| [Customer Behavior Analysis](./projects/18_customer_behavior_analysis) | Predicting customer activity decline | Classification, SHAP, segmentation | Actionable recommendations |
| [Cow Selection ML](./projects/19_cow_selection_ml) | Baseline establishment for livestock | Regression + Classification, multi-objective | Dual-model system |
| [Toxic Comments Processing](./projects/24_toxic_comments_processing) | NLP text classification | TF-IDF, NLP preprocessing, threshold optimization | F1: 0.778 |
| [Multimodal Image-Text Matching](./projects/multimodal_image_text_matching) | Age prediction using images + text | ResNet50, BERT, ensemble methods | MAE: 5.4 |

## All Projects Index

| # | Project Name | Description | Status | Technologies |
|---|--------------|-------------|---------|--------------|
| -- | [Project Template](./projects/project_template) | Template for new projects | 🟡 Template | Python, Jupyter |
| 01 | [Music Preference Analysis](./projects/music_preference_analysis) | Yandex Music behavior patterns | ✅ Completed | Python, Pandas, SciPy |
| 02 | [Credit Risk Analysis](./projects/credit_risk_analysis) | Credit risk pattern identification | ✅ Completed | Python, SciPy, Pandas |
| 06 | [ML Farm](./projects/6_ml_farm) | Cow farm ML modeling | ✅ Completed | Python, ML, Scikit-learn |
| 08 | [ML HR](./projects/8_ml_hr) | HR ML modeling | ✅ Completed | Python, ML, HR Analytics |
| 09 | [Geo Bootstrap](./projects/9_geo_bootstrap) | Geographic bootstrap analysis | ✅ Completed | Python, Statistics, Bootstrap |
| 10 | [ML OneClick](./projects/10_ml_oneclick) | One-click ML solution | ✅ Completed | Python, ML, Automation |
| 11 | [Side Project: Accord](./projects/11_sideproject_accord) | Accord side project | ✅ Completed | Python, Side Project |
| 12 | [Side Project: ExpressTrip](./projects/12_sideproject_expresstrip) | Express trip analysis | ✅ Completed | Python, Travel Analytics |
| 13 | [Side Project: SeaTreats](./projects/13_sideproject_seatreats) | Sea treats analysis | ✅ Completed | Python, Food Analytics |
| 14 | [Marketing Analysis](./projects/14_marketing_analysis) | Marketing campaign analysis | ✅ Completed | Python, Marketing Analytics |
| 15 | [Russian Cinema Analysis](./projects/15_russian_cinema_analysis) | Russian cinema data research | ✅ Completed | Python, Cinema Analytics |
| 16 | [Startup Success Prediction](./projects/16_startup_success_prediction) | Startup success ML model | ✅ Completed | Python, ML, Business Analytics |
| 17 | [Housing Price Prediction](./projects/17_housing_price_prediction) | Housing price ML model | ✅ Completed | Python, ML, Real Estate |
| 18 | [Customer Behavior Analysis](./projects/18_customer_behavior_analysis) | Customer behavior strategy | ✅ Completed | Python, Customer Analytics |
| 19 | [Cow Selection ML](./projects/19_cow_selection_ml) | Cow selection ML modeling | ✅ Completed | Python, ML, Agriculture |
| 20 | [Car Price Determination](./projects/20_car_price_determination) | Car price ML model | ✅ Completed | Python, ML, Automotive |
| 21 | [Star Temperature Prediction](./projects/21_star_temperature_prediction) | Star temperature ML model | ✅ Completed | Python, ML, Astronomy |
| 22 | [Time Series Prediction](./projects/22_time_series_prediction) | Time series forecasting | ✅ Completed | Python, ML, Time Series |
| 23 | [Text Processing](./projects/23_text_processing) | Text analysis and processing | ✅ Completed | Python, NLP, Text Analytics |
| 24 | [Toxic Comments Processing](./projects/24_toxic_comments_processing) | Toxic comments ML model | ✅ Completed | Python, ML, NLP, Moderation |
| 25 | [Scooter Rental Analysis](./projects/25_scooter_rental_analysis) | Scooter rental statistics | ✅ Completed | Python, Statistics, Transportation |
| 29 | [Multimodal Image-Text Matching](./projects/multimodal_image_text_matching) | Image + text age prediction | ✅ Completed | Python, BERT, ResNet50, XGBoost |

## Repository Structure

```
yandex-practicum-projects/
├── README.md                    # This file - Project overview
├── projects/                    # Individual project directories
│   ├── project_template/                  # Project template
│   ├── music_preference_analysis/         # EDA, Statistical Testing
│   ├── credit_risk_analysis/              # Statistical Testing, Risk Modeling
│   ├── multimodal_image_text_matching/    # Computer Vision, BERT, Ensemble
│   └── ...                                # Other projects
├── docs/                        # Documentation and planning
│   └── PROJECT_IMPROVEMENT_PLAN.md
├── common/                      # Shared utilities and templates
│   ├── utils/                  # Common utility functions
│   └── templates/              # Project templates
├── .github/workflows/          # CI/CD workflows
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
├── Makefile                    # Build automation
└── .gitignore                  # Git ignore rules
```

## Quick Start

### Prerequisites
- Python 3.11+
- Git
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/yandex-practicum-projects.git
   cd yandex-practicum-projects
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

5. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

### Using the Makefile

The repository includes a `Makefile` with common commands:

```bash
# View all available commands
make help

# Install dependencies
make install

# Install development dependencies
make install-dev

# Format code
make format

# Run linting
make lint

# Run tests
make test

# Clean temporary files
make clean

# Initial setup
make setup

# Validate repository structure
make validate
```

## Creating a New Project

### Option 1: Use the Makefile (Recommended)
```bash
make new-project
# Follow the prompts to enter project number and name
```

### Option 2: Manual Creation
1. Create a new directory in `projects/` with the format `XX_project_name`
2. Copy the template from `common/templates/project_template.md`
3. Customize the README and create your notebook
4. Add the project to the index table above

### Project Naming Convention
- Use descriptive `snake_case` names (e.g., `customer_churn_prediction`)
- No numeric prefixes
- Skills documented in README title (e.g., `# Project Name (Skill1, Skill2)`)
- Keep names concise but descriptive

## 🛠️ Development Workflow

### Code Quality
- **Formatting**: Code is automatically formatted with `black` and `isort`
- **Linting**: Code quality checked with `flake8`
- **Type Checking**: Static type checking with `mypy`
- **Security**: Security vulnerabilities checked with `bandit`

### Pre-commit Hooks
The repository uses pre-commit hooks to ensure code quality:
- Automatic code formatting
- Import sorting
- Linting checks
- Notebook cleaning
- Security checks
- Large file prevention

### Continuous Integration
GitHub Actions automatically:
- Runs tests on push/PR
- Checks code quality
- Validates notebooks
- Performs security scans
- Builds the package

## Common Utilities

The `common/utils/` module provides reusable functions:

### Data Utilities (`data_utils.py`)
- `load_data()` - Load data from various formats
- `save_data()` - Save data to various formats
- `validate_data()` - Data quality validation
- `get_data_info()` - Comprehensive data summary

### Visualization Utilities (`viz_utils.py`)
- `set_plot_style()` - Consistent plotting style
- `create_plot()` - Common plot types
- `save_plot()` - Save plots with consistent settings
- `create_correlation_heatmap()` - Correlation analysis
- `create_distribution_plot()` - Distribution analysis

### Machine Learning Utilities (`ml_utils.py`)
- `evaluate_model()` - Model evaluation
- `cross_validate()` - Cross-validation
- `feature_importance()` - Feature importance analysis
- `prepare_data_for_ml()` - Data preprocessing
- `create_model_summary()` - Comprehensive model summary

## Data Management

### Data Guidelines
- **Never commit large datasets** to git (use `.gitignore`)
- **Document data sources** in project READMEs
- **Include data dictionaries** for complex datasets
- **Store processed data** in `data/` directories
- **Use relative paths** in notebooks

### Supported Data Formats
- CSV, Excel (.xlsx, .xls)
- Parquet, HDF5
- JSON, Pickle
- Database connections (SQLAlchemy)

## Troubleshooting

### Common Issues

**Import errors with common utilities**
```bash
# Make sure you're in the repository root
# Install in development mode
pip install -e .
```

**Pre-commit hooks not working**
```bash
# Reinstall hooks
pre-commit install --overwrite
```

**Notebook formatting issues**
```bash
# Clean notebooks manually
nbqa black .
nbqa isort .
```

### Getting Help
- Check the [Issues](../../issues) page for known problems
- Review the [Makefile](./Makefile) for available commands
- Examine the [CI workflow](./.github/workflows/ci.yml) for error details

## Contributing

### Adding New Projects
1. Create your project directory
2. Follow the project template
3. Update this README with project details
4. Ensure all tests pass
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions
- Include tests for new utilities
- Keep notebooks clean and well-documented

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Yandex Practicum** - For providing the educational framework
- **Open Source Community** - For the amazing tools and libraries
- **Fellow Students** - For collaboration and feedback

---

## Project Status

- **Total Projects**: 26
- **Completed**: 25
- **In Progress**: 0
- **Template**: 1
- **Featured Portfolio**: 5

*Last updated: January 2026*
