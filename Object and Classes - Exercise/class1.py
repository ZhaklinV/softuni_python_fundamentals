class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.grades = list()

    def add_student(self, name: str, grade: float):
        if self.__students_count > len(self.students):
            self.students.append(str(name))
            self.grades.append(float(grade))

    def get_average_grade(self):
        average = f"{(sum(self.grades) / len(self.grades)):.2f}"
        return float(average)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self)}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
