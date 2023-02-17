energy = int(input())
command = input()
out_of_energy = False
count_won_battle = 0

while command != "End of battle":
    distance = int(command)

    if energy - distance < 0:
        out_of_energy = True
        break
    else:
        energy -= distance
        count_won_battle += 1
        if count_won_battle % 3 == 0:
            energy += count_won_battle

    command = input()

if out_of_energy:
    print(f"Not enough energy! Game ends with {count_won_battle} won battles and {energy} energy")
else:
    print(f"Won battles: {count_won_battle}. Energy left: {energy}")
