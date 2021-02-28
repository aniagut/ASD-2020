def mosty(G):
    def DFS(G,v,visited,parents,time,low,kolejnosc,n):
        visited[v]=True
        kolejnosc.append(v)
        time[v]=len(kolejnosc)
        low[v]=time[v]
        for i in range (n):
            if G[v][i]==1:
                G[v][i]=0
                G[i][v]=0
                if visited[i]==False:
                    parents[i]=v
                    DFS(G,i,visited,parents,time,low,kolejnosc,n)
                else:
                    if time[i]<low[v]:
                        low[v]=time[i]
        if parents[v]!=None and  low[v]<low[parents[v]]:
            low[parents[v]]=low[v]
    n=len(G)
    visited=[False]*n
    parents=[None]*n
    time=[None]*n
    low=[None]*n
    kolejnosc=[]
    DFS(G,0,visited,parents,time,low,kolejnosc,n)
    for i in range (n):
        if low[i]==time[i]:
            if parents[i]!=None:
                print(parents[i],i)

G=[[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,1,0],[0,0,1,0,1,1,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1],[0,0,0,0,0,0,1,0]]
mosty(G)
