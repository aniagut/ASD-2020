class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Queue:
    def __init__(self):
        self.size=0
        self.head=Node(None)
        self.tail=Node(None)
    def enqueue(self,x):
        new=Node(x)
        if self.size==0:
            self.head=new
            self.tail=new
            self.size+=1
        else:
            tmp=Node(None)
            tmp.next=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=new
            self.tail=new
            self.size+=1
    def pop(self):
        res=self.head.val
        self.head=self.head.next
        self.size-=1
        return res
    def is_empty(self):
        return self.size==0

def BFS(G,s,t,parents):
    visited=[False]*len(G)
    q=Queue()
    q.enqueue(s)
    visited[s]=True
    while not q.is_empty():
        u=q.pop()
        for i in range(len(G[u])):
            if visited[i]==False and G[u][i]>0:
                q.enqueue(i)
                visited[i]=True
                parents[i]=u
    if visited[t]==True:
        return True
    else:
        return False
def fordfulkerson(G,s,t):
    parents=[None]*len(G)
    max_flow=0
    while BFS(G,s,t,parents):
        curr_flow=(float('inf'))
        fin=t
        while fin!=s:
            curr_flow=min(curr_flow,G[parents[fin]][fin])
            fin=parents[fin]
        max_flow+=curr_flow
        fin=t
        while fin!=s:
            u=parents[fin]
            G[u][fin]-=curr_flow
            G[fin][u]+=curr_flow
            fin=parents[fin]
    return max_flow
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
print(fordfulkerson(graph,0,5))



