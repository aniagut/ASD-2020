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

#kolorowanie BFS-em
def isbipartite(G):
    n=len(G)
    color=[-1]*n
    q=Queue()
    color[0]=1
    q.enqueue(0)
    while not q.is_empty():
        u=q.dequeue()
        for i in range(u+1,n):
            if G[u][i]==1:
                if color[i]==-1:
                    color[i]=1-color[u]
                    q.enqueue(i)
                elif color[i]==color[u]:
                    return False
    return True

graph=[[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,1],[0,0,1,0,1],[0,1,0,1,0]]
print(isbipartite(graph))
