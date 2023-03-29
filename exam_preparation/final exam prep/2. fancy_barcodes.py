import re

n = int(input())

for _ in range(n):
    input_line = input()
    regex = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
    match = re.findall(regex, input_line)

    if not match:
        print("Invalid barcode")
    else:
        for element in match:
            group_el = [el for el in element if el.isdigit()]
            if group_el:
                group_code = f''.join(group_el)
            else:
                group_code = '00'

            print(f"Product group: {group_code}")
