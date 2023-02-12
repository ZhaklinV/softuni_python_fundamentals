items_list = input().split(", ")
input_line = input()

while input_line != "Craft!":
    if "Combine Items" in input_line:
        command, items = input_line.split(" - ")
        old_item, new_item = items.split(":")
        if old_item in items_list:
            index = items_list.index(old_item) + 1
            items_list.insert(index, new_item)

    else:
        command, item = input_line.split(" - ")
        if command == "Collect":
            if item not in items_list:
                items_list.append(item)

        elif command == "Drop":
            if item in items_list:
                items_list.remove(item)

        elif command == "Renew":
            if item in items_list:
                items_list.remove(item)
                items_list.append(item)

    input_line = input()

print(", ".join(items_list))
