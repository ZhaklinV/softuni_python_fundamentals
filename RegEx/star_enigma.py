import re

number_of_message = int(input())
attacked_planet = []
destroyed_planet = []
decrypted_text = ''

for i in range(number_of_message):
    encrypted_text = input()
    searched_letters = 'star'
    count_ch = len([char for char in encrypted_text if char.lower() in searched_letters])

    for symb in encrypted_text:
        true_symbol = chr(ord(symb) - count_ch)
        decrypted_text += true_symbol

regex = r'@(?P<planet>[A-Za-z]+)([^\-:@!>])*' \
        r'\:(?P<population>\d+)([^\-:@!>])*' \
        r'\!(?P<type>A|D)\!([^\-:@!>])*' \
        r'->(?P<count>\d+)'

valid_text = re.finditer(regex, decrypted_text)

for el in valid_text:
    current = el.groupdict()

    if current['type'] == 'A':
        attacked_planet.append(current['planet'])

    elif current['type'] == 'D':
        destroyed_planet.append(current['planet'])

print(f"Attacked planets: {len(attacked_planet)}")
[print(f"-> {x}") for x in sorted(attacked_planet)]

print(f"Destroyed planets: {len(destroyed_planet)}")
[print(f"-> {x}") for x in sorted(destroyed_planet)]
