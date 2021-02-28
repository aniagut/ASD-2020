def szachwonica(K):
    n=len(K)
    M=[[[] for i in range(n+1)] for i in range (n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            M[i][j]=K[i-1][j-1]
    for i in range (2,n+1):
        M[1][i]+=M[1][i-1]
        M[i][1]+=M[i-1][1]
    for i in range(2,n+1):
        for j in range(2,n+1):
            M[i][j]+=min(M[i-1][j],M[i][j-1])
    return M[n][n]
K=[[1,2,3,2,1],[1,1,2,4,5],[7,3,1,1,1],[2,1,5,3,1],[3,4,2,2,1]]
print(szachwonica(K))