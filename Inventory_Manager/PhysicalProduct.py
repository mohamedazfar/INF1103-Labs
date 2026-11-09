from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

BASE_SHIPPING_FEE = 5.00
RATE_PER_KG = 2.00

# Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self._weight: float = weight

    def get_weight(self) -> float:
        return self._weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight:.2f}kg")

    def get_fulfilment_info(self) -> str:
        return("The product requires physical shipping")

    def calculate_shipping_cost(self) -> float:
        return (BASE_SHIPPING_FEE + (RATE_PER_KG * self._weight))