input_data = input()
products = {}

while input_data != "statistics":
    data = input_data.split(": ")
    key = data[0]
    value = int(data[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value
    input_data = input()

print("Products in stock:")

for product,quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
