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
        while i>self.head and distances[x]<distances[self.q[i-1]]:
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

def dijkstra(G,s):
    n=len(G)
    distances=[float("inf")]*n
    distances[s]=0
    parents=[None]*n
    q=PriorityQueue(100)
    q.put(s,distances)
    while not q.is_empty():
        v=q.get()
        for i in range (n):
            if G[v][i]>0:
                if distances[i]>distances[v]+G[v][i]:
                    distances[i]=distances[v]+G[v][i]
                    parents[i]=v
                    q.put(i,distances)
    print(distances)
G=[[0,3,0,0,0,0,0,0,2],[3,0,2,1,0,0,0,0,0],[0,2,0,0,5,0,0,0,0],[0,1,0,0,1,7,0,0,0],[0,0,5,1,0,0,20,0,0],[0,0,0,7,0,0,2,1,1],[0,0,0,0,20,2,0,8,0],[0,0,0,0,0,1,8,0,3],[2,0,0,0,0,1,0,3,0]]
dijkstra(G,0)