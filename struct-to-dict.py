class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

s1 = Student("Rahul", 101, 87.5)

student_dict = s1.__dict__

print(student_dict)