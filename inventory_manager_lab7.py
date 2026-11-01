import json
import os
from abc import ABC, abstractmethod

# Represents and manages a single product
class Product(ABC):
    
    def __init__(self, id, name, price, stock):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def update_stock(self, quantity):
        self._stock = quantity

    def display_information(self):
        print("ID:", self._id)
        print("Name:", self._name)
        print(f"Price: ${self._price:.2f}")
        print("Stock:", self._stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass

# Physical Product Class
class PhysicalProduct(Product):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight}kg")

    def get_fulfilment_info(self):
        print("The product requires physical shipping")

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, download_size):
        super().__init__(id, name, price, stock)
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size}MB")

    def get_fulfilment_info(self):
        print("The product is delivered digitally")

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
        print("\nCurrent Inventory")
        print("--------------------------------------------")
        for product in self.__products:
            print(f"ID: {product.get_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()} ")
        print("--------------------------------------------\n")

    def get_next_id(self):
        highest=0
        for product in self.__products:
            id = product.get_id()
            if id.startswith("P") and id[1:].isdigit():
                highest = max(highest, int(id[1:]))
        return f"P{highest + 1:03d}"
                
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
    id = inventory.get_next_id()
    print(f"Product ID: {id} ")
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
    print("-------------------------------------")
    product.display_information()
    print("-------------------------------------\n")

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


'''# Main Program
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
        print("Invalid selection! Try again.\n")
        show_menu()
'''

product1 = PhysicalProduct("P001", "Pen", 4.0, 2, 0.5)
product1.display_information()
product1.get_fulfilment_info()

product2 = DigitalProduct("P001", "Pen", 4.0, 2, 1000)
product2.display_information()
product2.get_fulfilment_info()

product3 = Product("P001", "Water", 5.0, 5)
product3.display_information()