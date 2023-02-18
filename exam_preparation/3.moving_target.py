targets = [int(x) for x in input().split()]
input_line = input()

while input_line != "End":
    command, index, value = input_line.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        radius = value
        start_index = index - radius
        end_index = index + radius

        if start_index < 0 or start_index > len(targets) or end_index < 0 or end_index > len(targets):
            print("Strike missed!")
        else:
            for indx in range(end_index, start_index - 1, -1):
                targets.pop(indx)

    input_line = input()

print(*targets, sep="|")
