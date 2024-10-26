
# Vehicle Diagnostic Trouble Code (DTC) Analysis, Prediction, and Alert System

This project provides a full pipeline for analyzing, predicting, and sending alerts based on electric vehicle Diagnostic Trouble Codes (DTCs). The system includes:
- **Data ingestion** from raw files.
- **Data cleaning** and preprocessing.
- **Exploratory Data Analysis (EDA)** with visualizations.
- **Machine Learning model training** to predict future vehicle issues.
- **Real-time alerts** for high-severity issues via Telegram.
- A **dashboard** to monitor vehicle health and trends.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Configuration](#project-configuration)
- [How to Run the Project](#how-to-run-the-project)
- [Directory Structure](#directory-structure)
- [Automating the Workflow](#automating-the-workflow)

---

## Prerequisites

Before you start, ensure you have the following:
- **Python 3.x** installed.
- A **Telegram account** and a bot created (for alerts).
- Basic familiarity with Python, `pip`, and the command line.

---

## Installation

1. **Clone the Project Repository**:

   Download the project files to your local machine:

   \`\`\`bash
   git clone <your-repository-url>
   cd vehicle_dtc_project
   \`\`\`

2. **Install the Required Packages**:

   Install all dependencies using `pip`:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

---

## Project Configuration

### Telegram Bot Setup

For real-time alerts, you'll need to set up a Telegram bot and retrieve your chat ID:

1. **Create a Bot** using [BotFather](https://t.me/BotFather).
2. **Send a Message** to the bot.
3. **Retrieve Your Chat ID** using the Telegram API:  
   Replace \`<YOUR_BOT_TOKEN>\` in the URL below with your bot token:
   \`\`\`
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   \`\`\`
4. Copy the chat ID from the API response and configure it in the `config.yaml` file.

### Configure `config.yaml`:

Update the `config/config.yaml` file with your bot token and chat ID:

\`\`\`yaml
telegram:
  bot_token: "YOUR_TELEGRAM_BOT_TOKEN"
  chat_id: "YOUR_CHAT_ID"
\`\`\`

---

## How to Run the Project

### Step 1: Data Ingestion

Ingest the raw vehicle DTC data by running the following command:

\`\`\`bash
python src/data_ingestion.py
\`\`\`

The script will read the data from the `data/raw/` folder and prepare it for further processing.

### Step 2: Data Cleaning

Clean the ingested data by running:

\`\`\`bash
python src/data_cleaning.py
\`\`\`

The cleaned data will be saved in the `data/cleaned/` folder.

### Step 3: Exploratory Data Analysis (EDA)

Generate visualizations to explore the data by running:

\`\`\`bash
python src/eda_analysis.py
\`\`\`

Visualizations, including trends and severity levels, will be saved in the `data/processed/` folder.

### Step 4: Model Training

Train a machine learning model to predict future DTC occurrences:

\`\`\`bash
python src/model_training.py
\`\`\`

The trained model will be saved in the `models/` folder.

### Step 5: Real-Time Alerts

To start monitoring for critical DTC codes and receive real-time alerts via Telegram, run:

\`\`\`bash
python src/alerts/telegram_alerts.py
\`\`\`

### Step 6: Dashboard

Launch the dashboard to monitor vehicle health in real-time:

\`\`\`bash
python src/dashboard.py
\`\`\`

The dashboard will be available at \`http://127.0.0.1:8050/\`.

---

## Directory Structure

Here’s an overview of the project structure:

\`\`\`plaintext
vehicle_dtc_project/
│
├── data/                             # Data storage
│   ├── raw/                          # Raw input data
│   ├── cleaned/                      # Cleaned data
│   ├── processed/                    # Processed data and visualizations
├── models/                           # Trained ML models
├── logs/                             # Log files for monitoring progress
├── config/                           # Configuration files
├── src/                              # Source code
│   ├── data_ingestion.py             # Data ingestion script
│   ├── data_cleaning.py              # Data cleaning script
│   ├── eda_analysis.py               # Exploratory Data Analysis script
│   ├── model_training.py             # Model training script
│   ├── alerts/telegram_alerts.py      # Telegram alerting script
│   └── dashboard.py                  # Real-time dashboard
├── tests/                            # Unit tests
├── requirements.txt                  # Project dependencies
├── README.md                         # Project instructions
\`\`\`

---

## Automating the Workflow

You can automate all the steps (data ingestion, cleaning, model training, alerts, and the dashboard) by creating a batch script (\`run_all.bat\`):

\`\`\`plaintext
@echo off
python src/data_ingestion.py
python src/data_cleaning.py
python src/model_training.py
python src/alerts/telegram_alerts.py
python src/dashboard.py
\`\`\`

Run the script with:

\`\`\`bash
run_all.bat
\`\`\`

This will sequentially run all project components.

---

## Conclusion

This project provides a full workflow to analyze, predict, and alert based on vehicle DTC data. The real-time dashboard and Telegram alerts ensure that critical issues are reported promptly. Let me know if you encounter any issues or need further customization!
