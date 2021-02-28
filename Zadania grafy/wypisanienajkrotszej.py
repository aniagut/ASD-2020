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
def print_(v,parents):
    if parents[v]!=None:
        print_(parents[v],parents)
    print(v)
def dij(G,s,t):
    n=len(G)
    dist=[float('inf')]*n
    dist[s]=0
    parents=[None]*n
    q=priorityqueue()
    q.put(s)
    while not q.is_empty():
        u=q.get()
        for i in range (n):
            if G[u][i]!=0:
                if dist[i]>dist[u]+G[u][i]:
                    dist[i]=dist[u]+G[u][i]
                    parents[i]=u
                    q.put(i)
    print_(t,parents)
G=[[0,5,7,0,0],[0,0,1,0,0],[0,0,0,4,2],[0,0,0,0,8],[0,0,0,0,0]]
dij(G,0,4)