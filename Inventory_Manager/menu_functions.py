from helpers import check_float_input, check_int_input, check_str_input
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

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
def add_product_menu(inventory, supplier):
    print("\nAdd New Product")
    id = inventory.get_next_id()
    print(f"Product ID: {id} ")
    name = input("Product Name: ")
    price = check_float_input("Price: ")
    stock = check_int_input("Stock Quantity: ")
    product_type = check_str_input("Product Type (Physical/Digital): ")

    if product_type == "physical":
        weight = check_float_input("Weight: ")
        product = PhysicalProduct(id, name, price, stock, supplier, weight)
    elif product_type == "digital":
        download_size = check_float_input("Download Size: ")
        product = DigitalProduct(id, name, price, stock, supplier, download_size)

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
    quantity = check_int_input("New Stock Quantity: ")
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