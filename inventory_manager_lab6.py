import json
import os

# Represents and manages a single product
class Product:
    def __init__(self, id, name, price, stock):
        self.__id = str(id)
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_product(self):
        print("\nProduct Found")
        print("-------------------------------------")
        print("ID:", self.__stock)
        print("Name:", self.__name)
        print("Price:", self.__price)
        print("Stock:", self.__stock)
        print("-------------------------------------\n")

# Manages a collection of products
class Inventory:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None  

    def display_all(self):
        print("\nCurrent Inventory\n")
        print("--------------------------------------------")
        for product in self.__products:
            print(f"ID: {product.get_id()} | Name: {product.get_name()} | Price: {product.get_price()} | Stock: {product.get_stock()} ")
        print("--------------------------------------------\n")

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
            json.dump(inventory, file, indent=4)
    
    return inventory

def save(inventory, filename):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)

    print("\nSaving inventory...\n"
          f"Inventory saved successfully to {filename}.\n")

def display(inventory):
    print("\nCurrent Inventory\n"
          "--------------------------------------------")
    for product in inventory:
        print(" | ".join(f"{key}: {value}" for key, value in product.items()))
    print("--------------------------------------------\n")

def add(inventory):
    print("\nAdd New Product")
    id = input("Product ID: ")

    for product in inventory:
        if product["ID"] == id:
            print("Product ID already exists")
            return inventory

    name = input("Product Name: ")
    price = getValidPriceInput("Price: ")
    stock = getValidStockInput("Stock Quantity: ")

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
    found = False
    
    for product in inventory:
        if product['ID'] == id:
            print("\nProduct Found:")
            print("Name:", product["Name"])
            print("Current Stock:", product["Stock"], "\n")
            new_stock = getValidStockInput("New Stock Quantity: ")
            product["Stock"] = new_stock
            found = True
            break

    if found:
        print("\nStock updated successfully!\n")
    else:
        print("\nProduct not found\n")

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
            break

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

def getValidStockInput(prompt):
    while True:
        stock = input(prompt)
        if stock.isdigit():
            return int(stock)
        else:
            print("Error! Enter a non-negative integer.")

def getValidPriceInput(prompt):
    while True:
        price = input(prompt)
        try:
            if float(price) > 0:
                return f"${float(price):.2f}"

        except ValueError:
            pass
        print("Error! Enter a non-negative number.")

def exit(inventory, filename):
    save(inventory, filename)
    print("\nThank you for using Inventory Management System.\n"
            "Program terminated.\n")

# Main Program
filename = "inventory.json"

print("\n====================================================\n"
      "INVENTORY MANAGEMENT SYSTEM\n"
      "====================================================\n"
      )

inventory = load(filename)

menu()

actions = {
    1: display,
    2: add,
    3: update,
    4: search,
    5: save,
    6: exit
}

while True:
    try:
        option = int(input("Enter Option: "))

    except ValueError:
        print("Invalid input! Enter a number.\n")
        menu()
        continue

    if option == 5:
        actions[option](inventory, filename)

    elif option == 6:
        actions[option](inventory, filename)
        break

    elif option in actions:
        result = actions[option](inventory)

        if result is not None:
            inventory = result

    else:
        print("Invalid selection! Try again.")
        menu()
