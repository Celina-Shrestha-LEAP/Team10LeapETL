from src.db.target import get_target_connection


def loadClients(client_rows):
    if not client_rows:
        return 0

    query = """
        INSERT INTO clients (
            client_id,
            first_name, 
            last_name,
            updated_at
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (client_id)
        DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            updated_at = EXCLUDED.updated_at
    """

    with get_target_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(query, client_rows)

        conn.commit()

    return len(client_rows)



def loadEmployees(employee_rows):
    if not employee_rows:
        return 0

    query = """
        INSERT INTO employees (
            employee_id,
            first_name, 
            last_name,
            updated_at
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (employee_id)
        DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            updated_at = EXCLUDED.updated_at
    """

    with get_target_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(query, employee_rows)

        conn.commit()

    return len(employee_rows)


def loadPrices(price_rows):
    if not price_rows:
        return 0

    query = """
        INSERT INTO prices (
            price_id,
            ticker, 
            ask_price,
            ask_size,
            bid_price,
            bid_size,
            ask_exchange,
            bid_exchange,
            tape,
            recorded_at,
            quote_timestamp
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (price_id)
        DO UPDATE SET
            ticker = EXCLUDED.ticker,
            ask_price = EXCLUDED.ask_price,
            ask_size = EXCLUDED.ask_size,
            bid_price = EXCLUDED.bid_price,
            bid_size = EXCLUDED.bid_size,
            ask_exchange = EXCLUDED.ask_exchange,
            bid_exchange = EXCLUDED.bid_exchange,
            tape = EXCLUDED.tape,
            recorded_at = EXCLUDED.recorded_at,
            quote_timestamp = EXCLUDED.quote_timestamp
    """

    with get_target_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(query, price_rows)

        conn.commit()

    return len(price_rows)


def loadTransactions(transaction_rows):
    if not transaction_rows:
        return 0

    query = """
        INSERT INTO transactions (
            transaction_id,
            client_id,
            created_at,
            ttype,
            amount
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (transaction_id)
        DO UPDATE SET
            client_id = EXCLUDED.client_id,
            created_at = EXCLUDED.created_at,
            ttype = EXCLUDED.ttype,
            amount = EXCLUDED.amount
    """

    with get_target_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(query, transaction_rows)

        conn.commit()

    return len(transaction_rows)


def loadPrices(price_rows):
    if not price_rows:
        return 0

    query = """
        INSERT INTO prices (
            price_id,
            ticker, 
            ask_price,
            ask_size,
            bid_price,
            bid_size,
            ask_exchange,
            bid_exchange,
            tape,
            recorded_at,
            quote_timestamp
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (price_id)
        DO UPDATE SET
            ticker = EXCLUDED.ticker,
            ask_price = EXCLUDED.ask_price,
            ask_size = EXCLUDED.ask_size,
            bid_price = EXCLUDED.bid_price,
            bid_size = EXCLUDED.bid_size,
            ask_exchange = EXCLUDED.ask_exchange,
            bid_exchange = EXCLUDED.bid_exchange,
            tape = EXCLUDED.tape,
            recorded_at = EXCLUDED.recorded_at,
            quote_timestamp = EXCLUDED.quote_timestamp
    """

    with get_target_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(query, price_rows)

        conn.commit()

    return len(price_rows)