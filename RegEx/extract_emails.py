import re

text = input()

pattern = r'\s(?P<email>([A-Za-z0-9]+[A-Za-z0-9\-\.\_]*)\@([A-Za-z]+[A-Za-z\-]+(\.[A-Za-z\-]*)+))\b'

result = re.finditer(pattern,text)

for match in result:
    print(match.group('email'))
