import re

text = input()

pattern = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'

result = re.finditer(pattern,text)

valid = [match.group() for match in result]
print(", ".join(valid))
