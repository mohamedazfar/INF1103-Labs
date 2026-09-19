def get_valid_input():
    '''Handles the prompt, handles input validation, and returns a valid integer or a quit signal'''
    stock = input("Enter a stock quantity: ")

    if stock.isdigit():
        return int(stock)
    
    elif stock == 'quit':
        return stock
    
    else:
        print("Error! Enter a non-negative integer.")
        return None

def process_delivery(current_total, new_value):
    '''Calculates the new total and returns it'''
    new_total = current_total + new_value 
    return new_total

def calculate_tax(amount):
    '''Takes delivery amount and returns the tax'''
    tax = amount * 0.10
    print("Delivery Processed. Tax for this Delivery:", tax)
    return tax

def generate_report(total_units, failed_attempts, deliveries):
    '''Prints the final summary'''
    print("--------------------------------------")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Total Deliveries processed:", deliveries)

# Main program
inventory = 0
error = 0
deliveries = 0

while True:
    stock = get_valid_input()

    if stock == 'quit':
        break

    if stock is None:
        error += 1
        continue

    inventory = process_delivery(inventory, stock)
    deliveries += 1

    calculate_tax(stock)
    
generate_report(inventory, error, deliveries)