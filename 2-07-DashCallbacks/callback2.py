import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/gapminderDataFiveYear.csv')

app = dash.Dash()


# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
year_options = []
for year in df['year'].unique(): # don't repeat years in list
    year_options.append({'label':str(year),'value':year}) # use dict set label for list to be the year as a string but still use the actual value as a int

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',options=year_options,value=df['year'].min()) # use year_options list for drop down, set default to min year
])

# connect input of dropdown menu to output of graph
@app.callback(Output('graph', 'figure'), # connect compent id graph to component property
              [Input('year-picker', 'value')]) # grab the year_picker list and grab value from that list
def update_figure(selected_year): # connect dropdown to actual figure
    
    # data only for selected year from dopdown
    filtered_df = df[df['year'] == selected_year]
    traces = []
    for continent_name in filtered_df['continent'].unique(): # filter through already filtered_df for unique continent names
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name] # first filter by year now filter by continent
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            # style
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=continent_name
        ))

    return { # return dict to go in graph call
        'data': traces, # use traces list above
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            hovermode='closest'
        )
    }

if __name__ == '__main__': # always add
    app.run_server()
