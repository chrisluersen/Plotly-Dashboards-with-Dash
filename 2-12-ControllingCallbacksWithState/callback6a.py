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
        style={'fontSize': 28}
    ),
    html.Button( # add button for controlling callback with state
        id='submit-button',
        n_clicks=0, # don't need to count number of clicks
        children='Submit', # text displayed in button
        style={'fontSize': 28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    # add button as input # input is action of clicking button
    [Input('submit-button', 'n_clicks')], # connect to submit button
    [State('number-in', 'value')])  # add state value # input value is stored in state # stuff in between input to output
def output(n_clicks, number): # once clicked return the number
    return number


if __name__ == '__main__':
    app.run_server()
