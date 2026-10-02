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
        print(f"{filename} found.\nInventory loaded successfully.")

    else:
        inventory = []
        with open(filename, "w") as file:
            inventory = json.dump(inventory, file)
    
    return inventory


# Main Program
filename = "inventory.json"

print("====================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("====================================================")

load(filename)


