import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_target_connection():
    try:
        conn = psycopg.connect(
            host=os.getenv("TARGET_DB_HOST"),
            port=os.getenv("TARGET_DB_PORT"),
            dbname=os.getenv("TARGET_DB_NAME"),
            user=os.getenv("TARGET_DB_USER"),
            password=os.getenv("TARGET_DB_PASSWORD"),
        )
        print("Datawarehouse connection successful")
        return conn
    except Exception as e:
        print(f"Datawarehouse connection error: {e}")
        raise