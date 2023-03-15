import re

text = input()
regex = re.compile(r'(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1')
result = list(regex.finditer(text))

sum_threshold = 1
for ch in text:
    if ch.isdigit():
        sum_threshold *= int(ch)

print(f"Cool threshold: {sum_threshold}")
print(f'{len(result)} emojis found in the text. The cool ones are:')

sum_of_ascii_letters = 0
for valid in result:
    sum_of_ascii_letters = sum([ord(letter) for letter in valid['emoji']])

    if sum_of_ascii_letters >= sum_threshold:
        print(valid[0])

