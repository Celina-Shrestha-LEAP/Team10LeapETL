import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from db.target import get_target_connection

ETL_NAME = "trading_db_etl"

def get_last_watermark():
    query = "SELECT last_watermark FROM watermark_etl WHERE name = %s"
    
    try:
        conn = get_target_connection()
        with conn.cursor() as cur:
            cur.execute(query, (ETL_NAME,))
            last_watermark = cur.fetchone()[0]
            return last_watermark
    except Exception as e:
        print(f"Error retrieving last watermark: {e}")
        raise
    
def update_last_watermark(new_watermark):
    query = "UPDATE watermark_etl SET last_watermark = %s WHERE name = %s"
    
    try:
        conn = get_target_connection()
        with conn.cursor() as cur:
            cur.execute(query, (new_watermark, ETL_NAME))
            conn.commit()
    except Exception as e:
        print(f"Error updating last watermark: {e}")
        raise


