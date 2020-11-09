# -*- coding: utf-8 -*-
from os.path import expanduser

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd

# DATA
# Get connection parameters
with open(expanduser('~/.pgpass'), 'r') as f:
    for i, line in enumerate(f):
        if i == 3:
            host, port, db, user, password = line.split(':')

# SQLAlchemy connectable
# Scheme: "postgresql://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
db_uri = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'
con = create_engine(db_uri).connect()

# Table named 'selfi4' will be returned as a dataframe.
df = pd.read_sql_table('selfi4', con, schema='futurecraft')

# WEB APP
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df_gr = df.groupby('settore')
fig = px.bar(df, x='settore')

app.layout = html.Div(children=[
    html.H1(children='Competenze FutureCRAFT'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
