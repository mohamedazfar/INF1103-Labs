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

    def display_info(self):
        print("-------------------------------------")
        print("ID:", self.__id)
        print("Name:", self.__name)
        print(f"Price:, ${self.__price}")
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
            print(f"ID: {product.get_id()} | Name: {product.get_name()} | Price: ${product.get_price()} | Stock: {product.get_stock()} ")
        print("--------------------------------------------\n")

# File Handling
def load(filename):
    inventory = Inventory()

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)              
        except json.JSONDecodeError:
            data = []
        print(f"{filename} found.\nInventory loaded successfully.\n")        
    
    else:
        data = []
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    for item in data:
        product = Product(item["ID"], item["Name"], item["Price"], item["Stock"])
        inventory.add_product(product)
    
    return inventory

def save(inventory, filename):
    data = []
    for product in inventory.get_products():
        data.append({
            "ID": product.get_id(),
            "Name": product.get_name(),
            "Price": product.get_price(),
            "Stock": product.get_stock()
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("\nSaving inventory...\n"
          f"Inventory saved successfully to {filename}.\n")

# Menu option functions
def add_product_menu(inventory):
    print("\nAdd New Product")
    id = input("Product ID: ")
    product = inventory.search_product(id)

    if product is not None:
        print("Product ID already exists")
        return

    name = input("Product Name: ")
    price = check_price_input("Price: ")
    stock = check_stock_input("Stock Quantity: ")

    product = Product(id, name, price, stock)
    inventory.add_product(product)
    print("\nProduct added successfully!\n")
    
def update_product_menu(inventory):
    print("\nUpdate Stock")
    id = input("Enter Product ID: ")
    product = inventory.search_product(id)
    
    if product is None:
        print("\nProduct not found\n")
        return
    
    print("\nProduct Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock(), "\n")
    quantity = check_stock_input("New Stock Quantity: ")
    product.update_stock(quantity)        
    print("\nStock updated successfully!\n")
    
def search_product_menu(inventory):
    print("\nSearch Product")
    id = input("Enter Product ID: ") 
    product = inventory.search_product(id)       

    if product is None:
        print("\nProduct not found.\n")
        return
    
    print("\nProduct Found")
    product.display_info()

# Helper functions
def show_menu():
    print("-------------MENU-------------\n"
    "1. Display All Products\n"  
    "2. Add Product\n" 
    "3. Update Stock\n" 
    "4. Search Product\n" 
    "5. Save Inventory\n"
    "6. Exit\n"
    "------------------------------\n")

def check_stock_input(prompt):
    while True:
        stock = input(prompt)
        if stock.isdigit():
            return int(stock)
        print("Error! Enter a non-negative integer.")

def check_price_input(prompt):
    while True:
        price = input(prompt)
        try:
            if float(price) > 0:
                return round(float(price), 2)
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
show_menu()

while True:
    option = input("Enter Option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product_menu(inventory)

    elif option == "3":
        update_product_menu(inventory)

    elif option == "4":
        search_product_menu(inventory)

    elif option == "5":
        save(inventory, filename)

    elif option == "6":
        exit(inventory, filename)
        break

    else:
        print("Invalid selection! Try again.")
        show_menu()
