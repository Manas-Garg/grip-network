import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize Dash App
app = dash.Dash(__name__)

# Load Data
data = pd.read_csv("processed/processed_climate_data.csv")

# App Layout
app.layout = html.Div([
    html.H1("Climate Analytics Dashboard"),
    dcc.Dropdown(
        id="metric-selector",
        options=[
            {"label": "CO2 Levels", "value": "co2"},
            {"label": "Temperature", "value": "temperature"},
        ],
        value="co2"
    ),
    dcc.Graph(id="metric-graph")
])

# Callback to Update Graph
@app.callback(
    Output("metric-graph", "figure"),
    [Input("metric-selector", "value")]
)
def update_graph(selected_metric):
    fig = px.line(data, x="timestamp", y=selected_metric, title=f"{selected_metric.capitalize()} Over Time")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
