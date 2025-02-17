import plotly.express as px # pip install plotly


data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])

fig = px.funnel(data, x='number', y='stage')

fig.show()