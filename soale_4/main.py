class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}"


class Course:
    def __init__(self, course_name, teacher_name):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        if not self.students:
            return "No students enrolled yet."
        student_list = ', '.join([student.name for student in self.students])
        return f"Students enrolled in {self.course_name}: {student_list}"

    def display(self):
        return f"{self.course_name} is taught by {self.teacher_name}."

    # متد مقایسه course_name و teacher_name
    def compare_course(self, course_name, teacher_name):
        if self.course_name == course_name and self.teacher_name == teacher_name:
            return f"Number of students enrolled: {len(self.students)}"
        else:
            return "No match found for this course and teacher."


courses = {}

if __name__ == "__main__":
    id_list = []

    while True:
        try:
            p_name = input("Enter your name: ")
            if not p_name.isalpha():
                raise ValueError("Person name should contain only letters.")
            if not len(p_name)>2:
                raise ValueError("Person name should have at least 2 letters.")

            p_age = int(input("Your age: "))

            while True:
                print("1: Teacher")
                print("2: Student")
                choice = input("Choose an option: ").strip()
                if choice in ("1", "2"):
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            if choice == "1":
                subject1 = input("Enter your subject: ")
                teacher_obj = Teacher(p_name, p_age, subject1)
                print(teacher_obj)

            elif choice == "2":
                student_id = input("Enter your ID: ")
                if student_id in id_list:
                    raise ValueError("This ID is already registered.")
                else:
                    id_list.append(student_id)

                student_obj = Student(p_name, p_age, student_id)
                print(student_obj)

                course_name = input("Enter your course: ")
                teacher_name = input("Enter your teacher's name: ")

                if (course_name, teacher_name) in courses:
                    course_obj = courses[(course_name, teacher_name)]
                else:
                    course_obj = Course(course_name, teacher_name)
                    courses[(course_name, teacher_name)] = course_obj


                course_obj.add_student(student_obj)

                compare_result = course_obj.compare_course(course_name, teacher_name)
                print(compare_result)

                print(course_obj.display())
                print(course_obj.list_students())

            print("Do you wanna exit? Yes or No: ")
            x = input().lower()
            if x == "yes":
                print("Have a good day!")
                break
        except ValueError as e:
            print(f"An error occurred: {e}")
