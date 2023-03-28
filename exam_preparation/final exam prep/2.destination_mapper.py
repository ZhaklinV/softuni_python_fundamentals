import re

input_line = input()
travel_points = 0
destinations = []
regex = r'(=|\/)(?P<place>[A-Z][A-Za-z]+)\1'

match = [el.groupdict() for el in re.finditer(regex, input_line)]

for current in match:
    current_destination = current['place']
    if len(current_destination) >= 3:
        travel_points += len(current_destination)
        destinations.append(current_destination)

print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {travel_points}")
