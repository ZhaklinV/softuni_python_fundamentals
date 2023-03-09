import re

text = input()

regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

result = re.finditer(regex,text)
valid = [num.group() for num in result]
print(*valid)
