employees_power = [int(input()) for _ in range(3)]  # the number of students that each employee can help per hour
total_per_hour = sum(employees_power)

student_count = int(input())
hour = 0

while student_count != 0:
    if total_per_hour <= student_count:
        student_count -= total_per_hour
    else:
        student_count = 0
    hour += 1

    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")
