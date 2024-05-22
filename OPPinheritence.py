class Person:
    def __init__(self, Name, Age, CID_Number):
        self.x = Name
        self.y = Age
        self.z = CID_Number

    def common_behavior(self, Walk, Talk, Eat, Sleep):
        self.a = Walk
        self.b = Talk
        self.c = Eat
        self.d = Sleep


class Teacher(Person):
    def __init__(self, Subject, Salary, Department, Designation):
        self.e = Subject
        self.f = Salary
        self.g = Department
        self.h = Designation

    def teacher_behavior(self, Teach, Grade_students, Attend_meeting):
        self.i = Teach
        self.j = Grade_students
        self.k = Attend_meeting

class student(Person):
    def __init__(self, Name, Age, CID_Number, Student_ID, Course, Year, GPA):
        super().__init__(Name, Age, CID_Number)
        self.l = Student_ID
        self.m = Course
        self.n = Year
        self.o = GPA

obj1 = student("Tashi",19,10903003423, 2230108, "ECE", "1st Year", 70)
print(f"The {self.x} is {self.y} years old bearing CID number {self.z}. He\'s Student ID is {obj1.l} and stuying {obj1.m} in {obj1.n}. He\'s aggregate is {obj1.o}. He ")

