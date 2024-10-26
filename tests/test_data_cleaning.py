import unittest
import pandas as pd
from src.data_cleaning import clean_data

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Set up some sample raw data
        self.raw_data = pd.DataFrame({
            'vehicle_id': ['V1234', 'V5678'],
            'timestamp': ['2024-01-01 12:00:00', '2024-01-02 14:00:00'],
            'dtc_code': ['c134113', 'c190004'],
            'severity': ['medium', 'high'],
            'description': ['Brake sensor malfunction', 'High-pressure warning']
        })

    def test_clean_data(self):
        cleaned_data = clean_data(self.raw_data)
        # Check if timestamp is converted to datetime
        self.assertEqual(pd.api.types.is_datetime64_any_dtype(cleaned_data['timestamp']), True)
        # Check if DTC codes are uppercased
        self.assertEqual(cleaned_data['dtc_code'][0], 'C134113')
        # Check if severity level is correctly mapped
        self.assertEqual(cleaned_data['severity_level'][0], 2)

if __name__ == '__main__':
    unittest.main()
