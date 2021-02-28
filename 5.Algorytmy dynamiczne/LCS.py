#LCS
def LCS(A,B):
    n=len(A)
    m=len(B)
    F=[[0 for i in range (n+1)] for i in range (m+1)]
    for i in range (m+1):
        F[i][0]=0
    for i in range (n+1):
        F[0][i]=0
    for i in range (1,m+1):
        for j in range (1,n+1):
            if A[j-1]==B[i-1]:
                F[i][j]=F[i-1][j-1]+1
            elif F[i-1][j]>F[i][j-1]:
                F[i][j]=F[i-1][j]
            else:
                F[i][j]=F[i][j-1]
    return F[m][n]
sl1="ania"
sl2="tatnia"
print(LCS(sl1,sl2))