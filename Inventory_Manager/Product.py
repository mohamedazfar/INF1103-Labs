from abc import ABC, abstractmethod
from Supplier import Supplier

# Represents and manages a single product
class Product(ABC):
    
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self._product_id: str = product_id
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        self.supplier: Supplier = supplier

    def get_id(self) -> str:
        return self._product_id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def update_stock(self, quantity):
        self._stock = quantity

    def display_information(self):
        print("ID:", self._product_id)
        print("Name:", self._name)
        print(f"Price: ${self._price:.2f}")
        print("Stock:", self._stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass