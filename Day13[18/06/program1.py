'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insertAtstart(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=self.tail=newNode;self.size+=1;
            return
        newNode.next= self.head
        self.head= newNode
        self.size+=1
        return head

    def insertAtEnd(self, value):#with tail
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
            return

        self.tail.next = newNode
        self.tail = newNode
        return self.head
        
    def insertAtEnd(self, value):#with out tail
         newNode = Node(value)

    if self.head is None:
            self.head = newNode
            self.size += 1
            return
    curr= self.head
    while curr.next:
        curr=curr.next
    curr.next=newNode
    return head'''


'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtStart(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def insertAtEnd(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def insertAtEndWithoutTail(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = newNode
        self.tail = newNode
        self.size += 1

    def deleteAtstart(self):
        if self.head is None:
            return -1

        if self.head.next is None:
            self.head = self.tail = None
            self.size -= 1
            return

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return self.head

    def deleteFromEnd(self):
        if self.head is None:
            return -1

        if self.head.next is None:
            self.head = self.tail = None
            self.size -= 1
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next

        d = curr.next
        curr.next = None
        self.tail = curr
        self.size -= 1
        return d

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def deleteAtIndex(self,Index):
        if self.head is None:
            return -1
        if index==0:
            deleteAtstart()
            return
        if index==self.size-1:
            deleteFromEnd()
            return
        curr=curr.next
        for i in range(index-1):
            curr=curr.next
        temp=curr.next
        curr.next=temp.next
        temp.next=None
        return temp'''



'''class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# create list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original:")
printList(head)

sol = Solution()
new_head = sol.reverseList(head)

print("Reversed:")
printList(new_head)'''


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
