"""
Visualization Utilities for the Streamlit Data App.
This module contains functions for creating various data visualizations.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def create_histogram(df, column, bins=20, kde=True):
    """
    Create a histogram for the selected column.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    column : str
        The column to visualize
    bins : int
        Number of bins for the histogram
    kde : bool
        Whether to overlay KDE plot
        
    Returns:
    --------
    matplotlib.figure.Figure
        The histogram figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x=column, bins=bins, kde=kde, ax=ax)
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    return fig


def create_scatter_plot(df, x_column, y_column, color_column=None):
    """
    Create a scatter plot for the selected columns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    x_column : str
        The column for x-axis
    y_column : str
        The column for y-axis
    color_column : str, optional
        The column for color encoding
        
    Returns:
    --------
    matplotlib.figure.Figure
        The scatter plot figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if color_column and color_column in df.columns:
        scatter = sns.scatterplot(data=df, x=x_column, y=y_column, hue=color_column, ax=ax)
        
        # If there are too many categories, adjust the legend
        if df[color_column].nunique() > 10:
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        scatter = sns.scatterplot(data=df, x=x_column, y=y_column, ax=ax)
    
    ax.set_title(f'Scatter Plot: {y_column} vs {x_column}')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    plt.tight_layout()
    return fig


def create_bar_chart(df, x_column, y_column, top_n=None):
    """
    Create a bar chart for the selected columns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    x_column : str
        The column for categories (x-axis)
    y_column : str
        The column for values (y-axis)
    top_n : int, optional
        Limit to top N categories by value
        
    Returns:
    --------
    matplotlib.figure.Figure
        The bar chart figure
    """
    # Group and aggregate the data
    chart_data = df.groupby(x_column)[y_column].sum().reset_index()
    
    # Sort and limit to top N if specified
    if top_n:
        chart_data = chart_data.sort_values(y_column, ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar chart
    sns.barplot(data=chart_data, x=x_column, y=y_column, ax=ax)
    
    # Rotate x-axis labels if there are too many categories
    if len(chart_data) > 5:
        plt.xticks(rotation=45, ha='right')
    
    ax.set_title(f'Bar Chart: {y_column} by {x_column}')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    plt.tight_layout()
    return fig


def create_line_chart(df, x_column, y_column, group_column=None):
    """
    Create a line chart for the selected columns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    x_column : str
        The column for x-axis
    y_column : str
        The column for y-axis
    group_column : str, optional
        The column for grouping multiple lines
        
    Returns:
    --------
    matplotlib.figure.Figure
        The line chart figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if group_column and group_column in df.columns:
        for group, data in df.groupby(group_column):
            data = data.sort_values(x_column)
            ax.plot(data[x_column], data[y_column], marker='o', label=group)
        ax.legend(title=group_column)
    else:
        sorted_data = df.sort_values(x_column)
        ax.plot(sorted_data[x_column], sorted_data[y_column], marker='o')
    
    ax.set_title(f'Line Chart: {y_column} vs {x_column}')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    
    # Rotate x-axis labels if there are too many unique values
    if df[x_column].nunique() > 5:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig


def create_correlation_heatmap(df, columns=None):
    """
    Create a correlation heatmap for the selected columns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    columns : list, optional
        List of columns to include in the correlation analysis
        
    Returns:
    --------
    matplotlib.figure.Figure
        The correlation heatmap figure
    """
    # Select only numeric columns if no columns are specified
    if columns:
        data = df[columns].select_dtypes(include=['number'])
    else:
        data = df.select_dtypes(include=['number'])
    
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Create the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
    ax.set_title('Correlation Matrix')
    plt.tight_layout()
    return fig