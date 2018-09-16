import os

import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output

from app import app, server
from apps import insurance_app, user_app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

STATIC_PREFIX = '/dash-server/templates/'

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return insurance_app.layout
    elif pathname == '/apps/app2':
         return user_app.layout
    else:
        # TODO - return logo
        return html.Div([
            html.H1('Page not available!')
])


if __name__ == '__main__':
    app.run_server(debug=True)