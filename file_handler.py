import os
import json
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

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
        if item["Product Type"] == "Physical":
            product = PhysicalProduct(item["ID"], item["Name"], item["Price"], item["Stock"], item["Weight"])
        elif item["Product Type"] == "Digital":
            product = DigitalProduct(item["ID"], item["Name"], item["Price"], item["Stock"], item["Download Size"])
        inventory.add_product(product)
    
    return inventory

def save(inventory, filename):
    data = []
    for product in inventory.get_products():
        row = {
            "ID": product.get_id(),
            "Name": product.get_name(),
            "Price": product.get_price(),
            "Stock": product.get_stock()
        }
        
        if isinstance(product, PhysicalProduct):
            row["Product Type"] = "Physical"
            row["Weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            row["Product Type"] = "Digital"
            row["Download Size"] = product.get_download_size()
        
        data.append(row)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("\nSaving inventory...\n"
          f"Inventory saved successfully to {filename}.\n")