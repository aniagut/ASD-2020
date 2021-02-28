def isCyclic(G,v,visited,parent,n):
    visited[v]=True
    for i in range (n):
        if G[v][i]==1:
            if visited[i]==False:
                if isCyclic(G,i,visited,v,n)==True:
                    return True
            elif parent!=i:
                return True
    return False

def isCycle(G):
    n=len(G)
    visited=[False]*n
    for i in range (n):
        if visited[i]==False:
            if isCyclic(G,i,visited,-1,n)==True:
                return True
    return False

G=[[0,1,0,1,0],[1,0,1,0,0],[0,1,0,0,1],[1,0,0,0,1],[0,0,1,1,0]]
print(isCycle(G))