import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_source_connection():
    return psycopg.connect(
        host=os.getenv("SOURCE_DB_HOST"),
        port=os.getenv("SOURCE_DB_PORT"),
        dbname=os.getenv("SOURCE_DB_NAME"),
        user=os.getenv("SOURCE_DB_USER"),
        password=os.getenv("SOURCE_DB_PASSWORD"),
    )