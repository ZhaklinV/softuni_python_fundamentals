n = int(input())
pieces_data = {}

for i in range(n):
    piece, composer, key = input().split("|")
    pieces_data[piece] = [composer, key]

command = input()

while not command == "Stop":
    command = command.split("|")
    action = command[0]
    if action == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pieces_data:
            pieces_data[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif action == "Remove":
        piece = command[1]
        if piece in pieces_data:
            pieces_data.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in pieces_data:
            pieces_data[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for k,v in pieces_data.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
