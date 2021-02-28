def DFSvisit(G,v,visited,lista,n):
    visited[v]=True
    for i in range (n):
        if G[v][i]==1:
            if visited[i]==False:
                DFSvisit(G,i,visited,lista,n)
    lista.append(v)


def topol_sort(G):
    n=len(G)
    visited=[False]*n
    lista=[]
    for i in range (n):
        if visited[i]==False:
            DFSvisit(G,i,visited,lista,n)
    return lista
G=[[0,0,1,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,1,0,0]]
print(topol_sort(G))