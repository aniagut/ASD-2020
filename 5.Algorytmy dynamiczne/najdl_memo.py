def lcslength(X,Y):
    m=len(X)
    n=len(Y)
    M=[[float('inf') for i in range(n+1)] for j in range (m+1)]
    return memo(X,Y,M,m,n)
def memo(X,Y,M,i,j):
    if M[i][j]<float('inf'):
        return M[i][j]
    elif i==0 or j==0:
        M[i][j]=0
    elif X[i-1]==Y[j-1]:
        M[i][j]=memo(X,Y,M,i-1,j-1)+1
    else:
        M[i][j]=max(memo(X,Y,M,i-1,j),memo(X,Y,M,i,j-1))
    return M[i][j]
X="ABCBDAB"
Y="BDCABA"
print(lcslength(X,Y))

