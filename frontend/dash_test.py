# -*- coding: utf-8 -*-
from os.path import expanduser
import os

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
df = pd.read_sql_table('selfi4_group', con, schema='futurecraft')

# WEB APP
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig = px.density_heatmap(df,
                         labels={"tecnologia": "Tecnologia", "provincia": "Provincia", "count": "Risposte"},
                         hover_name="count",
                         # color_continuous_scale=["#ff0100", "#ff9c00", "#f6ea00", "#54bf02", "#017b01"],
                         x=df['provincia'],
                         y=df['tecnologia'],
                         z=df['count'])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(children='FutureCRAFT WP4'),
    html.Img(src=app.get_asset_url('interreg.png')),
    html.Div(children="Domanda di competenze da parte delle imprese",
             style={'textAlign': 'center', 'font-weight': 'bold', }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children="""
    L’iniziativa FuturCRAFT avrà il compito di definire i possibili scenari futuri per i profili di competenza digitale nell’artigianato e di illustrare le opportunità di digitalizzazione disponibili per le aziende artigiane.
    """, style={'font-weight': 'bold'}),

    html.Div(children="""
    Con il supporto di svariate ricerche ed analisi verrà esaminata l’attuale offerta formativa: un’indagine Delphi ed alcune discussioni tra esperti mostreranno l’influenza della digitalizzazione sui mestieri artigiani, si effettueranno delle visite in realtà artigiane ed in generale si prenderà contatto più da vicino con la realtà dell’artigianato.
    """),

    html.Div(children="""
    Sulla base dei risultati si cercherà di sviluppare delle strategie di digitalizzazione utili per sostenere le aziende nella propria attività di innovazione.
    """),

    html.Div(children="""
    Il progetto mira a creare una conoscenza di base per lo sviluppo futuro dei mestieri artigiani, ma anche a mostrare concretamente come qualificarsi nel mondo del lavoro digitale.
    """),

    html.Div(children="""
    Il progetto FuturCRAFT è sostenuto dal Fondo Europeo di Sviluppo Regionale e da Interreg V-A Italia-Austria 2014-2020.
    """)
])

if __name__ == '__main__':
    app.run_server(debug=True)
