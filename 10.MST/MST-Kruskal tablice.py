def find_set(u,parents):
    if u!=parents[u]:
        parents[u]=find_set(parents[u],parents )
    return parents[u]
def union(x,y,parents,rank):
    x=find_set(x,parents)
    y=find_set(y,parents)
    if rank[x]>rank[y]:
        parents[y]=x
    else:
        parents[x]=y
        if rank[x]==rank[y]:
            rank[y]+=1
def Kruskalalg(edges,n):
    edges.sort(key=lambda x:x[2])
    edg=len(edges)
    MST=[]
    parents=[]
    for i in range (n):
        parents.append(i)
    rank=[0]*n
    for i in range(edg):
        u=edges[i][0]
        v=edges[i][1]
        if find_set(u,parents)!=find_set(v,parents):
            MST.append((u,v))
            union(u,v,parents,rank)
    return MST
krawedzie=[(0,1,1),(0,2,1),(0,6,6),(1,3,3),(2,3,2),(2,5,5),(3,4,1),(4,5,7),(5,6,8)]
print(Kruskalalg(krawedzie,7))