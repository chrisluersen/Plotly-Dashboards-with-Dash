#######
# Here we'll use the mpg.csv dataset to demonstrate
# how multiple inputs can affect the same graph.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')

# ['mpg','hp','displace']
features = df.columns # just a list of the actual columns

app.layout = html.Div([ # as always set up div

        html.Div([ # first drop down
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i.title(), 'value': i} for i in features], # i is column name
                value='displacement'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}), # style dict so dropdowns dont overlap 48% give 4% space between two #inline-block makes them appear next to eachother

        html.Div([ # second drop down
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='acceleration'
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='feature-graphic') # graph
], style={'padding':10}) # put some space between each component

@app.callback(
    Output('feature-graphic', 'figure'), # id is called feature-graph, value we're messing with is the figure
    [Input('xaxis', 'value'), # id of first dropdown
     Input('yaxis', 'value')]) # id of second dropdown
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'], # name of car itself on hover
            mode='markers', # make scatter plot and not line plot
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()
