# app.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/processed_data.csv")

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Global COVID-19 Dashboard"),
    dcc.Dropdown(id="country", options=[{"label": c, "value": c} for c in df['Country'].unique()],
                 value="India"),
    dcc.Graph(id="timeseries")
])

@app.callback(
    dash.dependencies.Output("timeseries", "figure"),
    [dash.dependencies.Input("country", "value")]
)
def update_graph(country):
    dff = df[df['Country'] == country]
    fig = px.line(dff, x="Date", y="7DayAvg", title=f"7-Day Avg New Cases - {country}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
