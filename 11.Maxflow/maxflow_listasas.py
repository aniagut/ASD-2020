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
            v=G[u][i][0]
            flow=G[u][i][1]
            if visited[v]==False and flow>0:
                q.enqueue(v)
                visited[v]=True
                parents[v]=u
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
            i=0
            while G[parents[fin]][i][0]!=fin:
                i+=1
            flow=G[parents[fin]][i][1]
            curr_flow=min(curr_flow,flow)
            fin=parents[fin]
        max_flow+=curr_flow
        fin=t
        while fin!=s:
            u=parents[fin]
            i=0
            while G[u][i][0]!=fin:
                i+=1
            G[u][i]=(G[u][i][0],G[u][i][1]-curr_flow)
            i=0
            while i<len(G[fin]) and G[fin][i][0]!=parents[fin]:
                i+=1
            if(i==len(G[fin])):
                G[fin].append((parents[fin],curr_flow))
            else:
                G[fin][i]=(G[fin][i][0],G[fin][i][1]+curr_flow)
            fin=parents[fin]
    return max_flow

graph=[[(1,16),(2,13)],[(2,10),(3,12)],[(1,4),(4,14)],[(5,20)],[(3,7),(5,4)],[]]
print(fordfulkerson(graph,0,5))