neighborhood = list(map(int, input().split("@")))
command = input()
current_index = 0

while command != "Love!":
    command = command.split()
    length = int(command[1])
    current_index += length

    if current_index > len(neighborhood)-1:
        current_index = 0

    if neighborhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
        command = input()
        continue

    neighborhood[current_index] -= 2

    if neighborhood[current_index] <= 0:
        print(f"Place {current_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    not_celebrated = [x for x in neighborhood if x > 0]
    print(f"Cupid has failed {len(not_celebrated)} places.")
