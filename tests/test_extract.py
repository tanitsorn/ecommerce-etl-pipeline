from python.extract.extract_data import extract_all
customers, orders, order_items, products = extract_all()

print("CUSTOMERS")
print(customers.head())

print("\nORDERS")
print(orders.head())

print("\nORDER ITEMS")
print(order_items.head())

print("\nPRODUCTS")
print(products.head())

