from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order

# Test Association
print("Test Association")
print("-----------------")

supplier1 = Supplier("S1", "tom", "tom@gmail.com")
pen = PhysicalProduct("P1", "Pen", 2.5, 3, supplier1, 0.3)
windows = DigitalProduct("P2", "Windows", 150, 5, supplier1, 5.2)

pen.supplier.display_information()
windows.supplier.display_information()

del supplier1
pen.supplier.display_information()
windows.supplier.display_information()


'''product3 = PhysicalProduct("P3", "Ruler", 3.5, 8, supplier1, 0.1)'''

'''inventoryA = Inventory()
inventoryA.add_product(product1)
inventoryA.remove_product(product1)
product1.display_information()'''

'''order = Order("1")'''

'''order.add_order_line(product1, 1)
order.add_order_line(product2, 1)
order.add_order_line(product3, 1)

for orderline in order.order_lines:
    orderline.get_product().display_information()
    print(f"Quantity: {orderline.get_quantity()}\n")

print(order.calculate_total())

order = Order("2")
order.add_order_line(product1, 1)

for orderline in order.order_lines:
    orderline.get_product().display_information()
    print(f"Quantity: {orderline.get_quantity()}\n")

print(order.calculate_total())
'''





