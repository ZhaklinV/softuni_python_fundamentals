import re

input_line = input()
cal_per_day = 2000
total_cal = 0

regex = r'(#|\|)(?P<name>[A-Za-z ]+(\s[A-Za-z]+)?)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1'

match = [object_.groupdict() for object_ in re.finditer(regex, input_line)]

if not match:
    print("You have food to last you for: 0 days!")

else:
    for el in match:
        total_cal += int(el['calories'])

    days = total_cal // cal_per_day
    print(f"You have food to last you for: {days} days!")

    if days > 0:
        for data in match:
            print(f"Item: {data['name']}, Best before: {data['date']}, Nutrition: {data['calories']}")
