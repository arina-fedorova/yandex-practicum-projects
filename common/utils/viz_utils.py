"""
Visualization utilities for common data science operations.

This module provides functions for creating, customizing, and saving plots
across different projects.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Optional, Dict, Any, List, Tuple
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def set_plot_style(
    style: str = "default",
    context: str = "notebook",
    palette: str = "husl",
    font_scale: float = 1.0
) -> None:
    """
    Set consistent plotting style across all visualizations.
    
    Args:
        style: Matplotlib style to use
        context: Seaborn context (paper, notebook, talk, poster)
        palette: Color palette for plots
        font_scale: Font size scaling factor
    """
    # Set matplotlib style
    plt.style.use(style)
    
    # Set seaborn context and style
    sns.set_context(context, font_scale=font_scale)
    sns.set_palette(palette)
    
    # Set default figure size and DPI
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 300
    
    # Set font properties
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    
    logger.info(f"Plot style set: {style}, context: {context}, palette: {palette}")


def create_plot(
    plot_type: str,
    data: pd.DataFrame,
    x: Optional[str] = None,
    y: Optional[str] = None,
    hue: Optional[str] = None,
    **kwargs
) -> plt.Figure:
    """
    Create common types of plots with consistent styling.
    
    Args:
        plot_type: Type of plot to create
        data: DataFrame containing the data
        x: Column name for x-axis
        y: Column name for y-axis
        hue: Column name for color grouping
        **kwargs: Additional arguments for the plot
        
    Returns:
        Matplotlib Figure object
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    try:
        if plot_type == "histogram":
            sns.histplot(data=data, x=x, hue=hue, **kwargs)
        elif plot_type == "boxplot":
            sns.boxplot(data=data, x=x, y=y, hue=hue, **kwargs)
        elif plot_type == "scatter":
            sns.scatterplot(data=data, x=x, y=y, hue=hue, **kwargs)
        elif plot_type == "line":
            sns.lineplot(data=data, x=x, y=y, hue=hue, **kwargs)
        elif plot_type == "bar":
            sns.barplot(data=data, x=x, y=y, hue=hue, **kwargs)
        elif plot_type == "violin":
            sns.violinplot(data=data, x=x, y=y, hue=hue, **kwargs)
        elif plot_type == "heatmap":
            sns.heatmap(data, **kwargs)
        elif plot_type == "pairplot":
            return sns.pairplot(data, hue=hue, **kwargs)
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")
            
        # Improve plot appearance
        ax.set_title(f"{plot_type.title()} Plot", fontsize=16, fontweight='bold')
        if x:
            ax.set_xlabel(x.replace('_', ' ').title(), fontsize=12)
        if y:
            ax.set_ylabel(y.replace('_', ' ').title(), fontsize=12)
            
        plt.tight_layout()
        return fig
        
    except Exception as e:
        logger.error(f"Error creating {plot_type} plot: {e}")
        raise


def save_plot(
    fig: plt.Figure,
    file_path: Union[str, Path],
    format: str = "png",
    dpi: int = 300,
    bbox_inches: str = "tight"
) -> None:
    """
    Save plot to file with consistent settings.
    
    Args:
        fig: Matplotlib Figure object to save
        file_path: Path where to save the plot
        format: Output format (png, pdf, svg, jpg)
        dpi: Resolution for raster formats
        bbox_inches: Bounding box setting
    """
    file_path = Path(file_path)
    
    # Create directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        fig.savefig(
            file_path,
            format=format,
            dpi=dpi,
            bbox_inches=bbox_inches,
            facecolor='white',
            edgecolor='none'
        )
        logger.info(f"Plot saved successfully to {file_path}")
        
    except Exception as e:
        logger.error(f"Error saving plot to {file_path}: {e}")
        raise


def create_correlation_heatmap(
    data: pd.DataFrame,
    method: str = "pearson",
    figsize: Tuple[int, int] = (10, 8),
    annot: bool = True,
    cmap: str = "coolwarm"
) -> plt.Figure:
    """
    Create a correlation heatmap for numeric columns.
    
    Args:
        data: DataFrame with numeric columns
        method: Correlation method (pearson, spearman, kendall)
        figsize: Figure size as (width, height)
        annot: Whether to show correlation values
        cmap: Color map for the heatmap
        
    Returns:
        Matplotlib Figure object
    """
    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    if numeric_data.empty:
        raise ValueError("No numeric columns found in the data")
    
    # Calculate correlation matrix
    corr_matrix = numeric_data.corr(method=method)
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        corr_matrix,
        annot=annot,
        cmap=cmap,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )
    
    ax.set_title(f"Correlation Matrix ({method.title()})", fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    return fig


def create_distribution_plot(
    data: pd.DataFrame,
    columns: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (15, 10)
) -> plt.Figure:
    """
    Create distribution plots for multiple columns.
    
    Args:
        data: DataFrame containing the data
        columns: List of columns to plot (uses all numeric if None)
        figsize: Figure size as (width, height)
        
    Returns:
        Matplotlib Figure object
    """
    if columns is None:
        columns = list(data.select_dtypes(include=[np.number]).columns)
    
    if not columns:
        raise ValueError("No columns specified and no numeric columns found")
    
    n_cols = min(3, len(columns))
    n_rows = (len(columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    if n_cols == 1:
        axes = axes.reshape(-1, 1)
    
    for i, col in enumerate(columns):
        row = i // n_cols
        col_idx = i % n_cols
        
        if col in data.columns:
            if data[col].dtype in ['object', 'category']:
                # Categorical data - bar plot
                value_counts = data[col].value_counts()
                axes[row, col_idx].bar(range(len(value_counts)), value_counts.values)
                axes[row, col_idx].set_xticks(range(len(value_counts)))
                axes[row, col_idx].set_xticklabels(value_counts.index, rotation=45)
                axes[row, col_idx].set_title(f"Distribution of {col}")
            else:
                # Numeric data - histogram
                axes[row, col_idx].hist(data[col].dropna(), bins=30, alpha=0.7, edgecolor='black')
                axes[row, col_idx].set_title(f"Distribution of {col}")
                axes[row, col_idx].set_xlabel(col)
                axes[row, col_idx].set_ylabel("Frequency")
    
    # Hide empty subplots
    for i in range(len(columns), n_rows * n_cols):
        row = i // n_cols
        col_idx = i % n_cols
        axes[row, col_idx].set_visible(False)
    
    plt.tight_layout()
    return fig


def add_statistical_annotations(
    ax: plt.Axes,
    data: pd.DataFrame,
    x: str,
    y: str,
    test: str = "t-test"
) -> None:
    """
    Add statistical test annotations to plots.
    
    Args:
        ax: Matplotlib Axes object
        data: DataFrame containing the data
        x: Categorical column for grouping
        y: Numeric column for comparison
        test: Statistical test to perform
    """
    try:
        from scipy import stats
        
        # Perform statistical test
        if test == "t-test":
            groups = [group[y].dropna() for name, group in data.groupby(x)]
            if len(groups) == 2:
                stat, p_value = stats.ttest_ind(groups[0], groups[1])
                test_name = "t-test"
            else:
                stat, p_value = stats.f_oneway(*groups)
                test_name = "ANOVA"
        
        # Add annotation
        significance = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else "ns"
        ax.text(
            0.02, 0.98,
            f"{test_name}: p = {p_value:.3f} {significance}",
            transform=ax.transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
        )
        
    except ImportError:
        logger.warning("scipy not available, skipping statistical annotations")
    except Exception as e:
        logger.warning(f"Could not add statistical annotations: {e}")
