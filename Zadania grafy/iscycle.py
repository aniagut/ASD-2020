#graf nieskierowany-postac macierzowa
#usuwamy na chwilke dana krawedz zeby nie wylkrylo cyklu o jednej krawedzi

def iscycle(G):
   n=len(G)
   for i in range (n):
       col=[0]*n
       if DFSvisit(G,i,col,n)==True:
           return True
   return False
def DFSvisit(G,v,col,n):
    col[v]=1
    iscycle=False
    for i in range (n):
        if G[v][i]==1:
            if col[i]==0:
                G[i][v]=0
                iscycle=DFSvisit(G,i,col,n)
                G[i][v]=1
            else:
                iscycle=True
    return iscycle

G=[[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,0,1],[0,0,1,0,1,0],[1,1,0,1,0,0],[1,0,1,0,0,0]]
print(iscycle(G))