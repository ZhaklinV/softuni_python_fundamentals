def loot(command, treasure_chest):
    for item in command:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)

    return treasure_chest


def drop(command, treasure_chest):
    index = int(command[1])
    if 0 <= index < len(treasure_chest):
        current_item = treasure_chest[index]
        treasure_chest.remove(current_item)
        treasure_chest.append(current_item)

    return treasure_chest


def steal(command, treasure_chest):
    count = int(command[1])
    stolen_item = []
    for _ in range(count):
        stolen_item.insert(0, treasure_chest[-1])
        treasure_chest.pop(-1)
        if len(treasure_chest) == 0:
            break
    print(", ".join(stolen_item))
    return treasure_chest


def avarage_gain(treasure_chest):
    total_length = 0
    for item in treasure_chest:
        total_length += len(item)

    average = total_length / len(treasure_chest)
    return f"{average:.2f}"


treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()

    if "Loot" in command:
        command.remove("Loot")
        loot(command, treasure_chest)

    elif "Drop" in command:
        drop(command, treasure_chest)

    elif "Steal" in command:
        steal(command, treasure_chest)

    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:

    avarage_gain(treasure_chest)
    print(f"Average treasure gain: {avarage_gain(treasure_chest)} pirate credits.")
