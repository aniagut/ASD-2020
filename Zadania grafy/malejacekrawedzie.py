#czy istnieje sciezka z x do y, gdzie przechodzimy przez krawedzie o coraz mniejszych wagach
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
#idziemy bfsem od x jesli krawedz po jakiej weszlismy do danego wierzcholka wieksza niz wychodzaca z niego to dodajemy do kolejki
#jak dojdziemy do y to swieto
def jajo(G,x,y):
    n=len(G)
    q=Queue(n)
    dist=[float('inf')]*n
    q.enqueue(x)
    while not q.is_empty():
        v=q.dequeue()
        for i in range (n):
            if G[v][i]>0:
                if dist[v]>G[v][i]:
                    dist[i]=G[v][i]
                    q.enqueue(i)
    if dist[y]<float('inf'):
        return True
    else:
        return False
G=[[0,7,0,0,2,0,0],[0,0,6,0,0,0,7],[0,0,0,7,0,0,0],[0,0,0,0,0,4,0],[0,0,0,0,0,0,9],[0,0,0,0,0,0,0],[0,0,0,5,0,8,0]]
print(jajo(G,0,5))
