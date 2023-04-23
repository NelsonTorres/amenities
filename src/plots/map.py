import pandas as pd
import plotly.graph_objects as go
from plots import load_amenities

def filter_amenity(df: pd.DataFrame,  amenity: str):
    """Return rows with amenity amenity."""
    return df.where(df['amenity'] == amenity)

df = load_amenities()

df['name'] = [elem.get('name') for elem in df.tags]
df['amenity'] = [elem.get('amenity') for elem in df.tags]





fig = go.Figure()

def add_trace(fig: go.Figure, df: pd.DataFrame, amenity: str) -> None:
    """Adds mmarkers of amenity."""
    local_df = filter_amenity(df, amenity)
    fig.add_trace(
        go.Scattergeo(
            name=amenity,
            lon = local_df['lon'],
            lat = local_df['lat'],
            text = local_df['name'],
            mode = 'markers',
            legendgroup=amenity,
            marker_coloraxis="coloraxis",
            visible="legendonly"
        )
    )

add_trace(fig, df, 'pub')
add_trace(fig, df, 'sport')


fig.update_geos(
    visible=True, 
    resolution=110, 
    scope="europe",
    showcountries=True, 
    countrycolor="Black",
    showsubunits=True, 
    subunitcolor="Blue",

)

fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},
)

fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)


fig.show()