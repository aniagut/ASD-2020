def pktyart(G):
    def DFSvisit(v,czas,pkty):
        visited[v] = True
        time[v]=czas[0]
        low[v]=czas[0]
        czas[0]+=1
        for i in range(n):
            if G[v][i] == 1:
                if visited[i] == False:
                    parents[i] = v
                    iledzieci[v]+=1
                    DFSvisit(i,czas,pkty)
                else:
                    if time[i] < low[v]:
                        low[v] = time[i]
        if parents[v] != None and low[parents[v]] > low[v]:
            low[parents[v]] = low[v]

    n=len(G)
    czas=[1]
    visited=[False]*n
    parents=[None]*n
    time=[None]*n
    low=[None]*n
    iledzieci=[0]*n
    czykorzen=[False]*n
    pkty=[]
    for i in range (n):
        if visited[i]==False:
            czykorzen[i]=True
            DFSvisit(i,czas,pkty)
            if iledzieci[i]>=2:
                pkty.append(i)
    for i in range (n):
        if parents[i]!=None and low[i]>=time[parents[i]] and czykorzen[parents[i]]==False:
            pkty.append(parents[i])
    print(parents)
    print(time)
    print(low)
    print(pkty)
G=[[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,1,0],[0,0,1,0,1,1,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1],[0,0,0,0,0,0,1,0]]
pktyart(G)