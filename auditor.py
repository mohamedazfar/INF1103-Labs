inventory = 0

while True:
    stock = input("Enter a stock quantity: ")
    
    if stock.isdigit():
        stock = int(stock)

        if (inventory+stock) > 500:
            print("Total Inventory exceeded 500 units!")
            break

        inventory += stock

    elif stock == 'quit':
        break

    else:
        print("Error! Enter only positive integer")

print(inventory)