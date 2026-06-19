class Student:
    def __init__(self,name,age,branch):
        self.name= name
        self.age= age
        self.branch= branch
        
    def eat(self):
      print(f'{self.name} is eating')
    def sleep(self):
        print('sleeping')
    def play(self):
        print(f'{self.name} is playing')
    def study(self):
        print('studying')
student1 = Student('sai',20,'ece')
print(student1.name)
print(student1.age)
student1.eat()