def get_valid_input():
    prompt = "Enter a stock quantity: "
    stock = input(prompt)

    # checks if the input is valid integer
    if stock.isdigit():
        return int(stock)

    # exits the while loop if user wants to quit
    elif stock == 'quit':
        return stock

    # prints error message if user enters string or negative numbers
    else:
        print("Error! Enter only positive number.")
        return False

def process_delivery(current_total, new_value):
    new_total = current_total + new_value 
    return new_total

def calculate_tax(amount):
    tax_percent = 0.1
    tax_value = amount * tax_percent
    return tax_value 


inventory = 0
error = 0
inventory_limit = 500

while True:
    stock = get_valid_input()

    if stock == 'quit':
        break

    if stock == False:
        error += 1
        
    # exit if inventory exceeds 500
    if (inventory+stock) > inventory_limit:
        print("Alert: Total Inventory exceeded 500 units!")
        break

    # add the stock to the inventory
    inventory = process_delivery(inventory, stock)

    print(calculate_tax(stock))

    

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", error)