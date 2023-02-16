command = input()
to_do_list = [0]*10

while command != "End":
    importance,note = command.split("-")
    importance = int(importance)
    index = importance-1
    to_do_list[index] = note
    command = input()

final_list = [note for note in to_do_list if note != 0]
print(final_list)
