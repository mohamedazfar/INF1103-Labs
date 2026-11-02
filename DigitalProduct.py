from Product import Product

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, download_size):
        super().__init__(id, name, price, stock)
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size:.2f}MB")

    def get_fulfilment_info(self):
        return("The product is delivered digitally")