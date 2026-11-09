from file_handler import load, save
from menu_functions import show_menu, add_product_menu, update_product_menu, search_product_menu 

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
        save(inventory, filename)
        print("\nThank you for using Inventory Management System.\n"
                    "Program terminated.\n")
        break

    else:
        print("Invalid selection! Try again.\n")
        show_menu()