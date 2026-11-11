from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from Product import Product

def test_association(supplier1, pen, windows):
    print("Test Association")
    print("-----------------")

    # Display Supplier information for each product
    pen.supplier.display_information()
    windows.supplier.display_information()

    # Check is supplier still exists
    del supplier1
    pen.supplier.display_information()
    windows.supplier.display_information()

def test_aggregation(pen, inventoryA, inventoryB):
    print("\nTest Aggregation")
    print("-----------------")
  
    inventoryA.add_product(pen)
    inventoryA.remove_product("P1")
    inventoryA.display_all()
    pen.display_information()

    inventoryB.add_product(pen)
    inventoryB.display_all()
    
def test_composition(pen, windows, order1, order2):
    print("Test Composition")
    print("-----------------")
    
    order1.add_order_line(pen, 3)
    order1.add_order_line(windows, 1)

    for orderline in order1.order_lines:
        print(f"Product Name:{orderline.product.get_name()}, Quantity: {orderline.quantity}, Subtotal:${orderline.calculate_subtotal():.2f}")
    print(f"Order1 Total: ${order1.calculate_total():.2f}")
    
    order2.add_order_line(pen, 3)

    print(f"\nBefore:{len(order2.order_lines)}")
    order2.remove_order_line("P1")
    print(f"After:{len(order2.order_lines)}")

def show_product_details(product: Product, inventoryA: Inventory) -> None:
    print("\nTest Substitutability")
    print("-----------------")
    product.display_information()
    print(product.get_fulfilment_info())
    inventoryA.add_product(product)
    inventoryA.display_all()

def show_inventory(inventoryA: Inventory):
    print("\nTest Polymorphism")
    print("-----------------")
    for product in inventoryA.get_products():
        product.display_information()
        print(product.get_fulfilment_info())


#---------------------------------------------------------------------------
# Main function
supplier1 = Supplier("S1", "tom", "tom@gmail.com")
pen = PhysicalProduct("P1", "Pen", 2.5, 3, supplier1, 0.3)
windows = DigitalProduct("P2", "Windows", 150, 5, supplier1, 5.2)
inventoryA = Inventory()
inventoryB = Inventory()
order1 = Order("O1")
order2 = Order("O2")

test_association(supplier1, pen, windows)
test_aggregation(pen, inventoryA, inventoryB)
test_composition(pen, windows, order1, order2)
show_product_details(pen, inventoryA)
show_product_details(windows, inventoryA)
show_inventory(inventoryA)







