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

def save(product, filename):
    inventory = load(filename)
    inventory.append(product)

    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)

    print("Saving inventory before exit...\n"
          "Inventory saved successfully.")


# Main Program
filename = "inventory.json"

print("====================================================\n"
      "INVENTORY MANAGEMENT SYSTEM\n"
      "====================================================\n"
      )

load(filename)

print("-------------MENU-------------\n"
"1. Display All Products\n"  
"2. Add Product\n" 
"3. Update Stock\n" 
"4. Search Product\n" 
"5. Save Inventory\n"
"6. Exit\n"
"------------------------------\n"
)

product  = {
    "ID": "P003",
    "Name": "Keyboard",
    "Price": "$45.00",
    "Stock": 25
}

save(product, filename)
