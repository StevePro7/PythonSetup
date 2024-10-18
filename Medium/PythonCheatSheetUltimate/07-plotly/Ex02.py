import plotly.graph_objs as go
import plotly.io as pio

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
pio.show(fig)