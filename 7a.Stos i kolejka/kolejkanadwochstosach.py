class Stack:
    def __init__(self):
        self.s=[]
        self.top=-1
        self.size=0
    def push(self,x):
        self.top+=1
        self.size+=1
        if self.top==len(self.s):
            self.s.append(x)
        else:
            self.s[self.top]=x
    def pop(self):
        self.size -= 1
        res=self.s[self.top]
        self.top-=1
        return res
    def is_empty(self):
        return self.size==0

class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enqueue(self,x):
        while not self.s1.is_empty:
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
    def dequeue(self):
        return self.s1.pop()
    def is_empty(self):
        return self.s1.is_empty()

s=Stack()
q=Queue()
print(q.is_empty())
q.enqueue(3)
print(q.is_empty())
q.enqueue(5)
q.enqueue(9)
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())
