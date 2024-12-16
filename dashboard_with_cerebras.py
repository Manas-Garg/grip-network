import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Initialize Dash App
app = dash.Dash(__name__)

# Load Data
data = pd.read_csv("processed/processed_climate_data.csv")

# Cerebras API Configuration
CEREBRAS_API_URL = "https://api.cerebras.ai/v1/generate"
CEREBRAS_HEADERS = {
    "Authorization": "Bearer csk-w9kx62etv68c9rkdt382f3dc8vnmerrtr8ewxf55vyd4en29",
    "Content-Type": "application/json"
}

# Layout
def layout():
    return html.Div([
        html.H1("Cerebras-Powered Climate Dashboard"),
        dcc.Dropdown(
            id="metric-selector",
            options=[
                {"label": "CO2 Levels", "value": "co2"},
                {"label": "Temperature", "value": "temperature"},
            ],
            value="co2"
        ),
        dcc.Graph(id="metric-graph"),
        html.Button("Get Recommendation", id="recommendation-button", n_clicks=0),
        html.Div(id="recommendation-output")
    ])

app.layout = layout

@app.callback(
    Output("metric-graph", "figure"),
    [Input("metric-selector", "value")]
)
def update_graph(selected_metric):
    fig = px.line(data, x="timestamp", y=selected_metric, title=f"{selected_metric.capitalize()} Over Time")
    return fig

@app.callback(
    Output("recommendation-output", "children"),
    [Input("recommendation-button", "n_clicks")]
)
def generate_recommendation(n_clicks):
    if n_clicks > 0:
        prompt = "Analyze current climate data and recommend interventions."
        payload = {
            "model": "llama3.1-70b",
            "prompt": prompt,
            "max_tokens": 100
        }
        response = requests.post(CEREBRAS_API_URL, headers=CEREBRAS_HEADERS, json=payload)
        return response.json()["choices"][0]["text"]

if __name__ == "__main__":
    app.run_server(debug=True)
