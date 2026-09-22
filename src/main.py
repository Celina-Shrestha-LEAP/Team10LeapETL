from src.utils.watermark import get_last_watermark, update_last_watermark
from src.extract import (extractClients, extractEmployees, extractPrices, extractTransactions, extractHoldingsAndOrders)
from src.load import (loadClients, loadEmployees, loadPrices, loadTransactions, loadHoldingsAndOrders)

def run():
    last_watermark = get_last_watermark()
    print(f"Last watermark: {last_watermark}")
    
    # EXTRACT
    try:
        client_rows = extractClients(last_watermark)
        employee_rows = extractEmployees(last_watermark)
        price_rows = extractPrices(last_watermark)
        transaction_rows = extractTransactions(last_watermark)
        order_holding_rows = extractHoldingsAndOrders(last_watermark)
    except Exception as e:
        print(f"Error during extraction: {e}")
        return
    
    
    #LOAD
    try:
        loadClients(client_rows)
        loadEmployees(employee_rows)
        loadPrices(price_rows)
        loadTransactions(transaction_rows)
        loadHoldingsAndOrders(order_holding_rows)
    except Exception as e:
        print(f"Error during loading: {e}")
        return
    
    
    
    new_watermark = max(
        max([row['watermark'] for row in client_rows], default=last_watermark),
        max([row['watermark'] for row in employee_rows], default=last_watermark),
        max([row['watermark'] for row in price_rows], default=last_watermark),
        max([row['watermark'] for row in transaction_rows], default=last_watermark),
        max([row['watermark'] for row in order_holding_rows], default=last_watermark)
    )
    
    update_last_watermark(new_watermark)
    print(f"New watermark: {new_watermark}")



if __name__ == "__main__":
    run()