import plotly.graph_objs as go
import plotly.io as pio
import numpy as np


z = np.random.rand(10, 10)  # Generate random data
fig = go.Figure(data=go.Heatmap(z=z))
pio.show(fig)