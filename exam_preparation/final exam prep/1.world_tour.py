all_stops = input()

while True:
    command = input()
    if command == 'Travel':
        break

    command = command.split(":")
    action = command[0]
    if action == 'Add Stop':
        index = int(command[1])
        new_string = command[2]
        if 0 <= index <= len(all_stops) - 1:
            current_string = all_stops[index:]
            all_stops = all_stops[0:index] + new_string + all_stops[index:]

    elif action == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])

        if 0 <= start_index <= len(all_stops) - 1 and 0 <= end_index <= len(all_stops) - 1:
            all_stops = all_stops[0:start_index] + all_stops[end_index + 1:]

    elif action == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")
