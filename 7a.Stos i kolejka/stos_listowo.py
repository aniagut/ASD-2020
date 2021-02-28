class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
class Stack:
    def __init__(self):
        self.top=Node(None)
    def push(self,x):
        new=Node(x)
        new.next=self.top.next
        self.top.next=new
    def pop(self):
        res=self.top.next
        self.top.next=res.next
        return res.val
    def is_empty(self):
        return self.top.next==None
