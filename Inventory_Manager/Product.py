from abc import ABC, abstractmethod
from Supplier import Supplier

# Represents and manages a single product
class Product(ABC):
    
    def __init__(self, id: str, name: str, price: float, stock: int, supplier: Supplier):
        self._id: str = id
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        self._supplier: Supplier = supplier

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def get_supplier(self):
        return self._supplier

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