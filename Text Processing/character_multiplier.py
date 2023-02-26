words = input().split()
total_sum = 0
first_word = words[0]
second_word = words[1]

min_length = min(len(first_word), len(second_word))
count_ch_longer_word = max(len(first_word), len(second_word))

for i in range(min_length):
    first = ord(first_word[i])
    second = ord(second_word[i])

    total_sum += first * second

for index in range(min_length, count_ch_longer_word):
    if len(first_word) > len(second_word):
        current_char = first_word[index]
    else:
        current_char = second_word[index]

    total_sum += ord(current_char)

print(total_sum)
