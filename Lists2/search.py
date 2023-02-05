# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them. After that, you should filter out only
# the strings that include the given word and print that list too.

n = int(input())
input_word = input()

list_of_words = []
filtered_list = []

for i in range(n):
    input_str = input()
    list_of_words.append(input_str)

    if input_word in list_of_words[i]:
        filtered_list.append(list_of_words[i])

print(list_of_words)
print(filtered_list)
