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