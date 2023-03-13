import re

command = input()
total_income = 0

while not command == 'end of shift':
    regex = r'(%)(?P<name>[A-Z][a-z]+)(%)([^\|\$\%\.]*)' \
            r'(<)(?P<product>\w+)(>)([^\|\$\%\.]*)(\|)' \
            r'(?P<count>\d+)(\|)([^\|\$\%\.]*)' \
            r'(?P<price>[1-9]+[.0-9]*)\$'
    result = re.finditer(regex, command)
    for el in result:

        current_match=el.groupdict()
        count=int(current_match['count'])
        price=float(current_match['price'])
        current_price= count*price
        total_income+=current_price
        print(f"{current_match['name']}: {current_match['product']} - {current_price:.2f}")

    command = input()

print(f"Total income: {total_income:.2f}")
