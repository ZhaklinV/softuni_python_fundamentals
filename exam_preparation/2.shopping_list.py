initial_list = input().split("!")
input_line = input()
final_list = initial_list.copy()

while input_line != "Go Shopping!":

    if "Correct" in input_line:
        command, old_item, new_item = input_line.split()
        if old_item in final_list:
            index = final_list.index(old_item)
            final_list[index] = new_item

    else:
        command, item = input_line.split()
        if command == "Urgent":
            if item not in final_list:
                final_list.insert(0, item)

        elif command == "Unnecessary":
            if item in final_list:
                final_list.remove(item)

        elif command == "Rearrange":
            if item in final_list:
                final_list.remove(item)
                final_list.append(item)

    input_line = input()

print(", ".join(final_list))
