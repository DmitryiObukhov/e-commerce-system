from UniversityClasses.course import Course
from UniversityClasses.student import Student
from UniversityClasses.university import University

uni = University("Harvard")

maths = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

uni.add_course(maths)
uni.add_course(physics)

alice = Student("Alice", "S101")

uni.add_student(alice)

alice.enroll(maths)
# results
print("Alice's courses:")
alice.view_courses()

print("University's students:")
uni.view_students()

print("University's courses:")
uni.view_courses()
