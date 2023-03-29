import re

input_line = input()
mirror_word = {'valid':[]}

regex = r'([@|#])(?P<first>[A-Za-z]{3,})\1{2}(?P<second>[A-Za-z]{3,})\1'

match = [el.groupdict() for el in re.finditer(regex, input_line)]

if not match:
    print("No word pairs found!")
else:
    print(f"{len(match)} word pairs found!")

for element in match:
    first = element['first']
    second = element['second']
    if first == second[::-1]:
        mirror_word['valid'].append(f'{first} <=> {second}')

if not mirror_word['valid']:
    print("No mirror words!")

else:
    print("The mirror words are:")
    print(', '.join(mirror_word['valid']))

