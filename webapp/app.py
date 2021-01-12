# -*- coding: utf-8 -*-
from os.path import expanduser

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine


# DATA
# Get connection parameters
with open(expanduser('~/.pgpass'), 'r') as f:
    for i, line in enumerate(f):
        line = line[:-1]
        if i == 0:  #  number of the line with DB credentials
            host, port, db, user, password = line.split(':')

# SQLAlchemy connectable
# Scheme: "postgresql://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
db_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
con = create_engine(db_uri).connect()

# Table named 'selfi4' will be returned as a dataframe.
df = pd.read_sql_table('selfi4_group', con, schema='futurcraft')

tech_top5 = ["Sistema gestionale", "Cloud", "Cybersicurezza e business continuity",
             "Sistemi di pagamento mobile e/o via Internet", "Sistemi di e-commerce e/o e-trade"]

# WEB APP

app = dash.Dash(title='FuturCRAFT WP4')

colors = {
    'background': '#31302f',
    'text': '#fff',
    'title': '#fdcc0d'
}

fig = px.density_heatmap(df,
                         labels={"tecnologia_fcraft": "Tecnologia", "provincia": "Provincia", "count": "Risposte"},
                         x=df['provincia'],
                         y=df['tecnologia_fcraft'],
                         z=df['count'])

fig.update_layout(
    legend_title="Risposte SELFI4.0",
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.Div(className='row', children=[
        html.Div(className='four columns div-user-controls', children=[
            html.Img(src=app.get_asset_url('interreg-bianco.png'),
                     alt="INTERREG. L'iniziativa FuturCRAFT - \
                     Rafforzamento della ricerca, dello sviluppo tecnologico e dell'innovazione",
                     style={"display": "block",
                            "margin-left": "auto",
                            "margin-right": "auto",
                            "width": "80%",
                            "max-width": "300px",
                            "margin-bottom": "20px"}),
            html.H1('FutureCRAFT WP4', style={"font-size": "250%", "color": colors['title']}),
            html.P("""
                L’iniziativa FuturCRAFT avrà il compito di definire i possibili scenari futuri per i profili \
                di competenza digitale nell’artigianato e di illustrare le opportunità di digitalizzazione \
                disponibili per le aziende artigiane."""),
            html.P("""
                Con il supporto di svariate ricerche ed analisi verrà esaminata l’attuale offerta formativa: \
                un’indagine Delphi ed alcune discussioni tra esperti mostreranno l’influenza della digitalizzazione \
                sui mestieri artigiani, si effettueranno delle visite in realtà artigiane ed in generale si prenderà \
                contatto più da vicino con la realtà dell’artigianato."""),
            html.P("""
                Sulla base dei risultati si cercherà di sviluppare delle strategie di digitalizzazione utili per \
                sostenere le aziende nella propria attività di innovazione."""),
            html.P(['Developed by: ',
                      html.A('Digital Innovation Hub Vicenza',
                             href='https://digitalinnovationhubvicenza.it/',
                             target="_blank")], style={"margin-top": "15px"})
        ]),
        html.Div(className='eight columns div-for-charts bg-grey', children=[
            html.H2("Domanda di competenze da parte delle imprese", style={"text-align": "center"}),
            dcc.Graph(
                id='fcraft-wp4',
                figure=fig,
                style={"margin-left": "50px"}
            ),
            html.P("Top 5 delle tecnologie richieste:", style={"font-size": "120%", "margin-left": "50px"}),
            html.Ol(id='tech-top5', children=[html.Li(tech) for tech in tech_top5], style={"margin-left": "50px"})
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
