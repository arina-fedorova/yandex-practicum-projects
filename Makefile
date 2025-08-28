.PHONY: help install install-dev format lint test clean setup notebook-clean pre-commit-install pre-commit-update

# Default target
help:
	@echo "Available commands:"
	@echo "  install          - Install production dependencies"
	@echo "  install-dev      - Install development dependencies"
	@echo "  format           - Format code with black and isort"
	@echo "  lint             - Run linting checks with flake8"
	@echo "  test             - Run tests with pytest"
	@echo "  clean            - Clean temporary files and caches"
	@echo "  setup            - Initial repository setup"
	@echo "  notebook-clean   - Clean Jupyter notebooks"
	@echo "  pre-commit-install - Install pre-commit hooks"
	@echo "  pre-commit-update - Update pre-commit hooks"

# Install production dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

# Format code
format:
	black .
	isort .

# Run linting
lint:
	flake8 .
	mypy .

# Run tests
test:
	pytest

# Clean temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type f -name "*.log" -delete
	find . -type f -name "bandit-report.json" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/

# Initial setup
setup: install-dev pre-commit-install
	@echo "Repository setup complete!"
	@echo "Next steps:"
	@echo "  1. Create your first project in projects/01_project_name/"
	@echo "  2. Add project description to root README.md"
	@echo "  3. Run 'make format' to format your code"
	@echo "  4. Run 'make lint' to check code quality"

# Clean Jupyter notebooks
notebook-clean:
	nbqa black .
	nbqa isort .
	nbqa flake8 .

# Install pre-commit hooks
pre-commit-install:
	pre-commit install

# Update pre-commit hooks
pre-commit-update:
	pre-commit autoupdate

# Check repository status
status:
	@echo "Repository Status:"
	@echo "=================="
	@echo "Python version: $(shell python --version)"
	@echo "Pip version: $(shell pip --version)"
	@echo "Pre-commit hooks: $(shell pre-commit --version 2>/dev/null || echo 'Not installed')"
	@echo "Projects found: $(shell find projects -maxdepth 1 -type d -name "[0-9]*_*" | wc -l)"
	@echo "Active git hooks: $(shell ls -la .git/hooks/ | grep -c '^-')"

# Create new project structure
new-project:
	@echo "Creating new project structure..."
	@read -p "Enter project number (e.g., 01): " project_num; \
	read -p "Enter project name (kebab-case): " project_name; \
	mkdir -p projects/$${project_num}_$${project_name}/{data,src,reports}; \
	echo "# Project $$project_num: $$project_name" > projects/$${project_num}_$${project_name}/README.md; \
	echo "## Description" >> projects/$${project_num}_$${project_name}/README.md; \
	echo "" >> projects/$${project_num}_$${project_name}/README.md; \
	echo "## Data" >> projects/$${project_num}_$${project_name}/README.md; \
	echo "Place your datasets here. See data/README.md for guidelines." >> projects/$${project_num}_$${project_name}/README.md; \
	echo "## Results" >> projects/$${project_num}_$${project_name}/README.md; \
	echo "Generated reports and visualizations go here." >> projects/$${project_num}_$${project_name}/README.md; \
	echo "# Data Guidelines" > projects/$${project_num}_$${project_name}/data/README.md; \
	echo "1. Do not commit large datasets to git" >> projects/$${project_num}_$${project_name}/data/README.md; \
	echo "2. Document data sources and preprocessing steps" >> projects/$${project_num}_$${project_name}/data/README.md; \
	echo "3. Use .gitignore to exclude data files" >> projects/$${project_num}_$${project_name}/data/README.md; \
	echo "Project structure created successfully!"

# Validate repository structure
validate:
	@echo "Validating repository structure..."
	@test -f pyproject.toml || (echo "❌ Missing pyproject.toml" && exit 1)
	@test -f requirements.txt || (echo "❌ Missing requirements.txt" && exit 1)
	@test -f .pre-commit-config.yaml || (echo "❌ Missing .pre-commit-config.yaml" && exit 1)
	@test -f .gitignore || (echo "❌ Missing .gitignore" && exit 1)
	@test -f Makefile || (echo "❌ Missing Makefile" && exit 1)
	@test -d projects || (echo "❌ Missing projects directory" && exit 1)
	@test -d common || (echo "❌ Missing common directory" && exit 1)
	@echo "✅ Repository structure is valid!"
