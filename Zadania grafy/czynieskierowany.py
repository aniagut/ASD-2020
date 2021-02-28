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

def czynieskierowany(G):
    n=len(G)
    visited=[False]*n
    q=Queue()
    for i in range (n):
        if visited[i]==False:
            q.enqueue(i)
            visited[i]=True
            while not q.is_empty():
                u=q.dequeue()
                for i in range (n):
                    if G[u][i]==1:
                        if G[i][u]!=1: return False
                        if visited[i]==False:
                            visited[i]=True
                            q.enqueue(i)
    return True

G=[[0,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]
print(czynieskierowany(G))