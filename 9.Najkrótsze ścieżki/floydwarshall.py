#najkrotsze sciezki miedzy kazda para wierzcholkow
#dla grafow gestych
#na macierzy sasiedztwa
def floydwarshall(G):
    n=len(G)
    D=[[float('inf') for j in range (n)] for i in range (n)]
    for i in range (n):
        for j in range (n):
            if i==j:
                D[i][j]=0
            if G[i][j]!=0:
                D[i][j]=G[i][j]
    for t in range (n):
        for i in range (n):
            for j in range (n):
                D[i][j]=min(D[i][j],D[i][t]+D[t][j])
    return D
G=[[0,2,7,1,0,0,0],[0,0,0,4,0,0,3],[0,0,0,0,2,0,0],[0,0,3,0,1,3,5],[0,0,0,0,0,4,0],[0,0,0,0,0,0,0],[0,0,0,0,0,3,0]]
print(floydwarshall(G))