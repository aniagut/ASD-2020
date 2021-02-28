def mothervertice(G):
    def DFSvisit(G,v,visited,n):
        visited[v]=True
        for i in range (n):
            if G[v][i]==1 and visited[i]==False:
                DFSvisit(G,i,visited,n)
    n=len(G)
    visited=[False]*n
    v=0
    for i in range (n):
        if visited[i]==False:
            DFSvisit(G,i,visited,n)
            v=i
    for i in range (n):
        visited[i]=False
    DFSvisit(G,v,visited,n)
    for i in range (n):
        if visited[i]==False:
            return False
    print(v)
    return True
G=[[0,0,0,0,0,0],[1,0,0,0,0,0],[0,1,0,1,0,0],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,0]]
print(mothervertice(G))
