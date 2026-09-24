from db.source import get_source_connection
def run_query(query, last_watermark):
    with get_source_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (last_watermark,))
                return cur.fetchall()