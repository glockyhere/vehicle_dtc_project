# Vehicle Diagnostic Trouble Code (DTC) System

This project provides a pipeline to analyze, predict, and alert based on vehicle Diagnostic Trouble Codes (DTCs). It includes data ingestion, cleaning, exploratory data analysis (EDA), machine learning model training, and a real-time dashboard for vehicle health monitoring.

---

## Prerequisites

- Python 3.x
- A Telegram bot for alerts
- Packages listed in requirements.txt

---

## Installation

1. Clone the Project:
   git clone <your-repository-url>
   cd vehicle_dtc_project

2. Install Dependencies:
   pip install -r requirements.txt

---

## Configuration

Set up your Telegram bot and configure the config.yaml file with your bot token and chat ID:

telegram:
  bot_token: "YOUR_BOT_TOKEN"
  chat_id: "YOUR_CHAT_ID"

---

## How to Run the Project

1. Data Ingestion
   Load the raw DTC data:
   python src/data_ingestion.py

2. Data Cleaning
   Clean and preprocess the data:
   python src/data_cleaning.py

3. Exploratory Data Analysis (EDA)
   Generate visualizations of the data:
   python src/eda_analysis.py

4. Model Training
   Train a machine learning model to predict DTC issues:
   python src/model_training.py

5. Send Alerts
   Monitor high-severity issues and send alerts:
   python src/alerts/telegram_alerts.py

6. Dashboard
   Launch the real-time dashboard:
   python src/dashboard.py

---

## Directory Structure

vehicle_dtc_project/
├── data/                             # Raw, cleaned, and processed data
├── models/                           # Trained ML models
├── logs/                             # Log files
├── config/                           # Configuration files
├── src/                              # Source code (ingestion, cleaning, EDA, etc.)
├── tests/                            # Unit tests
├── README.md                         # Project documentation

---

## Automating the Workflow

You can automate all the steps by creating a batch script (run_all.bat):

@echo off
python src/data_ingestion.py
python src/data_cleaning.py
python src/model_training.py
python src/alerts/telegram_alerts.py
python src/dashboard.py

---

## Conclusion

This project analyzes and predicts DTC issues for vehicles, provides real-time alerts via Telegram, and offers a dashboard for monitoring vehicle health.
