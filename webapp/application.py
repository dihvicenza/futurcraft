# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
from sqlalchemy import create_engine

from tools import *
import multilingual_content as ml

# DATABASE CONNECTION
HOST, PORT, DB, USER, PASSWORD = db_credentials()
db_uri = f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"  # pg8000==1.16.5 is important
con = create_engine(db_uri, pool_pre_ping=True, pool_recycle=3600).connect()

# Table named 'selfi4' will be returned as a dataframe.
df = pd.read_sql_table("selfi4_group", con, schema="data")

# WEB APP
lng = "it"
app = dash.Dash(name=__name__,
                title="FuturCRAFT",
                meta_tags=[
                        # A description for search engines
                        {
                                "name": "description",
                                "content": "FuturCRAFT: Future competence profiles in training and specialization"
                        },
                        # For IE, use the latest renderer available (e.g. Edge)
                        {
                                "http-equiv": "X-UA-Compatible",
                                "content": "IE=edge"
                        },
                        # A tag necessary for "true" mobile support.
                        {
                                "name": "viewport",
                                "content": "width=device-width, initial-scale=1.0"
                        }
                ],
                assets_folder="static",
                assets_url_path="static")
application = app.server

# https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Heatmap.html
fig = go.Figure(data=go.Heatmap(
    name="Enterprises",
    showlegend=True,
    x=df["provincia"],
    y=df["tecnologia_fcraft"],
    z=df["percento"],
    text=df['formazione'],
    hovertemplate="<i>Province</i>: <b>%{x}</b><br>" +
                  "<i>Competence</i>: <b>%{y}</b><br>" +
                  "<i>Pct. of companies</i>: <b>%{z}%</b><br>" +
                  "<i>Number of schools</i>: <b>%{text}</b>",
    xgap=0.5,
    ygap=0.5,
    colorscale=["#fff", "#fdcc0d"],
    colorbar=dict(
        title="Prevalence",
        titleside="top",
        tickmode="array",
        tickvals=[1, 8, 15],
        ticktext=["Low", "Average", "High"],
        ticks="outside"
    )),
    layout=go.Layout(legend=dict(orientation="h"),
                     hoverlabel=dict(namelength=0)
                     )
)

fig.add_trace(go.Scatter(
    name="Schools",
    showlegend=True,
    x=df["provincia"],
    y=df["tecnologia_fcraft"],
    mode="markers",
    marker=dict(size=df["formazione"] ** 2 / 10,  # size=np.where(df['formazione'], 10, 0
                color="#164193",
                line=dict(width=2, color="#164193"),
                symbol="square"),
    hoverinfo="skip",
    hoverlabel=dict(namelength=0)
))

fig.update_layout(dragmode=False,
                  separators=",")

app.layout = html.Div([
    html.H1(id="h1"),

    html.Div(className="row", children=[

        html.Div(className="four columns div-user-controls", children=[

            html.Img(className="logo", src=app.get_asset_url("interreg.png"), alt="Logo: INTERREG FuturCRAFT"),

            html.Div(className="div-for-dropdown",
                     children=[dcc.Dropdown(id="lang-selector",
                                            value="en",
                                            clearable=False,
                                            options=[{"label": "English", "value": "en"},
                                                     {"label": "Italiano", "value": "it"},
                                                     {"label": "Deutsch", "value": "de"}]
                                            )
                               ],
                     ),
            dcc.Markdown(id="p_desc")
        ]),

        html.Div(className="eight columns div-for-charts",
                 children=[
                     dcc.Tabs([
                                dcc.Tab(label="TV+BL, BZ, VI", children=[
                                dcc.Graph(id="fcraft-wp4-ita",
                                          figure=fig,
                                          style={"margin-left": "50px"},
                                          config={"displayModeBar": False, "scrollZoom": False}),
                                dcc.Markdown(id="interpr")
                                ]),
                                dcc.Tab(label="SZG", children=[dcc.Markdown(id="szg")])
                     ]),
                     html.H2(id="best_prh"),
                     dcc.Markdown(id="best_pr"),
                     dcc.Tabs([
                             dcc.Tab(label="1", children=[dcc.Markdown(id="bp1")]),
                             dcc.Tab(label="2", children=[dcc.Markdown(id="bp2")]),
                             dcc.Tab(label="3", children=[dcc.Markdown(id="bp3")]),
                             dcc.Tab(label="4", children=[dcc.Markdown(id="bp4")]),
                             dcc.Tab(label="5", children=[dcc.Markdown(id="bp5")]),
                             dcc.Tab(label="6", children=[dcc.Markdown(id="bp6")]),
                             dcc.Tab(label="7", children=[dcc.Markdown(id="bp7")]),
                             dcc.Tab(label="8", children=[dcc.Markdown(id="bp8")]),
                             dcc.Tab(label="9", children=[dcc.Markdown(id="bp9")])
                 ])
                 ])
        ])
])


@ app.callback(
    [Output("h1", "children"),
     Output("p_desc", "children"),
     Output("szg", "children"),
     Output("interpr", "children"),
     Output("best_prh", "children"),
     Output("bp1", "children"),
     Output("bp2", "children"),
     Output("bp3", "children"),
     Output("bp4", "children"),
     Output("bp5", "children"),
     Output("bp6", "children"),
     Output("bp7", "children"),
     Output("bp8", "children"),
     Output("bp9", "children")],
    [Input("lang-selector", "value")])


def multi_output(value):
    return ml.h1[value], \
           ml.p_desc[value], \
           ml.szg[value], \
           ml.interpr[value], \
           ml.best_prh[value], \
           ml.bp1[value], \
           ml.bp2[value], \
           ml.bp3[value], \
           ml.bp4[value], \
           ml.bp5[value], \
           ml.bp6[value], \
           ml.bp7[value], \
           ml.bp8[value], \
           ml.bp9[value]


if __name__ == '__main__':
    application.run(debug=True, port=80)
