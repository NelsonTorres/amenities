"""Gets city area and amenities."""


import requests

from logging import Logger

logger = Logger(__name__)

def get_osm(place_name: str, amenity: str):
    """Downloads amenity coordinates."""
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
        [out:json];
        area[name="{place_name}"]->.b;
        rel(area.b);
        map_to_area -> .a;
        node(area.a)[amenity={amenity}];
        out meta;
    """
    response = requests.get(overpass_url, 
                            params={'data': overpass_query})

    data = response.json()

    elements = data["elements"]

    logger.error(f"Found {len(elements)} elements.")
    return elements



