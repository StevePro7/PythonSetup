import plotly.graph_objs as go
import plotly.io as pio

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 30, 25]
fig = go.Figure(data=go.Bar(x=categories, y=values))
pio.show(fig)