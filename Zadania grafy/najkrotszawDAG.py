#sortowanie topologiczne od s i potem sprawdzanie po kolei
def topological(G,v,stack,visited,n):
    visited[v]=True
    for i in range (n):
        if G[v][i]!=0 and visited[i]==False:
            topological(G,i,stack,visited,n)
    stack.append(v)
def najkrotsze(G,s):
    n=len(G)
    visited=[False]*n
    stack=[]
    topological(G,s,stack,visited,n)
    dist=[float('inf')]*n
    dist[s]=0
    print(stack)
    idx=len(stack)-1
    while idx>=0:
        u=stack[idx]
        idx-=1
        for i in range(n):
            if G[u][i]!=0:
                if dist[i]>dist[u]+G[u][i]:
                    dist[i]=dist[u]+G[u][i]
    print (dist)

G=[[0,2,0,3,0],[0,0,1,0,0],[0,0,0,1,3],[0,0,0,0,4],[0,0,0,0,0]]
najkrotsze(G,0)


