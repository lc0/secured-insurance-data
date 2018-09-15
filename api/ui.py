import json
from textwrap import dedent as d
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime

# df = pd.read_csv(
#     ('https://raw.githubusercontent.com/plotly/'
#      'datasets/master/1962_2006_walmart_store_openings.csv'),
#     parse_dates=[1, 2],
#     infer_datetime_format=True
# )

# future_indices = df['OPENDATE'] > datetime.datetime(year=2050,month=1,day=1)
# df.loc[future_indices, 'OPENDATE'] -= datetime.timedelta(days=365.25*100)

df = pd.read_json('http://8732a407.ngrok.io/api/HealthMeasurement')
print(df.head())

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
                {
                    'x': df['heartRate'],
                    'text': df['heartRate'],
                    'customdata': df['ownerId'],
                    'name': 'Heart rate',
                    'type': 'histogram'
                },
                {
                    'x': df['numberOfStepsInInterval'],
                    'text': df['numberOfStepsInInterval'],
                    'customdata': df['ownerId'],
                    'name': 'Number of Steps',
                    'type': 'histogram'
                },
                # {
                #     'x': df['datetimeBeginStepsInterval'],
                #     'text': df['numberOfStepsInInterval'],
                #     'customdata': df['numberOfStepsInInterval'],
                #     'name': 'Steps',
                #     'type': 'bar'
                # },
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
    ]}




if __name__ == '__main__':
    app.run_server(debug=True)