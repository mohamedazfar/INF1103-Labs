from file_handler import load, save
from menu_functions import show_menu, add_product_menu, update_product_menu, search_product_menu 
from Supplier import Supplier
# Main Program
filename = "inventory.json"

print("\n====================================================\n"
      "INVENTORY MANAGEMENT SYSTEM\n"
      "====================================================\n"
      )

inventory = load(filename)
default_supplier = Supplier("S1", "Supplier1", "supplier1@gmail.com")
show_menu()

while True:   
    option = input("Enter Option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product_menu(inventory, default_supplier)

    elif option == "3":
        update_product_menu(inventory)

    elif option == "4":
        search_product_menu(inventory)

    elif option == "5":
        save(inventory, filename)

    elif option == "6":
        save(inventory, filename)
        print("\nThank you for using Inventory Management System.\n"
                    "Program terminated.\n")
        break

    else:
        print("Invalid selection! Try again.\n")
        show_menu()