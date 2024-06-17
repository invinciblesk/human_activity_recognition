import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Load the data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
     """Clean the data."""
    # Convert timestamp to datetime
     df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Add your data cleaning steps here
    # For example, remove rows with missing values
     df = df.dropna()

     # drop duplicates
     df.drop_duplicates(inplace=True)
     return df