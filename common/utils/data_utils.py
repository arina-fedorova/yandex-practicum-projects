"""
Data utilities for common data science operations.

This module provides functions for loading, saving, and validating data
across different projects.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Optional, Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_data(
    file_path: Union[str, Path],
    file_type: Optional[str] = None,
    **kwargs
) -> pd.DataFrame:
    """
    Load data from various file formats.
    
    Args:
        file_path: Path to the data file
        file_type: Type of file (auto-detected if None)
        **kwargs: Additional arguments passed to pandas read functions
        
    Returns:
        Loaded data as pandas DataFrame
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file type is not supported
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Auto-detect file type if not specified
    if file_type is None:
        file_type = file_path.suffix.lower()
    
    try:
        if file_type in ['.csv', '.txt']:
            return pd.read_csv(file_path, **kwargs)
        elif file_type in ['.xlsx', '.xls']:
            return pd.read_excel(file_path, **kwargs)
        elif file_type in ['.parquet']:
            return pd.read_parquet(file_path, **kwargs)
        elif file_type in ['.h5', '.hdf5']:
            return pd.read_hdf(file_path, **kwargs)
        elif file_type in ['.json']:
            return pd.read_json(file_path, **kwargs)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
            
    except Exception as e:
        logger.error(f"Error loading file {file_path}: {e}")
        raise


def save_data(
    data: pd.DataFrame,
    file_path: Union[str, Path],
    file_type: Optional[str] = None,
    **kwargs
) -> None:
    """
    Save data to various file formats.
    
    Args:
        data: DataFrame to save
        file_path: Path where to save the file
        file_type: Type of file (auto-detected if None)
        **kwargs: Additional arguments passed to pandas save functions
    """
    file_path = Path(file_path)
    
    # Auto-detect file type if not specified
    if file_type is None:
        file_type = file_path.suffix.lower()
    
    # Create directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        if file_type in ['.csv', '.txt']:
            data.to_csv(file_path, index=False, **kwargs)
        elif file_type in ['.xlsx', '.xls']:
            data.to_excel(file_path, index=False, **kwargs)
        elif file_type in ['.parquet']:
            data.to_parquet(file_path, index=False, **kwargs)
        elif file_type in ['.h5', '.hdf5']:
            data.to_hdf(file_path, key='data', index=False, **kwargs)
        elif file_type in ['.json']:
            data.to_json(file_path, orient='records', **kwargs)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
            
        logger.info(f"Data saved successfully to {file_path}")
        
    except Exception as e:
        logger.error(f"Error saving file {file_path}: {e}")
        raise


def validate_data(
    data: pd.DataFrame,
    expected_columns: Optional[list] = None,
    expected_dtypes: Optional[Dict[str, Any]] = None,
    check_missing: bool = True,
    check_duplicates: bool = True
) -> Dict[str, Any]:
    """
    Validate data quality and structure.
    
    Args:
        data: DataFrame to validate
        expected_columns: List of expected column names
        expected_dtypes: Dictionary of expected column data types
        check_missing: Whether to check for missing values
        check_duplicates: Whether to check for duplicate rows
        
    Returns:
        Dictionary with validation results
    """
    validation_results = {
        'is_valid': True,
        'errors': [],
        'warnings': [],
        'summary': {}
    }
    
    # Check if DataFrame is empty
    if data.empty:
        validation_results['is_valid'] = False
        validation_results['errors'].append("DataFrame is empty")
        return validation_results
    
    # Check expected columns
    if expected_columns:
        missing_cols = set(expected_columns) - set(data.columns)
        if missing_cols:
            validation_results['is_valid'] = False
            validation_results['errors'].append(f"Missing columns: {missing_cols}")
    
    # Check data types
    if expected_dtypes:
        for col, expected_dtype in expected_dtypes.items():
            if col in data.columns:
                if not pd.api.types.is_dtype_equal(data[col].dtype, expected_dtype):
                    validation_results['warnings'].append(
                        f"Column {col} has dtype {data[col].dtype}, expected {expected_dtype}"
                    )
    
    # Check missing values
    if check_missing:
        missing_counts = data.isnull().sum()
        if missing_counts.sum() > 0:
            validation_results['warnings'].append(
                f"Missing values found: {missing_counts.to_dict()}"
            )
    
    # Check duplicates
    if check_duplicates:
        duplicate_count = data.duplicated().sum()
        if duplicate_count > 0:
            validation_results['warnings'].append(
                f"Found {duplicate_count} duplicate rows"
            )
    
    # Generate summary
    validation_results['summary'] = {
        'shape': data.shape,
        'memory_usage': data.memory_usage(deep=True).sum(),
        'dtypes': data.dtypes.to_dict(),
        'missing_values': data.isnull().sum().to_dict() if check_missing else {},
        'duplicate_rows': data.duplicated().sum() if check_duplicates else 0
    }
    
    return validation_results


def get_data_info(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Get comprehensive information about a DataFrame.
    
    Args:
        data: DataFrame to analyze
        
    Returns:
        Dictionary with data information
    """
    info = {
        'shape': data.shape,
        'columns': list(data.columns),
        'dtypes': data.dtypes.to_dict(),
        'memory_usage': data.memory_usage(deep=True).sum(),
        'missing_values': data.isnull().sum().to_dict(),
        'numeric_columns': list(data.select_dtypes(include=[np.number]).columns),
        'categorical_columns': list(data.select_dtypes(include=['object', 'category']).columns),
        'datetime_columns': list(data.select_dtypes(include=['datetime']).columns),
        'duplicate_rows': data.duplicated().sum(),
        'unique_counts': {col: data[col].nunique() for col in data.columns}
    }
    
    return info
