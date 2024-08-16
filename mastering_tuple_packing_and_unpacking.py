#Task 1
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Tim", "Keyboard", 1),
    ("Carol", "USB Thumbstick", 3)
]
def orders_format(order_list):
    print("List of Orders\n")
    for order in order_list:
        name, item, quantity = order
        print(f"--Name: {name}\n     Item: {item}\n     Quantity: {quantity}")

orders_format(orders)