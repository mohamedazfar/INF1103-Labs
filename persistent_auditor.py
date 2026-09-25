import os

def load_inventory(file_name):

    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            print("\nNo Current current_orders found.")
        return None
            
    else:
        with open(file_name, "r") as file:
            current_orders = file.readlines()

        print("\nCurrent Orders:")
        for order in current_orders:
            print(order, end="")
        return current_orders

def get_valid_input():
    print("\n")
    productName = input("Enter Product Name: ")
    if productName == 'quit':
        return productName

    quantity = input("Enter Quantity: ")
    if quantity == 'quit' :
        return quantity
    
    elif quantity.isdigit():
        return productName, int(quantity)
    
    else:
        print("Error! Enter a non-negative integer.")
        return None

def getNewID(orderIDLatest):
    new_id = int(orderIDLatest) + 1
    return str(new_id)

def addToNewOrders(new_id, order, new_orders):
    transaction =  new_id + ", " + order[0] + ", " + str(order[1]) + "\n"

    new_orders.append(transaction)
    print("\nNew Order Added:")
    print(transaction)
    return new_orders

def save_inventory(file_name, new_orders):
    with open(file_name, "a") as file:
        file.writelines(new_orders)
    print(f"Order successfully saved to {file_name}")

def getLatestOrderID(list):
    id = max(list).split(",")[0]
    return id

def calculate_total(inventory, order):
    inventory += order[1]
    return inventory

# Main program
file_name = "inventory.txt"
inventory = 0
new_orders = []
orderID_start = 1000


current_orders = load_inventory(file_name)
orderIDLatest = getLatestOrderID(current_orders)

while True:
    order = get_valid_input()
    if order == 'quit':
        break

    if order is None:
        continue

    new_id = getNewID(orderIDLatest)
    new_orders = addToNewOrders(new_id, order, new_orders)

    orderIDLatest = getLatestOrderID(new_orders)
    inventory = calculate_total(inventory, order)
    
print(inventory)
save_inventory(file_name, new_orders)