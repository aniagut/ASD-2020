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

def kolorowanie(G):
    n=len(G)
    maxdeg=0
    for i in range (n):
        sum=0
        for j in range (n):
            if G[i][j]==1:
                sum+=1
        if sum>maxdeg:
            maxdeg=sum
    maxdeg+=1
    kolory=[[None for i in range (n)] for j in range (n)]
    q=Queue(n*n)
    q.enqueue(0)
    while not q.is_empty():
        v=q.dequeue()
        for i in range (n):
            if G[v][i]==1 and kolory[v][i]==None:
                col = [True] * maxdeg
                for j in range(n):
                    if G[j][v] == 1 and kolory[j][v] != None:
                        col[kolory[j][v]] = False
                for k in range (n):
                    if G[i][k]==1 and kolory[i][k]!=None:
                        col[kolory[i][k]]=False
                idx=0
                while idx<maxdeg-1 and col[idx]==False:
                    idx+=1
                kolory[v][i],kolory[i][v]=idx,idx
                q.enqueue(i)
    return kolory

G=[[0,1,0,0,1,0],[1,0,1,0,0,1],[0,1,0,1,1,1],[0,0,1,0,1,1],[1,0,1,1,0,0],[0,1,1,1,0,0]]
print(kolorowanie(G))



