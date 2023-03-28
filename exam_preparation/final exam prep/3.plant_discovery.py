n = int(input())
plants_info = {}

for i in range(n):
    plant, rarity = input().split('<->')
    if plant in plants_info:
        plants_info[plant]['rarity'] = int(rarity)
        continue
    plants_info[plant] = plants_info.get(plant, {'rarity': int(rarity), 'rating': []})

command = input()

while not command == 'Exhibition':
    command = command.split()
    action = command[0]
    plant = command[1]

    if plant not in plants_info:
        print('error')
        command = input()
        continue

    if action == 'Rate:':
        rating = int(command[-1])
        plants_info[plant]['rating'].append(rating)

    elif action == 'Update:':
        new_rarity = int(command[-1])
        plants_info[plant]['rarity'] = new_rarity

    elif action == 'Reset:':
        plants_info[plant]['rating'] = []

    command = input()

print("Plants for the exhibition:")
for name, value in plants_info.items():
    rare = value['rarity']
    average_rating = 0
    if value['rating']:
        average_rating = sum(value['rating']) / len(value['rating'])
    print(f'- {name}; Rarity: {rare}; Rating: {average_rating:.2f}')
