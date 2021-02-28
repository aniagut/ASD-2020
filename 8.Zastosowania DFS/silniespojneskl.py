#u,v naleza jezeli z u istn sciezka skier do v i z v do u
#graf silnie spojnych skladowych jest DAGIem
def DFSvisit(G,v,visited,n,czasy):
    visited[v]=True
    for i in range(n):
        if G[v][i]==1:
            if visited[i]==False:
                DFSvisit(G,i,visited,n,czasy)
    czasy.append(v)
def DFSback(G,v,visited,n,lista):
    visited[v]=True
    for i in range(n):
        if G[i][v]==1:
            if visited[i]==False:
                DFSback(G,i,visited,n,lista)
    lista.append(v)

def silniesp(G):
    n=len(G)
    visited=[False]*n
    czasy=[]
    for i in range(n):
        if visited[i]==False:
            DFSvisit(G,i,visited,n,czasy)
    for i in range (n):
        visited[i]=False
    for i in range (n-1,-1,-1):
        lista=[]
        if visited[czasy[i]]==False:
            DFSback(G,czasy[i],visited,n,lista)
        if len(lista)>0: print(lista)

G=[[0,0,1,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,1,0,0]]
silniesp(G)