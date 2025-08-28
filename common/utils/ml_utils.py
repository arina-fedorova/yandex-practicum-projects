"""
Machine Learning utilities for common data science operations.

This module provides functions for model evaluation, cross-validation,
feature importance analysis, and other ML-related tasks.
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any, Tuple, Optional
from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, mean_squared_error, mean_absolute_error, r2_score,
    classification_report, confusion_matrix
)
from sklearn.preprocessing import StandardScaler, LabelEncoder
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def evaluate_model(
    model,
    X_test: Union[pd.DataFrame, np.ndarray],
    y_test: Union[pd.Series, np.ndarray],
    task: str = "classification",
    **kwargs
) -> Dict[str, Any]:
    """
    Evaluate a trained model on test data.
    
    Args:
        model: Trained scikit-learn model
        X_test: Test features
        y_test: Test targets
        task: Task type ("classification" or "regression")
        **kwargs: Additional arguments for specific metrics
        
    Returns:
        Dictionary containing evaluation metrics
    """
    try:
        y_pred = model.predict(X_test)
        
        if task == "classification":
            # Handle binary vs multiclass classification
            if len(np.unique(y_test)) == 2:
                # Binary classification
                y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
                
                metrics = {
                    'accuracy': accuracy_score(y_test, y_pred),
                    'precision': precision_score(y_test, y_pred, average='binary'),
                    'recall': recall_score(y_test, y_pred, average='binary'),
                    'f1': f1_score(y_test, y_pred, average='binary'),
                }
                
                if y_pred_proba is not None:
                    metrics['roc_auc'] = roc_auc_score(y_test, y_pred_proba)
                    
            else:
                # Multiclass classification
                metrics = {
                    'accuracy': accuracy_score(y_test, y_pred),
                    'precision_macro': precision_score(y_test, y_pred, average='macro'),
                    'precision_weighted': precision_score(y_test, y_pred, average='weighted'),
                    'recall_macro': recall_score(y_test, y_pred, average='macro'),
                    'recall_weighted': recall_score(y_test, y_pred, average='weighted'),
                    'f1_macro': f1_score(y_test, y_pred, average='macro'),
                    'f1_weighted': f1_score(y_test, y_pred, average='weighted'),
                }
                
        elif task == "regression":
            metrics = {
                'mse': mean_squared_error(y_test, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
                'mae': mean_absolute_error(y_test, y_pred),
                'r2': r2_score(y_test, y_pred),
            }
            
        else:
            raise ValueError(f"Unsupported task type: {task}")
            
        # Add predictions to results
        results = {
            'metrics': metrics,
            'predictions': y_pred,
            'task': task,
            'model_type': type(model).__name__
        }
        
        logger.info(f"Model evaluation completed for {task} task")
        return results
        
    except Exception as e:
        logger.error(f"Error evaluating model: {e}")
        raise


def cross_validate(
    model,
    X: Union[pd.DataFrame, np.ndarray],
    y: Union[pd.Series, np.ndarray],
    cv: int = 5,
    scoring: Union[str, List[str]] = "default",
    task: str = "classification",
    **kwargs
) -> Dict[str, Any]:
    """
    Perform cross-validation on a model.
    
    Args:
        model: Scikit-learn model to validate
        X: Features
        y: Targets
        cv: Number of cross-validation folds
        scoring: Scoring metric(s) to use
        task: Task type ("classification" or "regression")
        **kwargs: Additional arguments for cross_val_score
        
    Returns:
        Dictionary containing cross-validation results
    """
    try:
        # Set default scoring based on task
        if scoring == "default":
            if task == "classification":
                scoring = "accuracy"
            elif task == "regression":
                scoring = "r2"
        
        # Perform cross-validation
        cv_scores = cross_val_score(
            model, X, y, cv=cv, scoring=scoring, **kwargs
        )
        
        results = {
            'cv_scores': cv_scores,
            'mean_score': cv_scores.mean(),
            'std_score': cv_scores.std(),
            'min_score': cv_scores.min(),
            'max_score': cv_scores.max(),
            'cv_folds': cv,
            'scoring': scoring,
            'task': task
        }
        
        logger.info(f"Cross-validation completed: {scoring} = {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
        return results
        
    except Exception as e:
        logger.error(f"Error in cross-validation: {e}")
        raise


def feature_importance(
    model,
    feature_names: Optional[List[str]] = None,
    method: str = "default",
    **kwargs
) -> pd.DataFrame:
    """
    Extract feature importance from a trained model.
    
    Args:
        model: Trained scikit-learn model
        feature_names: List of feature names (uses default if None)
        method: Method to extract importance ("default", "permutation", "shap")
        **kwargs: Additional arguments for specific methods
        
    Returns:
        DataFrame with feature names and importance scores
    """
    try:
        if method == "default":
            # Try to get feature_importances_ attribute
            if hasattr(model, 'feature_importances_'):
                importance_scores = model.feature_importances_
            elif hasattr(model, 'coef_'):
                # For linear models, use absolute coefficients
                importance_scores = np.abs(model.coef_)
                if importance_scores.ndim > 1:
                    importance_scores = np.mean(importance_scores, axis=0)
            else:
                raise ValueError("Model doesn't have feature_importances_ or coef_ attributes")
                
        elif method == "permutation":
            # Use permutation importance (requires sklearn >= 0.22)
            try:
                from sklearn.inspection import permutation_importance
                # This would require X and y, so we'll use default method
                logger.warning("Permutation importance requires X and y data, using default method")
                return feature_importance(model, feature_names, method="default")
            except ImportError:
                logger.warning("Permutation importance not available, using default method")
                return feature_importance(model, feature_names, method="default")
                
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        # Create feature names if not provided
        if feature_names is None:
            feature_names = [f"feature_{i}" for i in range(len(importance_scores))]
        
        # Create DataFrame
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance_scores
        }).sort_values('importance', ascending=False)
        
        # Add percentage
        importance_df['importance_pct'] = (importance_df['importance'] / importance_df['importance'].sum()) * 100
        
        logger.info(f"Feature importance extracted using {method} method")
        return importance_df
        
    except Exception as e:
        logger.error(f"Error extracting feature importance: {e}")
        raise


def prepare_data_for_ml(
    data: pd.DataFrame,
    target_column: str,
    categorical_columns: Optional[List[str]] = None,
    numeric_columns: Optional[List[str]] = None,
    test_size: float = 0.2,
    random_state: int = 42,
    scale_numeric: bool = True,
    encode_categorical: bool = True
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """
    Prepare data for machine learning tasks.
    
    Args:
        data: Input DataFrame
        target_column: Name of the target column
        categorical_columns: List of categorical columns
        numeric_columns: List of numeric columns
        test_size: Proportion of data for testing
        random_state: Random seed for reproducibility
        scale_numeric: Whether to scale numeric features
        encode_categorical: Whether to encode categorical features
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test, preprocessing_info)
    """
    try:
        # Identify columns if not specified
        if categorical_columns is None:
            categorical_columns = list(data.select_dtypes(include=['object', 'category']).columns)
            if target_column in categorical_columns:
                categorical_columns.remove(target_column)
                
        if numeric_columns is None:
            numeric_columns = list(data.select_dtypes(include=[np.number]).columns)
            if target_column in numeric_columns:
                numeric_columns.remove(target_column)
        
        # Create feature matrix
        X = data[numeric_columns + categorical_columns].copy()
        y = data[target_column]
        
        # Handle missing values
        X = X.fillna(X.median() if numeric_columns else X.mode().iloc[0])
        
        preprocessing_info = {}
        
        # Encode categorical variables
        if encode_categorical and categorical_columns:
            label_encoders = {}
            for col in categorical_columns:
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col].astype(str))
                label_encoders[col] = le
            preprocessing_info['label_encoders'] = label_encoders
        
        # Scale numeric features
        if scale_numeric and numeric_columns:
            scaler = StandardScaler()
            X[numeric_columns] = scaler.fit_transform(X[numeric_columns])
            preprocessing_info['scaler'] = scaler
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y if len(y.unique()) <= 10 else None
        )
        
        # Convert to numpy arrays
        X_train = X_train.values
        X_test = X_test.values
        y_train = y_train.values
        y_test = y_test.values
        
        preprocessing_info['feature_names'] = X.columns.tolist()
        preprocessing_info['categorical_columns'] = categorical_columns
        preprocessing_info['numeric_columns'] = numeric_columns
        
        logger.info(f"Data prepared: {X_train.shape[0]} training samples, {X_test.shape[0]} test samples")
        return X_train, X_test, y_train, y_test, preprocessing_info
        
    except Exception as e:
        logger.error(f"Error preparing data for ML: {e}")
        raise


def create_model_summary(
    model,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    feature_names: Optional[List[str]] = None,
    task: str = "classification"
) -> Dict[str, Any]:
    """
    Create a comprehensive model summary.
    
    Args:
        model: Trained model
        X_train: Training features
        y_train: Training targets
        X_test: Test features
        y_test: Test targets
        feature_names: List of feature names
        task: Task type
        
    Returns:
        Dictionary containing model summary
    """
    try:
        # Evaluate model
        evaluation = evaluate_model(model, X_test, y_test, task=task)
        
        # Get feature importance
        importance = feature_importance(model, feature_names)
        
        # Cross-validation results
        cv_results = cross_validate(model, X_train, y_train, task=task)
        
        summary = {
            'model_info': {
                'type': type(model).__name__,
                'parameters': model.get_params(),
                'task': task
            },
            'data_info': {
                'training_samples': X_train.shape[0],
                'test_samples': X_test.shape[0],
                'features': X_train.shape[1],
                'feature_names': feature_names
            },
            'performance': evaluation['metrics'],
            'cross_validation': cv_results,
            'feature_importance': importance,
            'predictions': evaluation['predictions']
        }
        
        logger.info("Model summary created successfully")
        return summary
        
    except Exception as e:
        logger.error(f"Error creating model summary: {e}")
        raise
