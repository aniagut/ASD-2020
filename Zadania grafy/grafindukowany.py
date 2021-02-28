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

def BFS(G,k):
    n=len(G)
    q=Queue()
    visited=[False]*n
    visited[0]=True
    q.enqueue(0)
    while not q.is_empty():
        v=q.dequeue()
        ile=0
        for i in range(n):
            if G[v][i]==1:
                ile+=1

        if ile>=k:
            for i in range (n):
                if G[v][i]==1 and visited[i]==False:
                    visited[i]=True
                    q.enqueue(i)
        else:
            for i in range (n):
                if G[v][i]==1:
                    visited[i]=True
                    G[v][i]=0
                    G[i][v]=0
                    q.enqueue(i)

    return G
G=[[0,1,1,1,1,0],[1,0,1,1,0,0],[1,1,0,1,0,0],[1,1,1,0,1,1],[1,0,0,1,0,1],[0,0,0,1,1,0]]
print(BFS(G,3))