import pandas as pd
from datetime import datetime
import plotly.graph_objs as go

# preserve privacy!
import plotly.tools
from plotly.offline import download_plotlyjs, plot
plotly.tools.set_config_file(world_readable=False, sharing='private')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]
plot(data, filename='charts/simple_candlestick.html')
