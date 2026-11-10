from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Product import Product

# Manages a collection of products
class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def get_products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.get_id() == product_id:
                self.__products.remove(product)

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("--------------------------------------------")
        for product in self.__products:
            print(f"ID: {product.get_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()}", end="")
            if isinstance(product, PhysicalProduct):
                print(f" | Weight: {product.get_weight():.2f}kg ")
            elif isinstance(product, DigitalProduct):  
                print(f" | Download Size: {product.get_download_size():.2f}MB ")  
        print("--------------------------------------------\n")

    def get_next_id(self) -> str:
        highest=0
        for product in self.__products:
            id = product.get_id()
            if id.startswith("P") and id[1:].isdigit():
                highest = max(highest, int(id[1:]))
        return f"P{highest + 1:03d}"