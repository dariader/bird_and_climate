import dash
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app_class = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app_class.server
app_class.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
                 'LA',
                 id='dropdown'
                 ),
    html.Div(id='display-value')
])

if __name__ == '__main__':
    app_class.run_server(debug=True)  # launch app on heroku
    app_class.run_server(host="0.0.0.0", port=8050, debug=True)  # launch app locally

