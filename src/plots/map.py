import pandas as pd
import plotly.graph_objects as go
from plots import load_amenities

#example
#df = pd.DataFrame(
#    {'object': ['Sendlinger Tor'],
#     'lat': [48.1340043],
#     'lon': [11.567605800000024]}
#     )

df = load_amenities()

df['name'] = [elem.get('name') for elem in df.tags]
available_tags = {key: value for key, value in df.tags.items()}
available_tags = 

fig = go.Figure(
    data=go.Scattergeo(
        lon = df['lon'],
        lat = df['lat'],
        text = df['name'],
        mode = 'markers',

    )
)

fig.update_geos(
    visible=False, 
    resolution=110, 
    scope="europe",
    showcountries=True, 
    countrycolor="Black",
    showsubunits=True, 
    subunitcolor="Blue"
)

fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(height=2400, margin={"r":0,"t":0,"l":0,"b":0})






fig.show()