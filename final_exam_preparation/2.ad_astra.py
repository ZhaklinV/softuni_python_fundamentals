input_line = input().split("|")
total_cal = 0
cal_per_day = 2000
product_available = []

for i in range(len(input_line)):
    if "#" in input_line[i]:
        for ch in input_line[i]:
            if ch == "#":
                ch.replace("#",'')
        input_line.remove('')

    if input_line[i].isalpha() and input_line.count("/") == 2 and input_line[i + 2].isdigit():
        name, expiration_data, calories = input_line[i], input_line[i + 1], int(input_line[i + 2])
        product_available.append(name)
        product_available.append(expiration_data)
        product_available.append(calories)
        i = i + 3

print(product_available)

# for item in input_line:
#     item_is_match = False
#     index = input_line.index(item)
#     current_items = ""
#
#     if "#" in item:
#         current_items = item.split("#")
#
#     elif "|" in item:
#         current_items = item.split("|")
#
#     else:
#         count = 0
#         while count != 2:
#             if "/" in item:
#                 count += 1
#             else:
#                 break
#             if count == 2:
#                 item_is_match = True
#
#     if item_is_match:
#         product_available = [current for current in current_items if current != ""]
#
# for j in range(0, len(product_available),3):
#     name = product_available[j]
#     expiration_data = product_available[j+1]
#     calories = int(product_available[j+2])
#
#     total_cal += calories
#
# days = total_cal / cal_per_day
#
# print(f"You have food to last you for: {days} days!")
#
# for i in range(0, len(product_available) + 1, 3):
#     print(f"Item: {i}, Best before: {i + 1}, Nutrition: {i + 2}")
