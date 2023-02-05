# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    input_num = int(input())
    if input_num % 2 == 0:
        even.append(input_num)
    else:
        odd.append(input_num)
    if input_num >= 0:
        positive.append(input_num)
    else:
        negative.append(input_num)

print(eval(input()))
