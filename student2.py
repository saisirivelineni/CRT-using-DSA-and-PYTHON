class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def display(self):
        print(self.name, self.roll_no, self.branch)


s1 = Student("Alxea", 101, "CSE")
s2 = Student("Priya", 102, "ECE")
s3 = Student("Sai", 103, "AI&DS")

s1.display()
s2.display()
s3.display()