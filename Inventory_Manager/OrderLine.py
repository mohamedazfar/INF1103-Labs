from Product import Product

class OrderLine():
    def __int__(self, product: Product, quantity: int):
        self._product: Product = product
        self._quantity: int = quantity

    def get_product(self) -> Product:
        return self._product

    def get_quantity(self) -> int:
        return self._quantity

    def calculate_subtotal(self) -> float:
        return self._product.get_price() * self._quantity
