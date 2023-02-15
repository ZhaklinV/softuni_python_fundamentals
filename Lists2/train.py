count_wagons = int(input())
command = input()
train = [0] * count_wagons

while command != "End":
    current_command = command.split()[0]
    problem = current_command[0]
    if problem == "add":
        train[-1] += int(current_command[1])
    elif problem == 'insert':
        people = int(current_command[2])
        index = int(current_command[1])
        train[index] += people
    elif problem == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] -= people

    command = input()

print(train)
