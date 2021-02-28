def sieci(G):
    def DFSvisit(G,n,v,visited):
        visited[v]=1
        for i in range(n):
            if G[v][i]==1:
                if visited[i]==False:
                    DFSvisit(G,n,i,visited)
        for i in range (n):
            G[v][i]=0
            G[i][v]=0
        print(v)

    n=len(G)
    visited=[False]*n
    for i in range (n):
        if visited[i]==False:
            DFSvisit(G,n,i,visited)
G=[[0,1,0],[1,0,1],[1,0,0]]
sieci(G)
