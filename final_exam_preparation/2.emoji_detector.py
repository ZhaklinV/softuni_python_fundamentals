text = input()
digits = [int(digit) for digit in text if digit.isdigit()]
cool_threshold = 1
# emoji = []

for num in digits:
    cool_threshold *= num
print(f"Cool threshold: {cool_threshold}")

text = text.split()

emoji = [word for word in text if word.count(":") == 4 or word.count("**") == 2]

for el in emoji:
    if el.startswith(":") or el.startswith("**"):
        if len(el) - 4 >= 3:
            if el[2].upper():
                pass



# for word in text:
#     if word.count("::") == 2 or word.count("**")==2:
#         emoji.append(word)

print(emoji)
