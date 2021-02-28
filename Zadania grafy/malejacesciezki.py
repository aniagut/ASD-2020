def czyistnieje(G,x,y):
    def DFSvisit(G,v,visited,dl):
        visited[v]=True
        for i in range(n):
            if G[v][i]<dl and G[v][i]!=0  and visited[i]==False:
                DFSvisit(G,i,visited,G[v][i])
    n=len(G)
    visited=[False]*n
    DFSvisit(G,x,visited,float('inf'))
    if visited[y]==True:
        return True
    return False
G=[[0,4,0,1,3],[4,0,5,0,0],[0,5,0,0,2],[1,0,0,0,0],[3,0,2,0,0]]
print(czyistnieje(G,0,2))