class Queue:
    def __init__(self):
        self.size=0
        self.head=0
        self.tail=-1
        self.q=[]
    def enqueue(self,x):
        self.tail+=1
        self.size==0
        if self.tail==len(self.q):
            self.q.append(x)
        else:
            self.q[self.tail]=x
    def dequeue(self):
        res=self.q[self.head]
        self.head+=1
        self.size-=1
        return res
    def is_empty(self):
        return self.size==0

def przesun(tab,k):
    n=len(tab)
    idx=n-k
    q=Queue()
    for i in range(n):
        q.enqueue(tab[idx%n])
        idx+=1
    for i in range (n):
        tab[i]=q.dequeue()

tab=[1,2,3,4,5,6]
przesun(tab,3)
print(tab)
