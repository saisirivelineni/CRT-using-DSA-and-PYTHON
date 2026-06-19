'''#queue implementation using list
def Enqueue(value):
    if size == len(queue): return False
    rear +=1
    size +=1
    queue[rear]=value
    return True
def dequeue():
    if size == 0: return False
    front +=1
    return True
def peek():
    return queue[Front]
def isFull():
    return size==len(queue)
def isEmpty():
    return size==0'''


'''#circular queue
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.front = -1
        self.rear = -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k

        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.k

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
obj = MyCircularQueue(3)

print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))

print(obj.Rear())
print(obj.isFull())

print(obj.deQueue())
print(obj.enQueue(4))

print(obj.Rear())'''

'''class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
Node1 = Node(10)
Node2 = Node(20)
Node1.data=30
Node1.next=Node2
Node1.next=None
print(Node1.data)'''


'''class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node1.next=Node2
Node2.next=Node3

print(Node1.data)
print(Node2.data)
print(Node3.data)'''


'''l1 = [4, 5, 3, 7, 6]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(l1[0])
current = head

for i in range(1, len(l1)):
    current.next = Node(l1[i])
    current = current.next

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")'''


l1 = [4, 5, 3, 7, 6]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createList(l1):
    head = None
    temp = None

    for i in l1:
        newNode = Node(i)

        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            temp = newNode

    return head


def display(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


head = createList(l1)
display(head)