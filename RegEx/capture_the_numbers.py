import re

command = input()
valid = []
while command:
    regex = r'\d+'

    result = re.findall(regex, command)
    if result:
        valid.append(" ".join(result))
    command = input()

print(*valid)
