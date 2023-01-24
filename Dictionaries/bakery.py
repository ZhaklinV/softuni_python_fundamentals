input_data = input().split()
products = {}

for index in range(0, len(input_data), 2):
    keys = input_data[index]
    value = int(input_data[index + 1])
    products[keys] = value

print(products)
