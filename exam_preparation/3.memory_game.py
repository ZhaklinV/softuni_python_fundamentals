def is_index_in_range(index, cards_count):
    if 0 <= index < cards_count:
        return True
    return False


def valid_indexes(index1, index2, count_card):
    if (
        is_index_in_range(index1, count_card)
        and is_index_in_range(index2, count_card)
        and index1 != index2
    ):
        return True
    return False


elements_list = input().split()
command = input()
count_moves = 0

while command != "end":
    count_moves += 1

    index1, index2 = [int(num) for num in command.split()]

    if valid_indexes(index1,index2, len(elements_list)):
        if elements_list[index1] == elements_list[index2]:
            match = elements_list[index1]
            print(f"Congrats! You have found matching elements - {elements_list[index1]}!")
            elements_list.remove(match)
            elements_list.remove(match)

        else:
            print("Try again!")

    else:
        middle = int(len(elements_list) // 2)
        element_to_add = f"-{count_moves}a"
        elements_list.insert(middle, element_to_add)
        elements_list.insert(middle, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if not len(elements_list):
        print(f"You have won in {count_moves} turns!")
        exit(0)

    command = input()

if command == "end" and len(elements_list):
    print("Sorry you lose :(")
    print(*elements_list, sep=" ")
