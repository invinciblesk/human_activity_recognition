import pandas as pd
import numpy as np
from scipy import stats

def clean_data(df, z_score_threshold=3):
    # Fill numeric columns with the median
    for col in df.select_dtypes(include=np.number).columns.tolist():
        df[col].fillna(df[col].median(), inplace=True)

    # Fill non-numeric columns with the mode
    for col in df.select_dtypes(exclude=np.number).columns.tolist():
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Remove rows in numeric columns where the z-score is greater than the threshold
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    for col in numeric_cols:
        df = df[(np.abs(stats.zscore(df[col])) < z_score_threshold)]
    
    # Convert 'timestamp' to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    return df