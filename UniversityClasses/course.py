class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
