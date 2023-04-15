"""Gets interface to communicate with postgreSQL."""
import os 
import psycopg2
from typing import Any
from models.amenity import Amenity
from datetime import datetime

def get_conn():
    """returns database connection."""
    return psycopg2.connect(
        database=os.environ["POSTGRESQL_DATABASE"], 
        user = os.environ["POSTGRESQL_USER"], 
        password = os.environ["POSTGRESQL_PASSWORD"], 
        host = os.environ["POSTGRESQL_HOST"], 
        port = os.environ["POSTGRESQL_PORT"]
    )

def dict_to_schema(schema):
    """converts dict to schema syntax."""
    schema_text = [f'{key} {value}' for key, value in schema.items()]
    return  ",\n".join(schema_text)


def create_table(conn: psycopg2.extensions.connection, table:str, if_not_exists: bool, schema: dict[str, str]) -> None:
    """Create a postgresql table."""
    with conn.cursor() as cur:
        statement = ''.join([
            "CREATE ",
            "TABLE ",
            "IF NOT EXISTS " if if_not_exists else "", 
            table,
            " ( \n",
            dict_to_schema(schema),
            "\n);",
        ])

        cur.execute(statement)
    conn.commit()



def store_amenities(conn: psycopg2.extensions.connection, amenities: list[dict[str: Any]]) -> None:
    """Saves amenity to table."""

    table_schema= {
        "type": "text",
        "id": "bigint",
        "lat": "float",
        "lon": "float",
        "timestamp": "timestamp",
        "version": "int",
        "uid": "bigint",
        "tags": "jsonb"
    }
    create_table(conn, "amenities", True,  table_schema)
    with conn.cursor() as cur:
        for amenity in amenities:
            dao = Amenity(
                amenity["type"],
                amenity["id"],
                amenity["lat"],
                amenity["lon"],
                datetime.strptime(amenity["timestamp"], '%Y-%m-%dT%H:%M:%SZ'),
                amenity["version"],
                amenity["uid"],
                amenity["tags"]
            )
            column_names = ',\n'.join(table_schema.keys())

            statement =f"""
                INSERT INTO amenities(
                {column_names}
                )
                values(
                    '{dao.type}',
                    {dao.id},
                    {dao.lat},
                    {dao.lon},
                    '{dao.timestamp}',
                    {dao.version},
                    {dao.uid},
                    '{dao.tags_str}'
            );"""            
            print(statement)
            cur.execute(statement)
    conn.commit()
