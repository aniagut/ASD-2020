#kolorujemy bfsem-jesli ktorys juz pokolorowany na inny niz powinien byc, to graf nie jest dwudzielny

class Queue:
    def __init__(self):
        self.head=0
        self.tail=-1
        self.size=0
        self.q=[]
    def enqueue(self,v):
        self.q.append(v)
        self.tail+=1
        self.size+=1
    def dequeue(self):
        result=self.q[self.head]
        self.head+=1
        self.size-=1
        return result
    def is_empty(self):
        return self.size==0

def BFScol(G):
    n=len(G)
    colour=[0]*n
    colour[0]=1
    q=Queue()
    q.enqueue(0)
    while not q.is_empty():
        v=q.dequeue()
        for i in range(n):
            if G[v][i]==1:
                if colour[i]==0:
                    if colour[v]==1:
                        colour[i]=2
                    else:
                        colour[i]=1
                    q.enqueue(i)
                else:
                    if colour[i]==colour[v]:
                        return False
    return True

G=[[0,1,0,1,1,1],[1,0,1,1,0,0],[0,1,0,0,1,1],[1,1,0,0,1,1],[1,0,1,1,0,0],[1,0,1,1,0,0]]
print(BFScol(G))


