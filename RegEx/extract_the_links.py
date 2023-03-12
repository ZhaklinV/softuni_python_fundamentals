import re

command = input()

while command:
    regex = r'(?P<link>www\.[A-Za-z0-9]+[\-A-Za-z0-9]*(\.[a-z]+)+)'
    result = re.finditer(regex,command)
    for match in result:
        print(match.group('link'))
    command = input()
