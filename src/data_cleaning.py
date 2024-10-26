import os
import pandas as pd
import logging
from datetime import datetime

# Ensure the logs directory exists
log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)

# Setup logging
logging.basicConfig(filename=os.path.join(log_dir, 'cleaning.log'), level=logging.INFO)

def clean_data(df):
    try:
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Remove rows where important columns are missing (like DTC code or timestamp)
        df.dropna(subset=['dtc_code', 'timestamp'], inplace=True)

        # Ensure DTC codes are uppercase
        df['dtc_code'] = df['dtc_code'].str.upper()

        # Map severity levels to numerical values
        severity_map = {'low': 1, 'medium': 2, 'high': 3}
        df['severity_level'] = df['severity'].map(severity_map)

        # Remove any rows with missing or invalid severity
        df = df.dropna(subset=['severity_level'])

        logging.info(f"{datetime.now()}: Data successfully cleaned.")
        return df
    except Exception as e:
        logging.error(f"{datetime.now()}: Error cleaning data - {str(e)}")
        return None

if __name__ == "__main__":
    # Load the raw data
    df = pd.read_csv('./data/raw/vehicle_dtc_data.csv')

    # Clean the data
    cleaned_df = clean_data(df)

    # Save cleaned data
    if cleaned_df is not None:
        cleaned_df.to_csv('./data/cleaned/cleaned_vehicle_dtc_data.csv', index=False)
        print(cleaned_df.head())
    else:
        print("Data cleaning failed. Check logs for details.")
