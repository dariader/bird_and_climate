import dash
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

"""
This is an app that will: 
1. get info from specific table from bird info
2. plot observations on a map
3. plot statistics on records from table
4. plots statistics on bird_info map
"""

external_stylesheets = [dbc.themes.SPACELAB]
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df_table = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app_class = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app_class.server

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                children=[
                    html.H2('Hello World'),
                    dcc.Dropdown(['LA', 'NYC', 'MTL'],
                                 'LA',
                                 id='dropdown-1'
                                 ),
                    html.Div(id='display-value-1'),
                    html.Br(),
                    html.H4(children='US Agriculture Exports (2011)'),
                    generate_table(df)],
                style={'backgroundColor': '#8c86ad', 'padding': 10, 'flex': 1})

        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
                html.Div(
                children=['''Dash: A web application framework for your data.''',
                          dcc.Graph(
                              id='example-graph-1',
                              figure=fig
                          )], style={'backgroundColor': '#83a885', 'padding': 10, 'flex': 1})
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Tab 1"),
        dbc.Tab(tab2_content, label="Tab 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ]
)

list_of_layouts = [
    html.Div(
        children=[html.H1(children='Hello Dash')],
        style={'backgroundColor': '#c2c2a3', 'padding': 10, 'flex': 1}),
    tabs,
    html.Div(
        style={'display': 'flex', 'flex-direction': 'row'},
        children=[
            html.Div(
                children=['''Dash: A web application framework for your data.''',
                          dcc.Graph(
                              id='example-graph',
                              figure=fig
                          )], style={'backgroundColor': '#83a885', 'padding': 10, 'flex': 1}),
            html.Div(
                children=[
                    html.H2('Hello World'),
                    dcc.Dropdown(['LA', 'NYC', 'MTL'],
                                 'LA',
                                 id='dropdown'
                                 ),
                    html.Div(id='display-value'),
                    html.Br(),
                    html.H4(children='US Agriculture Exports (2011)'),
                    generate_table(df)], style={'backgroundColor': '#8c86ad', 'padding': 10, 'flex': 1})
        ])
]


app_class.layout = html.Div(children=list_of_layouts)




if __name__ == '__main__':
    # app_class.run_server(debug=True)  # launch app on heroku
    app_class.run_server(host="0.0.0.0", port=8050, debug=True)  # launch app locally
