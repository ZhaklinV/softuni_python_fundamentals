import math

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
best_student_attendances = 0

for i in range(number_of_students):
    count_student_attendances = int(input())
    current_bonus = count_student_attendances / total_number_of_lectures * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        best_student_attendances = count_student_attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {best_student_attendances} lectures.")
