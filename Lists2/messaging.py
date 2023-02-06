input_numbers = input().split()
input_string = input()

message = []

for num in input_numbers:
    sum_of_digits = 0
    for digit in num:
        sum_of_digits += int(digit)

    index = sum_of_digits % len(input_string)
    message.append(input_string[index])
    input_string= input_string.replace(input_string[index],"",1) # replace (old index, new char, count)

print(*message, sep="")
