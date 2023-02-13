def fire(index, damage, ship_status):
    sunken = False
    if 0 <= index < len(ship_status):
        ship_status[index] -= damage
        if ship_status[index] <= 0:
            print("You won! The enemy ship has sunken.")
            sunken = True
    if sunken:
        return True


def defend(start_index, end_index, damage, ship):
    sunken = False
    if 0 <= start_index < len(ship) and 0 <= end_index < len(ship):
        for i in range(start_index, end_index + 1):
            ship[i] -= int(damage)
            if ship[i] <= 0:
                sunken = True
                print("You lost! The pirate ship has sunken.")
                break

    if sunken:
        return True


def repair(index, health, ship_st):
    if 0 <= index < len(ship_st):
        if ship_st[index] + health <= max_health_capacity:
            ship_st[index] += health
        else:
            ship_st[index] = max_health_capacity

    return ship_st


def status(max_health_capacity, pirate_ship_status):
    repair_border = 0.2 * max_health_capacity
    for_repair = [x for x in pirate_ship_status if x < repair_border]

    print(f"{len(for_repair)} sections need repair.")


pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health_capacity = int(input())

input_line = input()
stalemate = True

while input_line != "Retire":

    if "Fire" in input_line:
        command, index, damage = input_line.split()
        index, damage = int(index), int(damage)
        if fire(index, damage, warship_status):
            stalemate = False
            break

    elif "Defend" in input_line:
        command, start_index, end_index, damage = input_line.split()
        start_index, end_index, damage = int(start_index), int(end_index), int(damage)
        if defend(start_index, end_index, damage, pirate_ship_status):
            stalemate = False
            break

    elif "Repair" in input_line:
        command, index, health = input_line.split()
        index, health = int(index), int(health)
        repair(index, health, pirate_ship_status)

    elif "Status" in input_line:
        status(max_health_capacity, pirate_ship_status)

    input_line = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
