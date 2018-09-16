from collections import defaultdict

import dash_html_components as html
import requests

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def get_data_of_count_words():
    r = getImageCategories()
    headers = r['headers']
    counts = r['counts']

    return [{'x': headers, 'y': counts, 'type': 'bar', 'name': 'Most popular words'}]

def get_clients():
    r = requests.get('http://localhost:3000/api/InsuredClient')

    clients = []
    for client in r.json():
        clients.append((client['id'], client['name']))

    return clients

def getImageCategories():
    r = requests.get('http://localhost:3000/api/PictureMeasurement')
    pictures = r.json()

    pics = []
    for j in pictures:
        pics.append(str(j['predictors'][0]['key']))

    appearances = defaultdict(int)

    for curr in pics:
        appearances[curr] += 1

    app_dict = dict(appearances)
    list_headers=[]
    list_counts=[]

    for k,v in app_dict.items():
        list_headers.append(k)
        list_counts.append(v)

    return {'headers':list_headers,
        'counts':list_counts}

COLORS = [{
'text': '#008000'},
{'text': '#040404'},
{'text': '#f41111'}]

def t_style(value):
    style = {
        'color': COLORS[1]['text']
    }
    return style

def sy_style(value):
    if value <= 0:
        style = {
            'color': COLORS[0]['text']
        }
    elif value == 0:
        style = {
            'color': COLORS[1]['text']
        }
    else:
        style = {
            'color': COLORS[2]['text']
        }
    return style

def text_style(valued):
    style = {}

    value = float(valued)
    if value > 0:
        style = {
            'color': COLORS[0]['text']
        }
    elif value == 0:
        style = {
            'color': COLORS[1]['text']
        }
    elif value < 0:
        style = {
            'color': COLORS[2]['text']
        }
    return style

# reusable componenets
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))], className="reaponsive-table"
    )