import json
import datetime

from collections import namedtuple

from textwrap import dedent as d
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import numpy as np



# df = pd.read_csv(
#     ('https://raw.githubusercontent.com/plotly/'
#      'datasets/master/1962_2006_walmart_store_openings.csv'),
#     parse_dates=[1, 2],
#     infer_datetime_format=True
# )

# future_indices = df['OPENDATE'] > datetime.datetime(year=2050,month=1,day=1)
# df.loc[future_indices, 'OPENDATE'] -= datetime.timedelta(days=365.25*100)

df = pd.read_json('http://8732a407.ngrok.io/api/HealthMeasurement')
df['normal'] = np.random.normal(100, 5, df.shape[0])

# # in case of no data
# df = pd.DataFrame(np.random.normal(100, 5, 1000))
# df["ownerId"] = 'fake_user'
# df["heartRate"] = np.random.normal(60, 10, 1000)
# df["numberOfStepsInInterval"] = np.random.normal(200, 20, 1000)
# df["normal"] = np.random.normal(100, 5, 1000)

print(df.head())
print(df.shape)

owner_options = df["ownerId"].unique()

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
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
    dcc.Interval(
        id='interval-component',
        interval=10*1000, # in milliseconds
        n_intervals=0
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
    [dash.dependencies.Input('User', 'value'),
    #  Input('interval-component', 'n_intervals')
    ])
def update_graph(User, n_intervals=0):
    if n_intervals:
        _df = pd.read_json('http://8732a407.ngrok.io/api/HealthMeasurement')
        _df['normal'] = np.random.normal(100, 5, _df.shape[0])
        global df
        df = _df.copy()
        print("Just refreshed. New shape is " + str(df.shape[0]))

    if User is None or User == "All Users":
        df_new = df
    else:
        print("Filter for one user" + str(User))
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
                    'x': df_new['normal'],
                    'text': df_new['normal'],
                    'customdata': df_new['ownerId'],
                    'name': 'Normal',
                    'type': 'histogram'
                }
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

Highlight = namedtuple('highlight', ['start', 'end'])

def generate_highlight(data_array, highlight):
    return {
            'type': 'rect',
            'x0': np.percentile(data_array, highlight.start),
            'y0': 0,
            'x1': np.percentile(data_array, highlight.end),
            'y1': 100,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 10,
            }
        },




if __name__ == '__main__':
    app.run_server(debug=True)