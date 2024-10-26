import os
import pandas as pd
from faker import Faker
import random

# Ensure the raw data directory exists
raw_data_dir = './data/raw'
os.makedirs(raw_data_dir, exist_ok=True)

# Initialize Faker for generating fake data
fake = Faker()

# Define some sample DTC codes and descriptions
dtc_codes = {
    'C190004': 'High-pressure warning',
    'C134113': 'Brake sensor malfunction',
    'C134112': 'Steering angle sensor failure',
    'C134131': 'Electronic stability control failure',
    'C134138': 'Tire pressure warning',
}

# Generate sample vehicle DTC data
def generate_vehicle_dtc_data(num_records=100):
    data = []
    for _ in range(num_records):
        vehicle_id = fake.license_plate()  # Fake vehicle ID
        timestamp = fake.date_time_this_year()  # Random timestamp
        dtc_code = random.choice(list(dtc_codes.keys()))  # Random DTC code
        severity = random.choice(['low', 'medium', 'high'])  # Random severity
        description = dtc_codes[dtc_code]  # Description based on DTC code
        data.append([vehicle_id, timestamp, dtc_code, severity, description])
    
    return pd.DataFrame(data, columns=['vehicle_id', 'timestamp', 'dtc_code', 'severity', 'description'])

# Generate 100 rows of sample data
df = generate_vehicle_dtc_data(100)

# Save the data to a CSV file
csv_file_path = os.path.join(raw_data_dir, 'vehicle_dtc_data.csv')
df.to_csv(csv_file_path, index=False)

print(f"Sample CSV data saved to {csv_file_path}")
