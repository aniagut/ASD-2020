class Stack:
    def __init__(self,n):
        self.s=[None]*n
        self.elements=0
        self.top=-1
    def push(self,x):
        self.top+=1
        self.s[self.top]=x
        self.elements+=1
    def pop(self):
        res=self.s[self.top]
        self.top-=1
        self.elements-=1
        return res
    def is_empty(self):
        return self.elements==0


def uniwersalneujscie(G):
    n=len(G)
    s=Stack(n)
    for i in range (n):
        s.push(i)
    while s.elements>=2:
        u=s.pop()
        v=s.pop()
        if G[u][v]==1:
            s.push(v)
        else:
            s.push(u)
    pp=s.pop()
    for i in range (n):
        if G[pp][i]!=0:
            return None
        if i!=pp and G[i][pp]!=1:
            return None
    return pp

G=[[0,1,1,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,1,0,0,0],[1,1,0,1,0]]
print(uniwersalneujscie(G))
