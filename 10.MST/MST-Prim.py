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

def Prim(G):
    n=len(G)
    wagi=[float("inf")]*n
    q=PriorityQueue(10)
    wagi[0]=0
    q.put(0,wagi)
    parents=[None]*n
    while not q.is_empty():
        v=q.get()
        for i in range (n):
            if G[v][i]!=0 and i!=parents[v]:
                if wagi[i]>G[v][i]:
                    wagi[i]=G[v][i]
                    parents[i]=v
                    q.put(i,wagi)
    return parents
G=[[0,2,1,0,0,0,6],[2,0,0,3,0,0,0],[1,0,0,2,0,5,0],[0,3,2,0,1,0,0],[0,0,0,1,0,7,0],[0,0,5,0,7,0,8],[6,0,0,0,0,8,0]]
print(Prim(G))