def get_valid_input():
    '''Handles the prompt, handles input validation, and returns a valid integer or a quit signal'''
    stock = input("Enter a stock quantity: ")

    if stock.isdigit():
        return int(stock)
    
    elif stock == 'quit':
        return stock
    
    else:
        print("Error! Enter only positive number.")
        return False

def process_delivery(current_total, new_value):
    '''Calculates the new total and returns it'''
    new_total = current_total + new_value 
    return new_total

def calculate_tax(amount):
    '''Takes delivery amount and returns the tax'''
    tax_percent = 0.1
    tax_value = amount * tax_percent
    return tax_value

def generate_report(total_units, failed_attempts):
    '''Prints the final summary'''
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
error = 0
inventory_limit = 500

while True:
    stock = get_valid_input()

    if stock == 'quit':
        break

    if stock == False:
        error += 1
        continue
        
    if (inventory+stock) > inventory_limit:
        print("Alert: Total Inventory exceeded 500 units!")
        break

    inventory = process_delivery(inventory, stock)

    calculate_tax(stock)

generate_report(inventory, error)