from helpers import check_price_input, check_stock_input
from Product import Product

def show_menu():
    print("-------------MENU-------------\n"
    "1. Display All Products\n"  
    "2. Add Product\n" 
    "3. Update Stock\n" 
    "4. Search Product\n" 
    "5. Save Inventory\n"
    "6. Exit\n"
    "------------------------------\n")

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
    product.display_product()

def exit_menu():
    print("\nThank you for using Inventory Management System.\n"
            "Program terminated.\n") 