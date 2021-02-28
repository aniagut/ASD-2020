#hamiltonian path in DAG-directed acyclic graph
def ispath(G):
    def DFSvisit(G,v,visited,n,sort):
        visited[v]=True
        for i in range (n):
            if G[v][i]==1 and visited[i]==False:
                DFSvisit(G,i,visited,n,sort)
        sort.append(v)

    n=len(G)
    visited=[False]*n
    sort=[]
    for i in range (n):
        if visited[i]==False:
            DFSvisit(G,i,visited,n,sort)
    for i in range (n-1):
        if G[sort[i+1]][sort[i]]==0:
            return False
    return True
G=[[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]]
print(ispath(G))