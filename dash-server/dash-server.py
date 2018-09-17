import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
from utils import get_clients, get_data_of_count_words
import plotly.graph_objs as go

app = dash.Dash()

user_df = pd.read_json('http://localhost:3000/api/HealthMeasurement')
#user_df = df.sample(frac=0.8, random_state=42)
owner_options = user_df["ownerId"].unique()
clients = get_clients()

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
        dcc.Dropdown(
            id='user-dropdown',
            options=[{'label': i[1], 'value': i[0]} for i in clients],
            value=clients[0][0]
        ),
    html.Div([
        html.Div([
            html.H3('Heart rate'),
            dcc.Graph(
        id='user-indicator-scatter',
        figure={
            'data': [
                go.Scatter(
                    x=user_df[user_df['ownerId'] == i]['datetimeBeginStepsInterval'],
                    y=user_df[user_df['ownerId'] == i]['heartRate'],
                    #text=user_df[user_df['ownerId'] == i]['ownerId'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                ) for i in user_df.ownerId.unique()
            ],
            'layout': {
                'title': '',
                'showlegend': True
            }
        }
    ),
        ], className="six columns",
        style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}
        ),
        html.Div([
            html.H3('Most common words  '),
            dcc.Graph(
        id='example-graph2',
        figure={
            'data': get_data_of_count_words(),
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
        ], className="six columns", 
        style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}
        ),
    ], className="row")
])


@app.callback(
    dash.dependencies.Output('user-indicator-scatter', 'figure'),
    [
    dash.dependencies.Input('user-dropdown', 'value'),
    ])
def update_graph(owner_id):
    print('owner_id %s' %str(owner_id))

    owner_id = int(owner_id)
    user_df_updated = user_df[user_df['ownerId'] == owner_id]

    return {
            'data': [
                go.Scatter(
                    x=user_df_updated[user_df_updated['ownerId'] == owner_id]['datetimeBeginStepsInterval'],
                    y=user_df_updated[user_df_updated['ownerId'] == owner_id]['heartRate'],
                    #text=user_df_updated[user_df_updated['ownerId'] == owner_id]['ownerId'],
                    mode='lines+markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=owner_id
                )
            ],
            'layout': {
                'title': '',
                'showlegend': True,
                'xaxis':{
                    'title':'Time of measurement'
                },
                'yaxis':{
                     'title':'Heart rate'
                }

            }
        }



if __name__ == '__main__':
    app.run_server(debug=True)