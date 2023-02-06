input_num = list(map(int, input().split()))

left_time = 0
right_time = 0

middle = len(input_num) // 2  # --> the middle of the list

for i in range(middle):
    left_time += (input_num[i])
    if (input_num[i]) == 0:
        left_time *= 0.8

for j in range(len(input_num) - 1, middle, -1):
    right_time += (input_num[j])
    if (input_num[j]) == 0:
        right_time *= 0.8

winner = ""
total_time = 0
if left_time < right_time:
    winner = "left"
    total_time = left_time
else:
    winner = "right"
    total_time = right_time
print(f"The winner is {winner} with total time: {total_time:.1f}")
