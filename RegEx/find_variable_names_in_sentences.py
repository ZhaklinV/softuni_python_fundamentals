import re

text = input()
pattern = r'\b\_(?P<variable>[A-Za-z0-9]+)\b'

result = re.finditer(pattern, text)

valid = [match.group('variable') for match in result]

print(','.join(valid))
