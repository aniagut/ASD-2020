class priorityqueue:
    def __init__(self):
        self.queue=[]
        self.size=0
        self.head=0
        self.tail=-1
    def put(self,v):
        self.queue.append(0)
        self.size+=1
        self.tail+=1
        i=self.tail-1
        while i>=self.head and self.queue[i]>v:
            self.queue[i+1]=self.queue[i]
            i-=1
        self.queue[i+1]=v
    def get(self):
        res=self.queue[self.head]
        self.head+=1
        self.size-=1
        return res
    def is_empty(self):
        if self.size==0: return True
        else: return False

def dijkstra(G,s):
    n=len(G)
    distance=[float('inf')]*n
    distance[s]=0
    q=priorityqueue()
    q.put(s)
    while not q.is_empty():
        v=q.get()
        for i in range (n):
            if G[v][i]!=0:
                if distance[i]>distance[v]+G[v][i]:
                    distance[i]=distance[v]+G[v][i]
                    q.put(i)
    return distance
g=[[0,2,10,0,0,0,0],[0,0,0,0,7,0,0],[0,0,0,0,0,0,5],[0,0,0,0,0,0,0],[0,0,0,1,0,4,4],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0]]
print(dijkstra(g,0))