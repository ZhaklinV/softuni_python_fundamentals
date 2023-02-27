# Write a program that reads a string from the console and replaces any sequence of the same letters with a single
# corresponding letter.

sequence = input()
result = ''

for i in range(len(sequence)):
    current = sequence[i]
    if i + 1 < len(sequence):
        if current != sequence[i + 1]:
            result += current
    else:
        result += sequence[-1]
print(result)
