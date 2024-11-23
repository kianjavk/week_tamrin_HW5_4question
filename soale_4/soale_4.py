# Person(parent class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Student(child class of Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"


# Teacher(child class of Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}"


# Course class for manage student list and courses
class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        if not self.students:
            return "No students enrolled yet."
        student_list = ', '.join([student.name for student in self.students])
        return f"Students enrolled in {self.course_name}: {student_list}"

    def display(self):
        return f"{self.course_name} is taught by {self.teacher.name}."