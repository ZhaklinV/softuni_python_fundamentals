message = input()
command = input()
while not command == 'Reveal':
    command = command.split(":|:")
    action = command[0]

    if action == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]

    elif action == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            substring = substring[::-1]
            message += substring
        else:
            print('error')
            command = input()
            continue

    elif action == 'ChangeAll':
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
