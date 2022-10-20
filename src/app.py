import dash
import dash_core_components as dcc
import dash_html_components as html
import time
__name__ = 'test app'
# simulate long loading time
time.sleep(120)

app = dash.Dash(__name__)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)