import pandas as pd
import requests
import yaml
import logging
from datetime import datetime

# Load configuration from config.yaml
with open('./config/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract Telegram bot token and chat ID from config file
bot_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']

logging.basicConfig(filename='./logs/alerts.log', level=logging.INFO)

def send_telegram_alert(message):
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(api_url, params=params)
    return response.status_code

def monitor_critical_issues(df):
    critical_issues = df[df['severity'] == 'high']
    for _, row in critical_issues.iterrows():
        message = f"Critical Alert! Vehicle {row['vehicle_id']} reported issue: {row['description']}"
        send_telegram_alert(message)
        logging.info(f"{datetime.now()}: Alert sent for Vehicle {row['vehicle_id']}")

if __name__ == "__main__":
    df = pd.read_csv('./data/cleaned/cleaned_vehicle_dtc_data.csv')
    monitor_critical_issues(df)
