"""
Data Processing Utilities for the Streamlit Data App.
This module contains functions for loading, processing, and filtering data.
"""

import pandas as pd
import numpy as np
import io


def load_data(uploaded_file):
    """
    Load data from an uploaded file (CSV or Excel).
    
    Parameters:
    -----------
    uploaded_file : UploadedFile
        The file uploaded through Streamlit's file_uploader
        
    Returns:
    --------
    pandas.DataFrame
        Loaded data as a DataFrame
    """
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "csv":
            return pd.read_csv(uploaded_file)
        elif file_extension in ["xlsx", "xls"]:
            return pd.read_excel(uploaded_file)
        else:
            raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")
    
    return None


def get_summary_statistics(df):
    """
    Generate summary statistics for a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze
        
    Returns:
    --------
    pandas.DataFrame
        Summary statistics including count, mean, std, min, max, and data types
    """
    if df is None or df.empty:
        return None
    
    numeric_summary = df.describe().T
    
    # Add data type information
    numeric_summary['dtype'] = df.dtypes.values
    
    # Count missing values
    numeric_summary['missing'] = df.isnull().sum().values
    numeric_summary['missing_pct'] = (df.isnull().sum() / len(df) * 100).values
    
    return numeric_summary


def filter_dataframe(df, filters):
    """
    Apply filters to a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to filter
    filters : dict
        Dictionary containing filter conditions
        
    Returns:
    --------
    pandas.DataFrame
        Filtered DataFrame
    """
    if df is None or df.empty or not filters:
        return df
    
    filtered_df = df.copy()
    
    for column, condition in filters.items():
        if column in filtered_df.columns:
            if isinstance(condition, tuple) and len(condition) == 2:
                # Range filter for numeric columns
                min_val, max_val = condition
                filtered_df = filtered_df[(filtered_df[column] >= min_val) & 
                                         (filtered_df[column] <= max_val)]
            elif isinstance(condition, list):
                # Multi-select filter for categorical columns
                filtered_df = filtered_df[filtered_df[column].isin(condition)]
    
    return filtered_df


def convert_df_to_csv(df):
    """
    Convert DataFrame to CSV for download.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to convert
        
    Returns:
    --------
    str
        CSV string representation of the DataFrame
    """
    return df.to_csv(index=False).encode('utf-8')