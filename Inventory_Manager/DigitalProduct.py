from Product import Product
from Supplier import Supplier

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(id, name, price, stock, supplier)
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size:.2f}MB")

    def get_fulfilment_info(self):
        return("The product is delivered digitally")