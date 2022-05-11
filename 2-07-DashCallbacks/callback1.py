import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'), # input box (dash core component(dcc))
    html.Div(id='my-div') # div under input box (html component)
])

@app.callback(
    Output(component_id='my-div', component_property='children'), # set html my-div output to be children property
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()
