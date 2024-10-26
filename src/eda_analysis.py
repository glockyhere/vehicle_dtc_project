import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('./data/cleaned/cleaned_vehicle_dtc_data.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Group by month and calculate average severity level for each month
df['month'] = df['timestamp'].dt.to_period('M')
severity_trend = df.groupby('month')['severity_level'].mean()

# Plot the average severity level over time
plt.figure(figsize=(10, 6))
severity_trend.plot(kind='line')
plt.title('Average Severity Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Average Severity Level')
plt.grid(True)
plt.savefig('./data/processed/severity_trend_smooth.png')  # Save the new plot
plt.show()

# OPTIONAL: Scatter plot to show individual events without connecting lines
plt.figure(figsize=(10, 6))
plt.scatter(df['timestamp'], df['severity_level'], alpha=0.5)
plt.title('Severity Levels Over Time (Scatter Plot)')
plt.xlabel('Date')
plt.ylabel('Severity Level')
plt.grid(True)
plt.savefig('./data/processed/severity_scatter.png')  # Save scatter plot
plt.show()
