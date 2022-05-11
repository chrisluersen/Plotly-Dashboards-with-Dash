#######
# This uses a small wheels.csv dataset
# to demonstrate multiple outputs.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div([
    dcc.RadioItems( # button list
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()], # show i, give's i data # grab all unique values from wheels column
        value=1
    ),
    html.Div(id='wheels-output'),

    html.Hr(),  # add a horizontal rule
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output')
], style={'fontFamily':'helvetica', 'fontSize':18}) # optional options...

@app.callback(
    Output('wheels-output', 'children'), # component id and children makes it under input
    [Input('wheels', 'value')]) # put value as wheels_value in callback_a
def callback_a(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)

@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def callback_b(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

if __name__ == '__main__':
    app.run_server()
