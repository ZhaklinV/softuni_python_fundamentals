class Class:
    __students_count = 22
    students = list()
    grades = list()

    def __init__(self, name):
        self.name = name
        self.current_count = 0
        self.average = 0

    def add_student(self, name: str, grade: float):
        if self.__students_count > self.current_count:
            self.students.append(name)
            self.grades.append(grade)
            self.current_count += 1

    def get_average_grade(self):
        self.average = sum(self.grades) / len(self.grades)
        return f"{self.average}"

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.average:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
print
print
