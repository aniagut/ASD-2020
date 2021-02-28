def najkrotszeprzerwy(Jobs,k):
    n=len(Jobs)
    Jobs.sort(key=lambda x:x[1])
    DP=[[float('inf') for i in range (k+1)] for j in range (n)]
    for i in range (n):
        DP[i][0],DP[i][1]=0,0
    for i in range (1,n):
        mini=min(i+2,k+1)
        for t in range(2,mini):
            j=i-1
            while j>=0:
                if Jobs[j][1]<=Jobs[i][0] and (DP[j][t-1]+(Jobs[i][0]-Jobs[j][1]))<DP[i][t]:
                    DP[i][t]=(DP[j][t-1]+(Jobs[i][0]-Jobs[j][1]))
                j-=1
    minimum=float('inf')
    for i in range (n-1,-1,-1):
        if DP[i][k]<minimum:
            minimum=DP[i][k]
    if minimum<float('inf'):
        return minimum
    else:
        return -1
J=[(4,6),(2,7),(3,10),(1,5),(2,6),(8,10)]
print(najkrotszeprzerwy(J,3))

