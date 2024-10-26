import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import logging

# Setup logging
logging.basicConfig(filename='./logs/model_training.log', level=logging.INFO)

# Load cleaned data
df = pd.read_csv('./data/cleaned/cleaned_vehicle_dtc_data.csv')

# Feature Engineering
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

# Features and target
X = df[['severity_level', 'hour']]
y = df['dtc_code']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, './models/trained_model.pkl')

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

logging.info("Model training completed and saved.")
