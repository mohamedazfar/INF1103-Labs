from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order

# Test Association
def test_association():
    print("Test Association")
    print("-----------------")

    supplier1 = Supplier("S1", "tom", "tom@gmail.com")
    pen = PhysicalProduct("P1", "Pen", 2.5, 3, supplier1, 0.3)
    windows = DigitalProduct("P2", "Windows", 150, 5, supplier1, 5.2)

    # Display Supplier information for each product
    pen.supplier.display_information()
    windows.supplier.display_information()

    # Check is supplier still exists
    del supplier1
    pen.supplier.display_information()
    windows.supplier.display_information()

# Test Aggregation
def test_aggregation():
    print("\nTest Association")
    print("-----------------")

    supplier1 = Supplier("S1", "tom", "tom@gmail.com")
    phone = PhysicalProduct("P3", "Iphone 18", 2000, 30, supplier1, 0.8)
    
    inventoryA = Inventory()
    inventoryA.add_product(phone)
    inventoryA.remove_product(phone)
    phone.display_information()

    inventoryB = Inventory()
    inventoryB.add_product(phone)
    inventoryB.display_all()
    
def test_composition():
    print("\nTest Composition")
    print("-----------------")
    order1 = Order("O1")

    supplier1 = Supplier("S1", "tom", "tom@gmail.com")
    pen = PhysicalProduct("P1", "Pen", 2.5, 3, supplier1, 0.3)
    windows = DigitalProduct("P2", "Windows", 150, 5, supplier1, 5.2)
    phone = PhysicalProduct("P3", "Iphone 18", 2000, 30, supplier1, 0.8)

    order1.add_order_line(pen, 3)
    order1.add_order_line(windows, 1)
    order1.add_order_line(phone, 2)

    for orderline in order1.order_lines:
        print(f"Product Name:{orderline.product.get_name()}, Quantity: {orderline.quantity}, Subtotal:${orderline.calculate_subtotal():.2f}")
    print(f"Order1 Total: ${order1.calculate_total():.2f}\n")

    order2 = Order("O2")
    order2.add_order_line(pen, 3)

    print(f"\nBefore:{len(order2.order_lines)}")
    order2.remove_order_line("P1")
    print(f"After:{len(order2.order_lines)}")

    

# Main
test_association()
test_aggregation()
test_composition()



'''for orderline in order.order_lines:
    orderline.get_product().display_information()
    print(f"Quantity: {orderline.get_quantity()}\n")

print(order.calculate_total())

order = Order("2")
order.add_order_line(product1, 1)

for orderline in order.order_lines:
    orderline.get_product().display_information()
    print(f"Quantity: {orderline.get_quantity()}\n")

print(order.calculate_total())'''






