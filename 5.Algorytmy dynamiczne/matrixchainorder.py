def matrix_chain_order(P):
    n=len(P)
    parents=[None]*n
    nawiasy=[[[] for i in range(n+1)] for i in range(n+1)]
    M=[[[] for i in range(n+1)] for i in range(n+1)]
    for i in range (1,n+1):
        M[i][i]=0
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            M[i][j]=float('inf')
            for k in range(i,j):
                q=M[i][k]+M[k+1][j]+P[i-1][0]*P[k-1][1]*P[j-1][1]
                if q<M[i][j]:
                    M[i][j]=q
                    nawiasy[i][j]=k
    return M[1][6]


P=[(30,35),(35,15),(15,5),(5,10),(10,20),(20,25)]
print(matrix_chain_order(P))
