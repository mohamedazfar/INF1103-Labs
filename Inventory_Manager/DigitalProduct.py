from Product import Product
from Supplier import Supplier

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size: float = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size:.2f}MB")

    def get_fulfilment_info(self):
        return("The product is delivered digitally")