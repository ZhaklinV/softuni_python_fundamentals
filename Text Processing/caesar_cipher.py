# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII
# table. For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

input_text = input()
encrypted_text = ''

for ch in input_text:
    new_char = (ord(ch) + 3)
    encrypted_text += chr(new_char)

print(encrypted_text)
