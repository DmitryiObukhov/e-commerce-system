class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def view_students(self):
        for student in self.students:
            print(student.name)

    def view_courses(self):
        for course in self.courses:
            print(course.name)
