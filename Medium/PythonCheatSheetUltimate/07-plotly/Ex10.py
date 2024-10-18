import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio


dates = pd.date_range('20230101', periods=5)
values = [10, 11, 12, 13, 14]
fig = go.Figure(data=go.Scatter(x=dates, y=values, mode='lines+markers'))
pio.show(fig)