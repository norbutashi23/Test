# Base class Person
class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Derived class Student
class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Derived class Teacher
class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Create objects
student = Student(name="Tashi Norbu", age=20, cid_number="10903003423", student_id="02230108", course="ECE", year=2, gpa=3.4)
teacher = Teacher(name="Sonam", age=45, cid_number="1090300684", subject="Mathematics", salary=60000, department="Math", designation="Professor")

# Call common methods
student.walk()
student.talk()
student.eat()
student.sleep()

teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()

# Call student specific methods
student.study()
student.attend_class()
student.write_exam()

# Call teacher specific methods
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()

