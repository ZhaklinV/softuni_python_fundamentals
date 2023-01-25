input_data = input()
courses = {}

while ':' in input_data:
    name, student_id, current_course = input_data.split(":")

    if current_course not in courses:
        courses[current_course] = {}
    courses[current_course][student_id] = name

    input_data = input()

searched_course = input_data
if "_" in searched_course:
    searched_course = searched_course.split("_")
    searched_course = ' '.join(searched_course)

for st_id, st_name in courses[searched_course].items():
    print(f'{st_name} - {st_id}')
