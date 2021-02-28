#przeszukiwanie wgłąb
def DfSvisit(G,v,visited,parents,leng,n):
    visited[v] = True
    for i in range(n):
        if G[v][i] == 1:
            if visited[i] == False:
                parents[i] = v
                leng[i] = leng[v] + 1
                DfSvisit(G,i,visited,parents,leng,n)
def DFS(G):
    n=len(G)
    visited=[False]*n
    parents=[None]*n
    leng=[0]*n
    leng[0]=0
    for i in range (n):
        if visited[i]==False:
            DfSvisit(G,i,visited,parents,leng,n)
    print(parents)
    print(leng)
G=[[0,1,1,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
DFS(G)