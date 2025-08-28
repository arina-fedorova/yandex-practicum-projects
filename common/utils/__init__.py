"""
Common utilities for Yandex Practicum Data Science projects.

This package contains reusable functions and classes that can be shared
across different projects in the monorepo.
"""

__version__ = "0.1.0"
__author__ = "Data Science Student"

# Import commonly used utilities
from .data_utils import *
from .viz_utils import *
from .ml_utils import *

__all__ = [
    # Data utilities
    "load_data",
    "save_data",
    "validate_data",
    
    # Visualization utilities
    "create_plot",
    "save_plot",
    "set_plot_style",
    
    # Machine Learning utilities
    "evaluate_model",
    "cross_validate",
    "feature_importance",
]
