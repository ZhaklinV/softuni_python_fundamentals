waiting_people = int(input())
lift_current_state = list(map(int, input().split()))

for i in range(len(lift_current_state)):
    if waiting_people >= 4:
        if lift_current_state[i] == 0:
            lift_current_state[i] = 4
            waiting_people -= 4
        else:
            get_people = 4 - lift_current_state[i]
            lift_current_state[i] = get_people + lift_current_state[i]
            waiting_people -= get_people
    else:
        lift_current_state[i] += waiting_people
        waiting_people = 0


check = [int(x) for x in lift_current_state if x != 4]

if waiting_people == 0 and check:
    print("The lift has empty spots!")

elif waiting_people != 0 and not check:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(*lift_current_state)
