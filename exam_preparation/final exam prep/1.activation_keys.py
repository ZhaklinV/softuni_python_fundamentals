activation_key = input()
command = input()

while not command == 'Generate':
    command = command.split('>>>')
    action = command[0]
    if action == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == 'Flip':
        start_index = int(command[2])
        end_index = int(command[3])
        lower_or_upper = command[1].lower()
        if lower_or_upper == "lower":
            range_to_lower = (activation_key[start_index:end_index]).lower()
            activation_key = activation_key[:start_index] + range_to_lower + activation_key[end_index:]
        elif lower_or_upper == 'upper':
            range_to_upper = (activation_key[start_index:end_index]).upper()
            activation_key = activation_key[:start_index] + range_to_upper + activation_key[end_index:]
        print(activation_key)

    elif action == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        item_to_slice = activation_key[start_index:end_index]
        activation_key = activation_key.replace(item_to_slice, '')
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
