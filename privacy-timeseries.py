import plotly.tools
import plotly.graph_objs as go
import pandas as pd

# preserve privacy!
from plotly.offline import download_plotlyjs, plot
plotly.tools.set_config_file(world_readable=False, sharing='private')


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
data = [go.Scatter( x=df['Date'], y=df['AAPL.Close'] )]

plot(data, filename='charts/pandas-time-series.html')


