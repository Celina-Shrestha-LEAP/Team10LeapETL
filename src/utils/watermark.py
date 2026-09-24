import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from db.target import get_target_connection
from datetime import datetime, timezone

ETL_NAME = "trading_db_etl"

def get_last_watermark(table_name='clients'):
    """Get watermark for a specific table"""
    query = "SELECT last_watermark FROM watermark_etl WHERE name_id = %s"
    
    try:
        conn = get_target_connection()
        with conn.cursor() as cur:
            cur.execute(query, (table_name,))
            result = cur.fetchone()
            if result:
                return result[0]
            return datetime(1970, 1, 1, tzinfo=timezone.utc)
    except Exception as e:
        print(f"Error retrieving watermark for {table_name}: {e}")
        raise
    
def update_last_watermark(table_name, new_watermark):
    """Update watermark for a specific table"""
    query = "UPDATE watermark_etl SET last_watermark = %s WHERE name_id = %s"
    
    try:
        conn = get_target_connection()
        with conn.cursor() as cur:
            cur.execute(query, (new_watermark, table_name))
            conn.commit()
        print(f"✓ Updated {table_name} watermark to {new_watermark}")
    except Exception as e:
        print(f"Error updating watermark for {table_name}: {e}")
        raise


def get_max_timestamp(rows):
    """Get the latest timestamp from rows (already normalized by transform.py)"""
    if not rows:
        return None
    timestamps = []
    for row in rows:
        ts = row[-1]
        if isinstance(ts, datetime):
            timestamps.append(ts)
    return max(timestamps) if timestamps else None


