# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

input_words = input()
char_dict = {}

for ch in input_words:
    if ch == " ":
        continue
    elif ch not in char_dict:
        char_dict[ch] = 0
    char_dict[ch] += 1

for key,value in char_dict.items():
    print(f"{key} -> {value}")
