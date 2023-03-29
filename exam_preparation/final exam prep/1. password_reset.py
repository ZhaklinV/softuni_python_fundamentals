input_string = input()
command = input()
new_string = ''

while not command == "Done":
    if command == 'TakeOdd':
        for i in range(1, len(input_string), 2):
            new_string += input_string[i]
        input_string = new_string
        print(new_string)

    else:
        command = command.split()
        action = command[0]

        if action == 'Cut':
            index, length = int(command[1]), int(command[2])
            current_substring = input_string[index:index + length]
            input_string = input_string.replace(current_substring, '', 1)
            print(input_string)

        elif action == 'Substitute':
            substring, substitute = command[1], command[2]
            if substring not in input_string:
                print("Nothing to replace!")
            else:
                input_string = input_string.replace(substring, substitute)
                print(input_string)

    command = input()

print(f"Your password is: {input_string}")