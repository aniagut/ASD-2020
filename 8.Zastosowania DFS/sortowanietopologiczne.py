def sortowanietop(G):
    def DFSvisit(G,v,visited,lista):
        visited[v]=True
        for i in range (n):
            if G[v][i]==1:
                if visited[i]==False:
                    DFSvisit(G,i,visited,lista)
        lista.append(v)

    n=len(G)
    visited=[False]*n
    lista=[]
    for i in range (n):
        if visited[i]==False:
            DFSvisit(G,i,visited,lista)
    for i in range (n-1,-1,-1):
        print(lista[i])

G=[[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[1,0,1,0,0],[0,0,0,1,0]]
sortowanietop(G)
