sequence = [int(num) for num in input().split()]
sequence.sort(key=lambda x: -x)

average = sum(sequence) / len(sequence)

first_five = [y for y in sequence if y > average]

if not first_five:
    print("No")
else:
    if len(first_five) > 5:
        for i in range(len(first_five)-1,4,-1):
            first_five.pop(i)

print(*first_five)