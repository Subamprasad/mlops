import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
from src.exception import CustomException
from src.logger import logging

# Define path to dataset
DATA_PATH = os.path.join('notebook', 'stud.csv')

def perform_eda():
    try:
        logging.info("Starting EDA process")
        
        # Check if file exists
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

        # Read dataset
        df = pd.read_csv(DATA_PATH)
        logging.info("Dataset loaded successfully")

        # 1. basic info
        print("-" * 50)
        print("Dataset Head:")
        print(df.head())
        print("-" * 50)
        
        print("\nDataset Info:")
        print(df.info())
        print("-" * 50)

        # 2. Check missing values
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("-" * 50)

        # 3. Check duplicates
        print("\nDuplicate Rows:", df.duplicated().sum())
        print("-" * 50)

        # 4. Statistical Summary
        print("\nStatistical Summary:")
        print(df.describe())
        print("-" * 50)

        # 5. Unique values in categorical columns
        print("\nUnique values in categorical columns:")
        categorical_columns = [feature for feature in df.columns if df[feature].dtype == 'O']
        for col in categorical_columns:
            print(f"{col}: {df[col].unique()}")
        
        logging.info("EDA process completed successfully")

    except Exception as e:
        logging.error("Error occurred during EDA")
        raise CustomException(e, sys)

if __name__ == "__main__":
    perform_eda()
