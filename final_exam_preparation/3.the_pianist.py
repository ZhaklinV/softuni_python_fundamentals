number_of_pieces = int(input())
pieces = []

for num in range(number_of_pieces):
    pieces.append(input().split("|"))

command = input()

while command != "Stop":
    command = command.split("|")

    for piece in pieces:

        if command[0] == "Add":
            command.remove('Add')
            if command[0] in piece:
                print(f"{command[0]} is already in the collection!")
            else:
                pieces.append(command)
                print(f"{command[0]} by {command[1]} in {command[2]} added to the collection!")

        elif command[0] == 'Remove':
            command.remove('Remove')
            if command in piece:
                pieces.remove(command)
                print(f"Successfully removed {command[0]}!")
            else:
                print(f"Invalid operation! {command[0]} does not exist in the collection.")

        elif command[0] == 'ChangeKey':
            command.remove('ChangeKey')
            if command in piece:
                index= pieces.index(command)
                pieces[index][2] = command[2]
                print(f"Changed the key of {command[0]} to {command[2]}!")
            else:
                print(f"Invalid operation! {command[0]} does not exist in the collection.")

        command= input()


for elem in pieces:
    name, composer, key = elem[0], elem[1], elem[2]
    print(f"{name} -> Composer: {composer}, Key: {key}")