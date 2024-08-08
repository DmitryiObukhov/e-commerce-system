class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)

    def view_courses(self):
        for course in self.courses:
            print(course.name)
