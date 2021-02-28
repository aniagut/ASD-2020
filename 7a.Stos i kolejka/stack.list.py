#STOS LISTOWO

class Node:
    def __init__(self):
        self.next=None
        self.val=None
class Stack:
    def __init__(self):
        self.top=Node() #wartownik
    def push(self,x):
        N=Node()
        N.val=x
        N.next=self.top.next
        self.top.next=N
    def pop(self):
        N=self.top.next
        self.top.next=N.next
        return N.val
    def is_empty(self):
        return self.top.next==None

A=Stack()
A.push(4)
A.push(7)
A.push(8)
print(A.top.next)
print(A.pop())
print(A.top.next)
print(A.pop())
print(A.top.next)
print(A.is_empty())
print(A.pop())
print(A.top.next)
print(A.is_empty())