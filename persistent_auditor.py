'''
1. read previous information / if no file, then create new file
2. use [] to store every valid transaction amount entered
3. when user quits, save the final total and the transaction history to txt file
4. create a load_inventory() and save_inventory function
'''

import os

def load_inventory():

    file_name = "inventory.txt"

    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            print("\nNo Current Orders found. \n")
            
    else:
        with open(file_name, "r") as file:
            orders = file.readlines()

        print("\nCurrent Orders:\n")
        for order in orders:
            print(order, end="")

        return orders

load_inventory()