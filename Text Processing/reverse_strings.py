word = input()

while not word == "end":
    reversed_word = word[::-1]  # -1 means that we start from the back forward
    print(f"{word} = {reversed_word}")

    word = input()