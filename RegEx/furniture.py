import re

command = input()

furniture = {}
total_price = 0

print("Bought furniture:")
while not command == 'Purchase':
    pattern = r'>>(?P<fur_name>[A-Za-z]+)<<(?P<price>\d+[\.\d+]*)!(?P<quantity>\d+)\b'
    result = re.finditer(pattern, command)
    for match in result:
        furniture = match.groupdict()
        name, price, quantity = furniture["fur_name"], float(furniture['price']), int(furniture['quantity'])
        current_price = price * quantity
        total_price += current_price
        print(f"{name}")

    command = input()

print(f"Total money spend: {total_price:.2f}")
