#######
# This makes a 3x3 scatterplot of wheels.csv, and sends
# the result of hover to the screen as a JSON object.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest' # when cursor is closest to scatterpoint that's the info were's
            )
        }
    )], style={'width':'30%', 'float':'left'}),

    html.Div([
    html.Pre(id='hover-data', style={'paddingTop':35}) # where to put the hover data
    ], style={'width':'30%'})
])

@app.callback(
    Output('hover-data', 'children'), # set hover-data to op
    [Input('wheels-plot', 'hoverData')]) # hoverData is from documentation hoverData is a string you can't change for plotly to recoginize it
def callback_image(hoverData):
    return json.dumps(hoverData, indent=2)

if __name__ == '__main__':
    app.run_server()
