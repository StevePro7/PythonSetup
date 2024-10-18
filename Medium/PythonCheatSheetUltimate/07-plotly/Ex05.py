import plotly.graph_objs as go
import plotly.io as pio


data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
fig = go.Figure(data=go.Histogram(x=data))
pio.show(fig)