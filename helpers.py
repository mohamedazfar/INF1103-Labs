# Helper functions
def check_stock_input(prompt):
    while True:
        stock = input(prompt)
        if stock.isdigit():
            return int(stock)
        print("Error! Enter a non-negative integer.")

def check_price_input(prompt):
    while True:
        price = input(prompt)
        try:
            if float(price) > 0:
                return round(float(price), 2)
        except ValueError:
            pass
        print("Error! Enter a non-negative number.")