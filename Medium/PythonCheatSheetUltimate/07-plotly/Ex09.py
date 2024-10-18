import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 30, 25]

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines'), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values), row=1, col=2)
pio.show(fig)