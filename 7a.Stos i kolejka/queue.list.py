class Node:
    def __init__(self):
        self.next=None
        self.val=None

class Queue:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
    def enqueue(self,x):
        a=Node()
        a.val=x
        if self.head.next==None:
            self.head.next=a
            self.tail.next=a
        else:
            self.tail.next.next=a
            self.tail.next=a
    def dequeue(self):
        if self.head.next!=None:
            b=self.head.next
            self.head.next=b.next
            return b.val
    def is_empty(self):
        return self.head.next==None

A=Queue()
A.enqueue(4)
A.enqueue(8)
A.enqueue(5)
print(A.is_empty())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.is_empty())




