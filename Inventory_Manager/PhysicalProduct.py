from Product import Product
from CanBeShipped import CanBeShipped

BASE_SHIPPING_FEE = 5.00
RATE_PER_KG = 2.00

# Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight:.2f}kg")

    def get_fulfilment_info(self):
        return("The product requires physical shipping")

    def calculate_shipping_cost(self):
        return (BASE_SHIPPING_FEE + (RATE_PER_KG * self._weight))