import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs.Scatter

new_data = Scatter(x=[3, 4], y=[3, 2] )
data = Data( [ new_data ] )
plot_url = py.plot(data, filename='extend plot', fileopt='extend')

