import numpy as np
# original source : https://plot.ly/python/sliders/

data = [dict(
        visible = False,
        line=dict(color='#00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = np.arange(0,10,0.01),
        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

steps = []
for i in range(len(data)):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Frequency: "},
    pad = {"t": 50},
    steps = steps
)]

layout = dict(sliders=sliders)
fig = dict(data=data, layout=layout)

''' public data '''
#import plotly.plotly as py
#py.plot(fig, filename='Sine Wave Slider', world_readable=True)

''' preserve privacy!'''
import plotly.tools
from plotly.offline import download_plotlyjs, plot
plotly.tools.set_config_file(world_readable=False, sharing='private')

plot(fig, filename='charts/Sine-Wave-Slider.html')
