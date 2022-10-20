import dash
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
print('1')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
print('2')
server = app.server
print('3')
app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
                 'LA',
                 id='dropdown'
                 ),
    html.Div(id='display-value')
])

print('4')

@app.callback(Output('display-value', 'children'),
              [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

print('5')

if __name__ == '__main__':
    app.run_server(debug=True)
