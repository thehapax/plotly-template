import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime
import plotly.graph_objs as go

# preserve privacy!
import plotly.tools
plotly.tools.set_config_file(world_readable=False, sharing='private')
# end preserve privacy!

# see original source guide here at: https://plot.ly/python/ohlc-charts/

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello, AAPL Stock Dash Demo'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                trace
            ],
            'layout': go.Layout(
                xaxis= dict(rangeslider = dict(visible=True)),
                yaxis={'title': 'USD'},
                hovermode='closest'
            )
        }            
    )   
])


if __name__ == '__main__':
    app.run_server(debug=True)
