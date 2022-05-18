#######
# A very basic Input/Output callback.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in', # choose a number in the input
        value=1,
        style={'fontSize':28}
    ),
    html.H1(id='number-out') # h1 tag assigned to number-out id # select it
])

@app.callback(
    Output('number-out', 'children'), # output with number-out id
    [Input('number-in', 'value')])
def output(number):
    return number

if __name__ == '__main__':
    app.run_server()
