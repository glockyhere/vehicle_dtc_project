import unittest
import pandas as pd
from src.model_training import RandomForestClassifier, train_test_split

class TestModelTraining(unittest.TestCase):
    def setUp(self):
        # Set up sample cleaned data
        self.cleaned_data = pd.DataFrame({
            'severity_level': [1, 2, 3],
            'timestamp': ['2024-01-01 12:00:00', '2024-01-02 14:00:00', '2024-01-03 10:00:00'],
            'dtc_code': ['C134113', 'C190004', 'C134112']
        })

        # Feature Engineering
        self.cleaned_data['timestamp'] = pd.to_datetime(self.cleaned_data['timestamp'])
        self.cleaned_data['hour'] = self.cleaned_data['timestamp'].dt.hour

        # Features and target
        self.X = self.cleaned_data[['severity_level', 'hour']]
        self.y = self.cleaned_data['dtc_code']

    def test_model_training(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
