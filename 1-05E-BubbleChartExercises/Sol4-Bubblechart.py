#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter( # make a scatter plot
    x=df['displacement'],
    y=df['acceleration'],
    text=df['name'], # set x and y
    mode='markers', # first set mode to markers
    marker=dict(size=df['weight']/500) # change marker size
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Vehicle acceleration vs. displacement',
    xaxis = dict(title = 'displacement'),
    yaxis = dict(title = 'acceleration = seconds to reach 60mph'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution4.html')
#######
# So what happened?? Why is the trend sloping downward?
# Remember that acceleration is the number of seconds to go from 0 to 60mph,
# so fewer seconds means faster acceleration!
######
