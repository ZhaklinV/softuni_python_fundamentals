input_data = input()
database = {}

while input_data != "end":
    course_name, student_name = input_data.split(" : ")

    if course_name not in database:
        database[course_name] = []
    database[course_name].append(student_name)

    input_data = input()

for key, value in database.items():
    print(f"{key}: {len(database[key])}")
    for student in database[key]:
        print(f"-- {student}")
