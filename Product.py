# Represents and manages a single product
class Product:
    def __init__(self, id, name, price, stock):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

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

    def display_product(self):
        print("-------------------------------------")
        print("ID:", self.__id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)
        print("-------------------------------------\n")