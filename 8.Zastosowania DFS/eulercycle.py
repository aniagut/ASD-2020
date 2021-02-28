#euler-przebiega przez wszystkie krawedzie grafu
#deg(v) parzysty-WW
def DFSeuler(G,v,n,lista):
    for i in range (n):
        if G[v][i]==1:
            G[v][i]=0
            G[i][v]=0
            DFSeuler(G,i,n,lista)
    lista.append(v)

def find_euler(G):
    n=len(G)
    lista=[]
    DFSeuler(G,4,n,lista)
    return lista

G=[[0,1,0,0,1,0,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,1],[0,0,1,0,0,1,0],[1,1,0,0,0,1,1],[0,0,1,1,1,0,1],[0,1,1,0,1,1,0]]
print(find_euler(G))
