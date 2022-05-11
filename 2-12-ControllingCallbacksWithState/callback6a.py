#######
# A very basic Input/Output callback, with State!
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize':28}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize':28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    [Input('submit-button', 'n_clicks')], # add button as input # input is action of clicking button
    [State('number-in', 'value')]) # add state value # input value is stored in state
def output(n_clicks, number):
    return number

if __name__ == '__main__':
    app.run_server()
