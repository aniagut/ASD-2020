def lcs_length(X,Y):
    m=len(X)
    n=len(Y)
    M=[[[]for i in range (n+1)] for i in range (m+1)]
    for i in range(0,m+1):
        M[i][0]=0
    for i in range(0,n+1):
        M[0][i]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                M[i][j]=M[i-1][j-1]+1
            elif M[i][j-1]>M[i-1][j]:
                M[i][j]=M[i][j-1]
            else:
                M[i][j]=M[i-1][j]
    return M[m][n]
X="ABCBDAB"
Y="BDCABA"
print(lcs_length(X,Y))
