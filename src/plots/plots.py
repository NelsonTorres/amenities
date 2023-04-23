import pandas as pd
from postgresql_connector import get_conn

pd.set_option('display.max_columns', None)



def load_amenities():
    """Loads amenities from database."""
    conn = get_conn()
    query  = "SELECT * FROM amenities"
    return pd.read_sql(query, conn)

# app = Dash(__name__)

# app.layout = html.Div([
#    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
#    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
#    dcc.Graph(id='graph-content')
#])

#@callback(
#    Output('graph-content', 'figure'),
#    Input('dropdown-selection', 'value')
#)
#def update_graph(value):
#    dff = df[df.country==value]
#    return px.line(dff, x='year', y='pop')

#if __name__ == '__main__':
#    app.run_server(debug=True)