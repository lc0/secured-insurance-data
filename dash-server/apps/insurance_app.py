import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

from app import app

df = pd.read_json('http://8732a407.ngrok.io/api/HealthMeasurement')
df['normal'] = np.random.normal(100, 5, df.shape[0])

owner_options = df["ownerId"].unique()

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                # {
                #     'x': df['OPENDATE'],
                #     'text': df['STRCITY'],
                #     'customdata': df['storenum'],
                #     'name': 'Open Date',
                #     'type': 'histogram'
                # },
                # {
                #     'x': df['date_super'],
                #     'text': df['STRCITY'],
                #     'customdata': df['storenum'],
                #     'name': 'Super Date',
                #     'type': 'histogram'
                # }
            ],
            'layout': {}
        }
    ),

    html.Div(className='row', children=[
        dcc.Dropdown(
                id="User",
                options=[{
                    'label': 'user #' + str(i),
                    'value': i
                } for i in owner_options],
                value='All Users')
    ])
])

@app.callback(
    dash.dependencies.Output('basic-interactions', 'figure'),
    [dash.dependencies.Input('User', 'value')])
def update_graph(User):
    if User == "All Users":
        df_new = df.copy()
    else:
        df_new = df[df['ownerId'] == User]

    return {'data': [
                {
                    'x': df_new['heartRate'],
                    'text': df_new['heartRate'],
                    'customdata': df_new['ownerId'],
                    'name': 'Heart rate',
                    'type': 'histogram'
                },
                {
                    'x': df_new['numberOfStepsInInterval'],
                    'text': df_new['numberOfStepsInInterval'],
                    'customdata': df_new['ownerId'],
                    'name': 'Number of Steps',
                    'type': 'histogram'
                },
                {
                    'x': df['normal'],
                    'text': df['normal'],
                    'customdata': df['ownerId'],
                    'name': 'Normal',
                    'type': 'histogram'
                },
    ]}



