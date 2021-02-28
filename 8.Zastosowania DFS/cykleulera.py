def eulercycle(G):
    def DFSvisit(G,v,list):
        for i in range (n):
            if G[v][i]==1:
                G[v][i]=0
                G[i][v]=0
                DFSvisit(G,i,list)
        list.append(v)
    n=len(G)
    for i in range (n):
        ile=0
        for j in range (n):
            if G[i][j]==1:
                ile+=1
        if ile%2!=0:
            return False
    list=[]
    DFSvisit(G,0,list)
    return list

G=[[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
print(eulercycle(G))
