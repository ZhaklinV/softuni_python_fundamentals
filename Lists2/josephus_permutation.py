people_in_circle = input().split()
k = int(input())
result = []
counter = 0
index = 0

while people_in_circle:
    counter += 1
    if counter % k != 0:
        index += 1
    elif counter % k == 0:
        result.append(people_in_circle[index])
        people_in_circle.pop(index)

    if index >= len(people_in_circle):
        index = 0

print(f'[{",".join(result)}]')

