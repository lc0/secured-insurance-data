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

    html.H1('Insurance cockpit', style={'color': 'black', 'fontSize': 25, 'centered':True}),

    html.Div([
        html.Img(src='../assets/swiss-re-logo.png', width=150, height=150),
        html.P('Dashboard containg overview of user data'),
    ]),
    html.Div(className='row', children=[
        dcc.Dropdown(
                id="User",
                options=[{
                    'label': 'user #' + str(i),
                    'value': i
                } for i in owner_options],
                value='All Users')
    ]),
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
    )
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
            ],
            'layout': {
                'shapes': [
                    generate_border(df_new['normal'], 10, color='rgb(55, 128, 191)'),
                    generate_border(df_new['normal'], 90, color='rgb(55, 128, 191)'),
                    generate_border(df_new['heartRate'], 10, color='rgb(50, 171, 96)'),
                    generate_border(df_new['heartRate'], 90, color='rgb(50, 171, 96)'),
                    generate_border(df_new['numberOfStepsInInterval'], 10, color='rgb(128, 0, 128)'),
                    generate_border(df_new['numberOfStepsInInterval'], 90, color='rgb(128, 0, 128)'),
            ]}
    }

def generate_border(data_array, percentile, color):
    return {
                'type': 'line',
                'x0': np.percentile(data_array, percentile),
                'y0': 0,
                'x1': np.percentile(data_array, percentile),
                'y1': 100,
                'line': {
                    'color': color,
                    'width': 4,
                    'dash': 'dot'
                },
                'name': f"{percentile}th percentile"
            }



