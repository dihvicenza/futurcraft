# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Competenza": ["IoT", "3D printing", "Cloud Computing", "IoT", "3D printing", "Cloud Computing"],
    "Quantità": [4, 1, 2, 2, 4, 5],
    "Provincia": ["Vicenza", "Vicenza", "Vicenza", "Bolzano", "Treviso", "Salisburgo"]
})

fig = px.bar(df, x="Competenza", y="Quantità", color="Provincia", barmode="group")

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