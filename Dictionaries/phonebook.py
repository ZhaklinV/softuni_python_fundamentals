info = input()
phonebook = {}

while "-" in info:
    name, phone_number = info.split("-")
    phonebook[name] = phone_number

    info = input()

n = int(info)

for i in range(n):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:

        print(f"{searched_name} -> {phonebook[searched_name]}")
