import re

participants = input().split(', ')
command = input()
racers = {}

while not command == 'end of race':
    digit = []
    name_regex = r'[^\W\d_]'
    digit_regex = r'[\d]'
    valid_names = re.findall(name_regex, command)
    valid_num = [int(dig) for dig in re.findall(digit_regex, command)]
    name = "".join(valid_names)
    distance = sum(valid_num)
    if name in participants and name not in racers:
        racers[name] = distance
    elif name in participants and name in racers:
        racers[name] += distance

    name = ''
    command = input()

sort_racers = sorted(racers.items(), key=lambda x: x[1], reverse=True)
counter = 1
for key in sort_racers:
    places = {1: '1st', 2: '2nd', 3: '3rd'}
    if counter == 4:
        break
    else:

        print(f"{places.get(counter)} place: {key[0]}")
        counter += 1
