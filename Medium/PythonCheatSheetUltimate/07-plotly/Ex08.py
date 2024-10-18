import plotly.graph_objs as go
import plotly.io as pio
import numpy as np


z = np.random.rand(20, 20)  # Generate random data
fig = go.Figure(data=go.Surface(z=z))
pio.show(fig)