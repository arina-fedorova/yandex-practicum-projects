# 🚀 Yandex Practicum Data Science Projects

A collection of data analysis projects implemented during the Data Science course at Yandex Practicum. The projects cover various real-world datasets and focus on exploratory data analysis, data cleaning, and reporting.

## Projects Index

| # | Project Name | Description | Status | Technologies |
|---|--------------|-------------|---------|--------------|
| 01 | [Project Template](./projects/01_project_template) | Template for new projects | 🟡 Template | Python, Jupyter |
| 02 | [Coming Soon...] | - | ⏳ Planned | - |
| 03 | [Coming Soon...] | - | ⏳ Planned | - |

## Repository Structure

```
yandex-practicum-projects/
├── README.md                    # This file - Project overview
├── projects/                    # Individual project directories
│   ├── 01_project_template/    # Project template
│   ├── 02_[project_name]/      # Future projects
│   └── ...
├── common/                      # Shared utilities and templates
│   ├── utils/                  # Common utility functions
│   │   ├── data_utils.py      # Data loading, saving, validation
│   │   ├── viz_utils.py       # Visualization helpers
│   │   └── ml_utils.py        # Machine learning utilities
│   └── templates/              # Project templates
├── .github/workflows/          # CI/CD workflows
├── pyproject.toml              # Project configuration
├── requirements.txt             # Python dependencies
├── .pre-commit-config.yaml     # Pre-commit hooks
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
- Use the format: `XX_project_name` (e.g., `01_customer_churn_analysis`)
- XX = sequential number (01, 02, 03...)
- project_name = descriptive name in kebab-case
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

- **Total Projects**: 1 (Template)
- **Completed**: 0
- **In Progress**: 0
- **Planned**: 2+

*Last updated: [Current Date]*
