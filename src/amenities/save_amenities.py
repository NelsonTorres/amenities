"""CLI application to link distinct infrastructure pieces."""

import click

from services.postgresql_connector import get_conn, store_amenities
from services.load_osm import get_osm
import json

@click.command()
@click.argument("place", nargs=1)
def save_amenities(place: str):
    """Saves amenities to database."""
    with get_conn() as conn:
        data = get_osm(place)
        store_amenities(conn, data)


if __name__ == "__main__":
    save_amenities()
