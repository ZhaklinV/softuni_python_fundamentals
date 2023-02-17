targets = [int(x) for x in input().split()]
command = input()
indices = []

while command != "End":
    index = int(command)

    if 0 <= index < len(targets):
        if index not in indices:
            indices.append(index)

            for i in range(len(targets)):
                if i != index and targets[i] != -1:
                    if targets[i] > targets[index]:
                        targets[i] -= targets[index]
                    elif targets[i] <= targets[index]:
                        targets[i] += targets[index]
            targets[index] = -1
    command = input()

print(f"Shot targets: {targets.count(-1)} -> ", end ="")
print(*targets,sep=" ")
