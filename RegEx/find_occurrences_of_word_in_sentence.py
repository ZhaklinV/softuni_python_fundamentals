import re

sentence = input().lower()
word = input().lower()

pattern = rf'\b{word}\b'

result = len(re.findall(pattern,sentence))

print(result)
