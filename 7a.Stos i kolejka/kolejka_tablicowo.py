class Queue:
    def __init__(self,n):
        self.Q=[None]*n
        self.head=0
        self.elements=0
    def enqueue(self,x):
        self.Q[self.head+self.elements]=x
        self.elements+=1
    def dequeue(self):
        res=self.Q[self.head]
        self.head+=1
        self.elements-=1
        return res
    def is_empty(self):
        return self.elements==0

