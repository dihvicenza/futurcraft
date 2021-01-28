# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

from tools import *
import multilingual_content as ml

# DATABASE CONNECTION
HOST, PORT, DB, USER, PASSWORD = db_credentials()
db_uri = f'postgresql+pg8000://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'  # pg8000==1.16.5 is important
con = create_engine(db_uri, pool_pre_ping=True, pool_recycle=3600).connect()

# Table named 'selfi4' will be returned as a dataframe.
df = pd.read_sql_table('selfi4_group', con, schema='data')

tech_top5 = ["Sistema gestionale", "Cloud", "Cybersicurezza e business continuity",
             "Sistemi di pagamento mobile e/o via Internet", "Sistemi di e-commerce e/o e-trade"]

# WEB APP
lng = "it"
app = dash.Dash(name=__name__,
                title="FuturCRAFT",
                assets_folder="static",
                assets_url_path="static")
application = app.server

fig = px.density_heatmap(df,
                         labels={'tecnologia_fcraft': 'Competenza',
                                 'provincia': 'Provincia',
                                 'percento': 'Percentuale'},
                         x=df['provincia'],
                         y=df['tecnologia_fcraft'],
                         z=df['percento'],
                         color_continuous_scale=["#fff", "#fdcc0d"])

fig.add_trace(go.Scatter(x=df['provincia'],
                         y=df['tecnologia_fcraft'],
                         mode='markers',
                         marker=dict(size=np.where(df['formazione'], 10, 0),
                                     color="black",
                                     line=dict(width=2, color="black"),
                                     symbol='x-thin'),
                         hoverinfo='skip'))

app.layout = html.Div([
    html.H1(id="h1"),

    html.Div(className='row', children=[

        html.Div(className='four columns div-user-controls', children=[

            html.Img(className="logo", src=app.get_asset_url("interreg.png"), alt="Logo: INTERREG FuturCRAFT"),

            html.Div(className="div-for-dropdown",
                     children=[dcc.Dropdown(id="lang-selector",
                                            value="en",
                                            clearable=False,
                                            options=[{"label": "English", "value": "en"},
                                                     {"label": "italiano", "value": "it"},
                                                     {"label": "Deutsch", "value": "de"}
                                                     ]
                                            )
                               ],
                     ),
            html.Div(id="p_desc"),
            dcc.Markdown(id="p_read_more"),
            dcc.Markdown(id="p_dev_by"),
            dcc.Markdown(id="h2_ref")
        ]),

        html.Div(className='eight columns div-for-charts',
                 children=[dcc.Graph(id="fcraft-wp4",
                                     figure=fig,
                                     style={"margin-left": "50px"},
                                     config={"displayModeBar": False, "scrollZoom": False}),
            html.P("Top 5 delle tecnologie richieste:", style={"font-size": "120%", "margin-left": "50px"}),
            html.Ol(id='tech-top5', children=[html.Li(tech) for tech in tech_top5], style={"margin-left": "50px"})
        ])
    ])
])


@app.callback(
    [Output("h1", "children"),
     Output("p_desc", "children"),
     Output("h2_ref", "children")],
     Output("p_read_more", "children"),
    Output("p_dev_by", "children"),
    [Input("lang-selector", "value")])
def multi_output(value):
    return ml.h1[value], \
           ml.p_desc[value], \
           ml.h2_ref[value], \
           ml.p_read_more[value], \
           ml.p_dev_by[value]


if __name__ == '__main__':
    application.run(debug=True, port=80)
