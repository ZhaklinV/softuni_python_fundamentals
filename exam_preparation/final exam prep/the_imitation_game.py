encrypted_message = input()
command = input()
decrypted_message = encrypted_message

while command != "Decode":
    command = command.split('|')
    action = command[0]
    if action == 'Move':
        n = int(command[1])
        decrypted_message = decrypted_message[n:] + decrypted_message[:n]

    elif action == 'Insert':
        index, value = int(command[1]), command[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

    elif action == 'ChangeAll':
        substring, replacement = command[1], command[2]
        decrypted_message=decrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {decrypted_message}")
