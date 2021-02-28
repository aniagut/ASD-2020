#najkrotsze ścieżki z s do innych wierzchołków w grafie nieważonym
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

def BFS(G,s):
    n=len(G)
    q=Queue()
    visited=[False]*n
    odleglosci=[0]*n
    parents=[None]*n
    visited[s]=True
    q.enqueue(s)
    while not q.is_empty():
        v=q.dequeue()
        for i in range(len(G[v])):
            if G[v][i]==1:
                if visited[i]==False:
                    visited[i]=True
                    odleglosci[i]=odleglosci[v]+1
                    parents[i]=v
                    q.enqueue(i)

