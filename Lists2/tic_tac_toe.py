def winning(first, second, third, x):
    player_win = False
    x = str(x)
    if first == [x, x, x] or second == [x, x, x] or third == [x, x, x]:
        player_win = True

    for i in range(0, 3):
        if first[i] == x and second[i] == x and third[i] == x:
            player_win = True
            if player_win:
                break

    if (first[0] == x and second[1] == x and third[2] == x) \
            or (first[2] == x and second[1] == x and third[0] == x):
        player_win = True

    if player_win:
        return True


first_row = input().split()
second_row = input().split()
third_row = input().split()
win = False

for player in range(1, 3):
    if winning(first_row, second_row, third_row, player):
        name_pl = {1: "First", 2: "Second"}
        print(f"{name_pl[player]} player won")
        win = True
        break

if not win:
    print("Draw!")
