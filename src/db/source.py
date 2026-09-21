import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_source_connection():
    try:
        conn = psycopg.connect(
            host=os.getenv("SOURCE_DB_HOST"),
            port=os.getenv("SOURCE_DB_PORT"),
            dbname=os.getenv("SOURCE_DB_NAME"),
            user=os.getenv("SOURCE_DB_USER"),
            password=os.getenv("SOURCE_DB_PASSWORD"),
        )
        print("Trading database connection successful")
        return conn
    except Exception as e:
        print(f"Trading database connection error: {e}")
        raise