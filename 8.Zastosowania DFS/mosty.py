def mosty(G):
    def DFSvisit(v,czas):
        visited[v] = True
        time[v]=czas[0]
        low[v]=czas[0]
        czas[0]+=1
        for i in range(n):
            if G[v][i] == 1:
                if visited[i] == False:
                    parents[i] = v
                    DFSvisit(i,czas)
                else:
                    if parents[v] == None or parents[v] != i:
                        if time[i] < low[v]:
                            low[v] = time[i]
        if parents[v] != None and low[parents[v]] > low[v]:
            low[parents[v]] = low[v]
    n=len(G)
    czas=[0]
    visited=[False]*n
    parents=[None]*n
    time=[None]*n
    low=[None]*n
    for i in range (n):
        if visited[i]==False:
            DFSvisit(i,czas)
    for i in range (n):
        if parents[i]!=None and low[i]==time[i]:
            print(parents[i],i)
G=[[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,1,0],[0,0,1,0,1,1,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1],[0,0,0,0,0,0,1,0]]
mosty(G)