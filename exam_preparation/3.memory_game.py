elements_list = input().split()
command = input()
count_moves = 0

while command != "end":
    count_moves += 1
    moves = [int(num) for num in command.split()]
    index1, index2 = moves[0], moves[1]
    middle = int(len(elements_list) // 2)
    out_of_range = [index for index in moves if index < 0 or index >= len(elements_list)]

    if out_of_range or index1 == index2:
        elements_list.insert(middle, f"-{count_moves}a")
        elements_list.insert(middle, f"-{count_moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements_list[index1] == elements_list[index2]:
        match = elements_list[index1]
        print(f"Congrats! You have found matching elements - {elements_list[index1]}!")
        elements_list.remove(match)
        elements_list.remove(match)

    elif elements_list[index1] != elements_list[index2]:
        print("Try again!")


    if not len(elements_list):
        print(f"You have won in {count_moves} turns!")
        break

    command = input()

if command == "end" and len(elements_list):
    print("Sorry you lose :(")
    print(*elements_list, end=" ")
