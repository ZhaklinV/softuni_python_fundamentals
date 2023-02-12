health = 100
bitcoins = 0

dungeon_rooms = input().split('|')
is_die = False

for room in dungeon_rooms:
    command, number = room.split()
    number = int(number)

    if command == "potion":
        diff = 0
        if number + health < 100:
            health += number
            diff = number
        else:
            diff = 100 - health
            health = 100

        print(f"You healed for {diff} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            index = dungeon_rooms.index(room) + 1
            print(f"Best room: {index}")
            is_die = True
            break

if not is_die:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
