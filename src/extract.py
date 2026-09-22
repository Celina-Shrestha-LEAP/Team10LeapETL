from db.source import get_source_connection
from utils.queryRunner import run_query


def extractClients(last_watermark):
    query = f"""SELECT client_id, first_name, last_name, updated_at FROM clients WHERE updated_at > %s ORDER BY updated_at, client_id"""
    return run_query(query, (last_watermark,))
    
def extractEmployees(last_watermark):
    query = f""" SELECT employee_id, first_name, last_name, role, updated_at FROM employees WHERE updated_at > %s ORDER BY updated_at, employee_id"""
    return run_query(query, (last_watermark,))
    
def extractPrices(last_watermark):
    query = f""" SELECT * FROM prices WHERE recorded_at > %s ORDER BY recorded_at, price_id"""
    return run_query(query, (last_watermark,))
    
def extractTransactions(last_watermark):
    query = f""" SELECT * FROM transactions WHERE created_at > %s ORDER BY created_at, transaction_id"""   
    return run_query(query, (last_watermark,))
    
def extractHoldingsAndOrders(last_watermark):
    query = f""" SELECT h.quantity, o.*
        FROM holdings h
        JOIN orders o
        ON h.client_id = o.client_id AND h.ticker = o.ticker WHERE o.order_date > %s"""
    return run_query(query, (last_watermark,))
    

    