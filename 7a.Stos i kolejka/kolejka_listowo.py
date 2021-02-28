class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
class Queue:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
    def enqueue(self,x):
        n=Node(x)
        if self.head.next==None:
            self.head.next=n
            self.tail.next=n
        else:
            self.tail.next.next=n
            self.tail.next=n
    def dequeue(self):
        res=self.head.next
        self.head.next=res.next
        return res.val
    def is_empty(self):
        return self.head.next==None
