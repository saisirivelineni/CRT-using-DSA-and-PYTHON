'''def square(x): 
      return x * x 
print(square(square(2)))'''


'''#stack 
stack=[]
stack.append(5)
stack.append(6)
print(stack) #[5,6]
stack.append(7)
stack.append(4)
print('stack',stack)#[5,7,4]
print(stack[-1])#4
print(len(stack)==0)'''

'''stack = [5,7,6,4,3]
T = 7

if T in stack:
    print("Found")'''

'''stack = [5,7,6,4,3]
T = 7

while stack:
    if stack.pop() == T:
        print("Found")
        break'''

'''stack=[5,3,8,2,9]
l=len(stack)
t=8
for i in range(l):
    if stack.pop() == t:
        print("Found")
        break'''

'''class Student:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch

    def display(self):
        print(self.name, self.rollno, self.branch)


S1 = Student("sai", 101, "ECE")
S2 = Student("kavya", 102, "EEE")
S3 = Student("ramya", 103, "CSE")

S1.display()
S2.display()
S3.display()'''

'''class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"


d1 = Dog("Rex")
d2 = Dog("Tommy")

print(d1.speak())
print(d2.speak())'''

'''#min stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())  # -3

obj.pop()

print(obj.top())     # 0
print(obj.getMin())  # -2 '''

'''#max stack
class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_max = max(val, self.stack[-1][1])
            self.stack.append((val, current_max))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMax(self) -> int:
        return self.stack[-1][1]


obj = MaxStack()

obj.push(2)
obj.push(5)
obj.push(3)

print(obj.getMax())  # 5

obj.pop()

print(obj.top())     # 5
print(obj.getMax())  # 5'''

'''#queue
from collections import deque

q=deque()
q.append(10)#enqueu
q.append(20)
q.append(30)
print(q.popleft())#dequeu
print(q[0])#peek'''
