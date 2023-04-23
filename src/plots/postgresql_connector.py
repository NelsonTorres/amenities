"""Gets interface to communicate with postgreSQL."""
import os 
import psycopg2
from sqlalchemy import create_engine


def get_conn():
    """returns database connection."""

    database = os.environ["POSTGRESQL_DATABASE"]
    user = os.environ["POSTGRESQL_USER"]
    password = os.environ["POSTGRESQL_PASSWORD"] 
    host = os.environ["POSTGRESQL_HOST"] 
    port = os.environ["POSTGRESQL_PORT"]

    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    return create_engine( connection_string)

