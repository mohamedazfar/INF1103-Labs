import json
import os

# Functions definitions
def load(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                inventory = json.load(file)              
        except json.JSONDecodeError:
            inventory = []
        print(f"{filename} found.\nInventory loaded successfully.\n")        
    else:
        inventory = []
        with open(filename, "w") as file:
            inventory = json.dump(inventory, file)
    
    return inventory

def save(inventory, filename):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)

    print(f"\nSaving inventory...\n"
          "Inventory saved successfully to {filename}.\n")

def display(inventory):
    print("\nCurrent Inventory\n"
          "--------------------------------------------")
    for product in inventory:
        print(" | ".join(f"{key}: {value}" for key, value in product.items()))
    print("--------------------------------------------\n")

def add(inventory):
    print("\nAdd New Product")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = input("Price: ")
    stock = int(input("Stock Quantity: "))

    product  = {
    "ID": id,
    "Name": name,
    "Price": price,
    "Stock": stock
    }

    inventory.append(product)
    print("\nProduct added successfully!\n")
    return inventory

def update(inventory):
    print("\nUpdate Stock")
    id = input("Enter Product ID: ")
    print("\nProduct Found:")
    
    for product in inventory:
        if product['ID'] == id:
            print("Name:", product["Name"])
            print("Current Stock:", product["Stock"], "\n")
            new_stock = int(input("New Stock Quantity: "))
            product["Stock"] = new_stock

    print("\nStock update successfully!\n")

    return inventory

def search(inventory):
    print("\nSearch Product")

    id = input("Enter Product ID: ")        
    found = False
    
    for product in inventory:
        if product['ID'] == id:
            print("\nProduct Found")
            print("-------------------------------------")
            print("ID:", product["ID"])
            print("Name:", product["Name"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])
            print("-------------------------------------\n")
            found = True

    if not found:
        print("\nProduct not found.\n")

def menu():
    print("-------------MENU-------------\n"
    "1. Display All Products\n"  
    "2. Add Product\n" 
    "3. Update Stock\n" 
    "4. Search Product\n" 
    "5. Save Inventory\n"
    "6. Exit\n"
    "------------------------------\n"
)

# Main Program
filename = "inventory.json"

print("\n====================================================\n"
      "INVENTORY MANAGEMENT SYSTEM\n"
      "====================================================\n"
      )

inventory = load(filename)

menu()

while True:
    option = int(input("Enter Option: "))

    if option == 1:
        display(inventory)

    elif option == 2:
        inventory = add(inventory)

    elif option == 3:
        inventory = update(inventory)

    elif option == 4: 
        search(inventory)

    elif option == 5:
        save(inventory, filename)

    elif option == 6:
        save(inventory, filename)
        print("\nThank you for using Inventory Management System.\n"
              "Program terminated.\n")
        break
