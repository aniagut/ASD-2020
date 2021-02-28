#graf skierowany,zrodlo i ujscie,jesli jest u-v to nie ma v-u
#mamy dane maksymalne pojemnosci
#metoda forda fulkersona
class Queue:
    def __init__(self,n):
        self.q=[None]*n
        self.head=0
        self.tail=-1
        self.elements=0
    def enqueue(self,x):
        self.tail+=1
        self.q[self.tail]=x
        self.elements+=1
    def dequeue(self):
        res=self.q[self.head]
        self.head+=1
        self.elements-=1
        return res
    def is_empty(self):
        return self.elements==0
def BFS(G,n,s,t,parents):
    visited=[False]*n
    visited[s]=True
    q=Queue(n)
    q.enqueue(s)
    while not q.is_empty():
        v=q.dequeue()
        for i in range (n):
            if G[v][i]>0:
                if visited[i]==False:
                    visited[i]=True
                    parents[i]=v
                    if i == t:
                        return True
                    q.enqueue(i)

    return False
def fordfulkerson(G,s,t):
    n=len(G)
    flow=0
    parents=[None]*n
    while BFS(G,n,s,t,parents):
        curr_flow=float('inf')
        v=t
        while v!=s:
            curr_flow=min(curr_flow,G[parents[v]][v])
            v=parents[v]
        flow+=curr_flow
        v=t
        while v!=s:
            G[parents[v]][v]-=curr_flow
            G[v][parents[v]]+=curr_flow
            v=parents[v]
    return flow
G=[[0,4,0,5,0,0],[0,0,1,2,0,0],[0,0,0,0,4,0],[0,0,0,0,2,3],[0,0,0,0,0,3],[0,0,0,0,0,0]]
print(fordfulkerson(G,0,5))
