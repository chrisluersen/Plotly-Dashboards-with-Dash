#######
# This histogram looks back at the mpg dataset
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

# categorical feature = bar chart
# continous feature = historam
data = [go.Histogram(
    x=df['mpg'] # only need one continous feature
)]

layout = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='basic_histogram.html')
