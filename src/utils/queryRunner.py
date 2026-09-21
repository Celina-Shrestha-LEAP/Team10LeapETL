from db.source import get_source_connection
def run_query(query):
    with get_source_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(cur.fetchall())
                return cur.fetchall()