import pandas as pd
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='./logs/ingestion.log', level=logging.INFO)

def ingest_data(source_file):
    try:
        # Example: Ingesting from CSV
        df = pd.read_csv(source_file)
        logging.info(f"{datetime.now()}: Data successfully ingested from {source_file}")
        return df
    except Exception as e:
        logging.error(f"{datetime.now()}: Error ingesting data - {str(e)}")
        return None

if __name__ == "__main__":
    # Ingest raw vehicle DTC data
    df = ingest_data('./data/raw/vehicle_dtc_data.csv')
    print(df.head())
