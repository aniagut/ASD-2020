class PriorityQueue:
    def __init__(self,n):
        self.q=[None]*n
        self.head=0
        self.tail=-1
        self.elements=0
    def put(self,x,distances):
        self.tail+=1
        self.elements+=1
        self.q[self.tail]=x
        i=self.tail
        while i>self.head and distances[x[0]]<distances[self.q[i-1][0]]:
            self.q[i]=self.q[i-1]
            i-=1
        self.q[i]=x
    def get(self):
        res=self.q[self.head]
        self.head+=1
        self.elements-=1
        return res
    def is_empty(self):
        return self.elements==0

def dijkstra(G,s,t):
    n=len(G)
    distances=[float("inf")]*n
    distances[s]=0
    q=PriorityQueue(100)
    q.put((s,0),distances)
    while not q.is_empty():
        v=q.get()
        for i in range (n):
            if G[v[0]][i]>0 and G[v[0]][i]!=v[1]:
                if distances[i]>distances[v[0]]+G[v[0]][i]:
                    distances[i]=distances[v[0]]+G[v[0]][i]
                    q.put((i,G[v[0]][i]),distances)
    return distances[t]
def islands(G, A, B):
    x=dijkstra(G,A,B)
    if x<float('inf'):
        return x
    else:
        return None
G=[[0,1,0,0,0],[1,0,5,0,0],[0,5,0,8,0],[0,0,8,0,8],[0,0,0,8,0]]
print(islands(G,0,4))