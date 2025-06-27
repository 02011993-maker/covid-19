import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Global COVID-19 Dashboard"),
    dcc.Dropdown(
        id='country',
        options=[{'label': c, 'value': c} for c in df['Country'].unique()],
        value='India'
    ),
    dcc.Graph(id='covid-trend', config={'responsive': True})
])

@app.callback(
    dash.dependencies.Output('covid-trend', 'figure'),
    [dash.dependencies.Input('country', 'value')]
)
def update_graph(selected_country):
    dff = df[df['Country'] == selected_country].sort_values('Date')
    fig = px.line(dff, x='Date', y='TotalConfirmed',
                  title=f"COVID-19 Cases in {selected_country}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
