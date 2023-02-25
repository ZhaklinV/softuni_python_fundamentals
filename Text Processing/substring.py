searching_str = input()
word = input()

while searching_str in word:
    word = word.replace(searching_str, '')

print(word)