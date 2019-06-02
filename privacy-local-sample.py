import plotly 
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

plotly.__version__ # plot.ly versioning

# privacy setting. do not remove or data will be available to public
plotly.tools.set_config_file(world_readable=False, sharing='private')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

fig = {
    'data': [
          {
          'x': df.gdpPercap, 
            'y': df.lifeExp, 
            'text': df.country, 
            'mode': 'markers', 
            'name': '2007'},
    ],
    'layout': {
        'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        'yaxis': {'title': "Life Expectancy"}
    }
}


url = plot(fig, filename='charts/pandas-multiple-scatter.html')


