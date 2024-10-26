import dash
from dash import dcc, html
import pandas as pd

# Load cleaned data
df = pd.read_csv('./data/cleaned/cleaned_vehicle_dtc_data.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Group by month and calculate average severity level for each month
df['month'] = df['timestamp'].dt.to_period('M')
severity_trend = df.groupby('month')['severity_level'].mean()

# Initialize the dashboard app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Vehicle Fleet Health Dashboard'),

    # Line plot for average severity over time
    dcc.Graph(
        id='severity-trend',
        figure={
            'data': [{'x': severity_trend.index.astype(str), 'y': severity_trend.values, 'type': 'line', 'name': 'Severity'}],
            'layout': {
                'title': 'Average Severity Trend Over Time',
                'xaxis': {'title': 'Month'},
                'yaxis': {'title': 'Average Severity Level'},
            }
        }
    ),

    # Scatter plot for individual severity events
    dcc.Graph(
        id='severity-scatter',
        figure={
            'data': [{'x': df['timestamp'], 'y': df['severity_level'], 'mode': 'markers', 'name': 'Severity'}],
            'layout': {
                'title': 'Severity Levels Over Time (Scatter Plot)',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Severity Level'},
            }
        }
    )
])

# Run the dashboard server
if __name__ == '__main__':
    app.run_server(debug=True)
