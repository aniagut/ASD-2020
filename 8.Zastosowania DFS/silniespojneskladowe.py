def silniespojne(G):
    def DFSvisit(G,v,visited,przetw):
        visited[v]=True
        for i in range (n):
            if visited[i]==False and G[v][i]==1:
                DFSvisit(G,i,visited,przetw)
        przetw.append(v)
    def DFSvisit_(G,v,visited,spojne,idx):
        visited[v]=True
        for i in range (n):
            if visited[i]==False and G[i][v]==1:
                DFSvisit_(G,i,visited,spojne,idx)
        spojne[idx].append(v)
    n=len(G)
    przetw=[]
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            DFSvisit(G,i,visited,przetw)
    spojne=[]
    visited=[False]*n
    idx=0
    for i in range (n-1,-1,-1):
        if visited[przetw[i]]==False:
            spojne.append([])
            DFSvisit_(G,przetw[i],visited,spojne,idx)
            idx+=1
    return spojne
G=[[0,0,1,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,1,0,0]]
print(silniespojne(G))