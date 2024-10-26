import unittest
import pandas as pd
from src.data_ingestion import ingest_data

class TestDataIngestion(unittest.TestCase):
    
    def test_ingest_data(self):
        # Sample test to ensure data ingestion works
        df = ingest_data('../data/raw/sample_data.csv')
        
        # Test if the dataframe is not empty
        self.assertIsNotNone(df)
        
        # Test if dataframe has the expected columns
        expected_columns = ['vehicle_id', 'timestamp', 'dtc_code', 'severity', 'description']
        self.assertTrue(all([col in df.columns for col in expected_columns]))
        
        # Test if the data contains rows
        self.assertGreater(len(df), 0)

if __name__ == '__main__':
    unittest.main()
