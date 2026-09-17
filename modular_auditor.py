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
    inventory += stock

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", error)