n = int(input())
student_info_dic = {}

for elements in range(n):
    name = input()
    grade = float(input())

    if name not in student_info_dic:
        student_info_dic[name] = grade
    else:
        average_grade = (student_info_dic[name] + grade) / 2
        student_info_dic[name] = average_grade

for nam, aver_gr in student_info_dic.items():
    if float(aver_gr) >= 4.5:
        print(f"{nam} -> {aver_gr:.2f}")
