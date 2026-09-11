inventory = 0

while True:
    stock = input("Enter a stock quantity: ")
    
    if stock.isdigit():
        stock = int(stock)

    elif stock == 'quit':
        break

    else:
        print("Error! Enter only positive integer")