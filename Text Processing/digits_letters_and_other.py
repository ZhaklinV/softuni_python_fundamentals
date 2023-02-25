text = input()
letter = ""
digits = ""
others = ''

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letter += ch
    else:
        others += ch

print(digits)
print(letter)
print(others)
