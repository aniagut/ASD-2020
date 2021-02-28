def DFSvisit(G,v,visited,n,przetworz):
    visited[v]=True
    for i in range (n):
        if G[v][i]==1:
            if visited[i]==False:
                DFSvisit(G,i,visited,n,przetworz)
            elif visited[i]==True and przetworz[i]==False:
                return True
    przetworz[v]=True
    return False

def topol_sort(G):
    n=len(G)
    visited=[False]*n
    przetworz=[False]*n
    iscycle=False
    for i in range (n):
        if visited[i]==False:
            iscycle=DFSvisit(G,i,visited,n,przetworz)
        if iscycle==True:
            return True
    return False
G=[[0,1,0,0,0,0,1,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,1,0],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0]]
print(topol_sort(G))