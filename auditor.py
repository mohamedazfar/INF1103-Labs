inventory = 0
error = 0

while True:
    stock = input("Enter a stock quantity: ")

    # checks if the input is valid integer
    if stock.isdigit():
        stock = int(stock)

        # exit if inventory exceeds 500
        if (inventory+stock) > 500:
            print("Total Inventory exceeded 500 units!")
            break

        # add the stock to the inventory
        inventory += stock

    # exits the while loop if user wants to quit
    elif stock == 'quit':
        break

    # prints error message if user enters string or negative numbers
    else:
        print("Error! Enter only positive integer")
        error += 1

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", error)