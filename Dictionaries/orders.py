def printing(item_dict):
    for key, value in item_dict.items():
        total_price = value[0] * value[1]
        print(f"{key} -> {total_price:.2f}")


def product_info():
    data = input()
    products_dict = {}

    while data != "buy":
        data = data.split()
        name = data[0]
        price = float(data[1])
        quantity = int(data[2])
        if name not in products_dict:
            products_dict[name] = [price, quantity]
        else:
            products_dict[name] = [price, (products_dict[name][1] + quantity)]

        data = input()
    printing(products_dict)


product_info()
