def bellman_ford(G,s):
    n=len(G)
    dist=[float('inf')]*n
    dist[s]=0
    for i in range (n-1):
        for i in range (n):
            for j in range (n):
                if G[i][j]!=0:
                    if dist[j]>dist[i]+G[i][j]:
                        dist[j]=dist[i]+G[i][j]
    for i in range (n):
        for j in range (n):
            if G[i][j]!=0:
                if dist[j]>dist[i]+G[i][j]:
                    return False
    return dist
G=[[0,-1,4,0,0],[0,0,3,2,2],[0,0,0,0,0],[0,1,5,0,0],[0,0,0,-3,0]]
print(bellman_ford(G,0))