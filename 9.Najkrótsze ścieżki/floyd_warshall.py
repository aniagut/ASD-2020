def floyd_warshall(G):
    macierz=[[float('inf')for i in range (len(G)) ] for i in range (len(G))]
    for i in range (len(G)):
        macierz[i][i]=0
    for i in range(len(G)):
        for j  in range(len(G)):
            if G[i][j]!=0:
                macierz[i][j]=G[i][j]
    for t in range(0,len(G)):
        for i in range(0,len(G)):
            for j in range(0,len(G)):
                macierz[i][j]=min(macierz[i][j],macierz[i][t]+macierz[t][j])
    print(macierz)
G=[[0,5,7,2,0],[0,0,0,0,4],[0,0,0,1,5],[0,0,0,0,0],[0,0,0,2,0]]
floyd_warshall(G)