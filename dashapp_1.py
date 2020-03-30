import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('dash_app', external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.H1('Hello')
)













app.run_server(debug=True)
