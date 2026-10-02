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

    print(f"Saving inventory...\n"
          "Inventory saved successfully to {filename}.")

def display(inventory):

    print("Current Inventory\n"
          "--------------------------------------------")
    for product in inventory:
        print(" | ".join(f"{key}: {value}" for key, value in product.items()))
    print("--------------------------------------------\n")

def add(inventory):
    print("Add New Product")
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
    print("Product added successfully!\n")
    return inventory

def update(inventory):
    print("Update Stock")
    id = input("Enter Product ID: ")
    print("\nProduct Found:")
    
    for product in inventory:
        if product['ID'] == id:
            print("Name:", product["Name"])
            print("Current Stock:", product["Stock"], "\n")
            new_stock = int(input("New Stock Quantity: "))
            product["Stock"] = new_stock

    print("Stock update successfully!")

    return inventory

def search(inventory):
    print("Search Product")

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
            print("-------------------------------------")
            found = True

    if not found:
        print("\nProduct not found.")

# Main Program
filename = "inventory.json"

print("====================================================\n"
      "INVENTORY MANAGEMENT SYSTEM\n"
      "====================================================\n"
      )

inventory = load(filename)


print("-------------MENU-------------\n"
"1. Display All Products\n"  
"2. Add Product\n" 
"3. Update Stock\n" 
"4. Search Product\n" 
"5. Save Inventory\n"
"6. Exit\n"
"------------------------------\n"
)

#inventory = add(inventory)
#inventory = update(inventory)
inventory = search(inventory)

#save(product, filename)

#display(inventory)
