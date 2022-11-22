import dash
import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import os
from cron_job.utils import open_connection
from flask_caching import Cache

"""
This is an app that will: 
1. get info from specific table from bird info
2. precalculate and cache data 
2. plot observations on a map
3. plot statistics on records from table
4. plots statistics on bird_info map
"""

DB_PASSW = os.getenv("BIRD_DB_PASSW")


def connect_to_db():
    """
    Connects to db port
    :return: connection link
    """
    cnx = open_connection()
    return cnx


def get_data_from_db(cnx, table_name):
    """
    A query to return table by the name passed to the function
    :return: SQL query
    """
    cur = cnx.cursor()
    cur2 = cnx.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    cur2.execute(f"SELECT column_name FROM information_schema.columns where table_name = 'cy';")
    colnames = [_[0] for _ in cur2.fetchall()]
    return pd.DataFrame.from_records(cur.fetchall(), columns=colnames)


def check_data(cnx, table_name):
    """
    An SQL query to remove duplicates in the data
    :return:
    """
    cur = cnx.cursor()
    cur.execute(f"SELECT speciesCode FROM {table_name};")


def summarize_data(data, item):
    """
    An SQL query that will return summary by field - species name and region
    :param data:
    :return:
    """
    pass


def map_data_to_geog_regions(data):
    """
    This function will map data from ebird to the geographical areas.
    :param data:
    :return:
    """
    pass


def generate_table(df):
    table = html.Div(dash_table.DataTable(
        id='datatable-paging',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=25,
        page_current=0
    ))
    return table


external_stylesheets = [dbc.themes.SPACELAB]
cnx = connect_to_db()
df = get_data_from_db(cnx, "CY")[1:100]
df['howmany'] = df['howmany'].replace(np.nan, 0).astype('float')
fig = px.histogram(df, x="sciname", y="howmany", color="sciname")

scale = 10
fig_map = px.scatter_mapbox(
    df,
    lon='lng',
    lat='lat',
    text='comname',
    size='howmany',
    size_max=10,
    mapbox_style="open-street-map",
)

fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


app_class = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app_class.server

cache = Cache(app_class.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                children=[
                    dbc.Pagination(max_value=5, fully_expanded=False),
                    generate_table(df)]
            )

        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                children=[html.H2('Species observation counts'),
                          dcc.Graph(
                              id='example-graph-1',
                              figure=fig
                          )])
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                children=[html.H2('Species observation location'),
                          dcc.Graph(
                              id='example-graph-2',
                              figure=fig_map
                          )])
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Table"),
        dbc.Tab(tab2_content, label="Barplot"),
        dbc.Tab(tab3_content, label="Map"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ]
)

list_of_layouts = [
    html.Div(
        children=[html.H1(children='Hello Dash')],
        style={'backgroundColor': '#c2c2a3', 'padding': 10, 'flex': 1}),
    tabs
]

app_class.layout = html.Div(children=list_of_layouts)

if __name__ == '__main__':
    # app_class.run_server(debug=True)  # launch app on heroku
    app_class.run_server(host="0.0.0.0", port=8050, debug=True)  # launch app locally
    cnx.close()
