import string

sequence = input().split()
total_sum = 0

for word in sequence:
    current_num = ''
    letter_in_front_of = ''
    letter_after = ''
    for ch in range(len(word)):
        if word[ch].isdigit():
            current_num += word[ch]
            if word[ch - 1].isalpha():
                letter_in_front_of = word[ch - 1]
            if word[ch + 1].isalpha():
                letter_after = word[ch + 1]
    current_num = int(current_num)

    position_front = string.ascii_lowercase.index(letter_in_front_of.lower()) + 1  #get position in alphabet,start from 1
    position_after = string.ascii_lowercase.index(letter_after.lower()) + 1

    if letter_in_front_of.isupper():
        current_num /= position_front
    elif letter_in_front_of.islower():
        current_num *= position_front

    if letter_after.isupper():
        current_num -= position_after
    elif letter_after.islower():
        current_num += position_after

    total_sum += current_num

print(f'{total_sum:.2f}')
