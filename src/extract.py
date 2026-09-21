from db.source import get_source_connection
from utils.queryRunner import run_query

def extractclients():
    query = """SELECT client_id, first_name, last_name FROM clients """
    run_query(query)
def instruments():
    query = """ SELECT * FROM intruments"""
    run_query(query)
def employees():
    query = """ SELECT employee_id, first_name, last_name, role FROM employees"""
    run_query(query)
def prices():
    query = """ SELECT * FROM prices"""
    run_query(query)
def holdings():
    query = """ SELECT * FROM holdings"""
    run_query(query)
def transactions():
    query = """ SELECT * FROM transactions"""   
    run_query(query)
def orders():
    query = """ SELECT * FROM orders"""
    run_query(query)
if __name__ == "__main__":
    holdings()