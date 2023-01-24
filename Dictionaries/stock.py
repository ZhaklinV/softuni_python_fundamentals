input_data = input().split()
searched_products = input().split()

products = {}

for index in range(0, len(input_data), 2):
    keys = input_data[index]
    value = int(input_data[index + 1])
    products[keys] = value

for search_prod in searched_products:
    if search_prod in products:
        print(f"We have {products[search_prod]} of {search_prod} left")
    else:
        print(f"Sorry, we don't have {search_prod}")
