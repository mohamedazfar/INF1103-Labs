import os

def load_inventory(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            print("\nNo Current Orders found.")
        return None, 0
            
    else:
        with open(file_name, "r") as file:
            current_orders = file.readlines()

        inventory = int(current_orders[-1].split(":")[1].strip())
        del current_orders[-1]

        print("\nCurrent Orders:")
        for order in current_orders:
            print(order, end="")

        return current_orders, inventory

def get_valid_input():
    productName = input("\nEnter Product Name: ")
    if productName == 'quit':
        return productName

    quantity = input("Enter Quantity: ")
    if quantity == 'quit' :
        return quantity
    
    elif quantity.isdigit():
        return productName, quantity
    
    else:
        print("Error! Enter a non-negative integer.")
        return None

def getNewID(orderIDLatest):
    new_id = int(orderIDLatest) + 1
    return str(new_id)

def addToNewOrders(new_id, order, new_orders):
    transaction =  new_id + ", " + order[0] + ", " + order[1] + "\n"
    new_orders.append(transaction)
    print("\nNew Order Added:")
    print(transaction)
    return new_orders

def save_inventory(file_name, current_orders, new_orders, inventory):
    with open(file_name, "w") as file:
        if current_orders is not None:
            file.writelines(current_orders)
        file.writelines(new_orders)
        file.write(f"Inventory Total: {inventory}\n")
    print(f"\nOrder successfully saved to {file_name}\n")

def getLatestOrderID(list):
    id = max(list).split(",")[0]
    return id

def calculate_total(inventory, order):
    inventory += int(order[1])
    return inventory

# Main program
file_name = "inventory.txt"
inventory = 0
new_orders = []
orderID_start = 1000

current_orders, inventory = load_inventory(file_name)

if current_orders is None:
    orderIDLatest = orderID_start
else:
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
    
save_inventory(file_name, current_orders, new_orders, inventory)