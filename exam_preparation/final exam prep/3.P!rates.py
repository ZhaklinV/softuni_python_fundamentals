command = input()
targeted_cities = {}

while not command == 'Sail':
    cities, population, gold = command.split('||')
    gold = int(gold)
    population = int(population)
    if cities not in targeted_cities:
        targeted_cities[cities] = [gold, population]
    else:
        targeted_cities[cities][0] += gold
        targeted_cities[cities][1] += population

    command = input()

command = input()
while not command == "End":
    command = command.split("=>")
    action = command[0]
    if action == 'Plunder':
        town, people, gold = command[1:]
        targeted_cities[town][1] -= int(people)
        targeted_cities[town][0] -= int(gold)

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targeted_cities[town][0] <= 0 or targeted_cities[town][1] <= 0:
            targeted_cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == 'Prosper':
        town, gold = command[1:]
        if int(gold)<0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town][0] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {targeted_cities[town][0]} gold.")

    command = input()

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for key, value in targeted_cities.items():
        print(f'{key} -> Population: {value[1]} citizens, Gold: {value[0]} kg')

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
