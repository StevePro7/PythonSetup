import plotly.graph_objs as go
import plotly.io as pio

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

labels = ['Earth', 'Water', 'Fire', 'Air']
sizes = [25, 35, 20, 20]
fig = go.Figure(data=go.Pie(labels=labels, values=sizes))
pio.show(fig)