"""Gets city area and amenities."""


import requests



def get_osm(place_name: str):

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
        [out:json];
        area[name="{place_name}"]->.b;
        rel(area.b);
        map_to_area -> .a;
        node(area.a)[amenity=pub];
        out meta;
    """
    response = requests.get(overpass_url, 
                            params={'data': overpass_query})

    data = response.json()
    return data["elements"]



