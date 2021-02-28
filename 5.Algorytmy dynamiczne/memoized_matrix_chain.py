def memoized_matrix_chain(P):
    n=len(P)
    M=[[float('inf') for i in range (n+1)] for j in range(n+1)]
    return lookup_chain(P,M,1,n)
def lookup_chain(P,M,i,j):
    if M[i][j]<float('inf'):
        return M[i][j]
    if i==j:
        M[i][j]=0
    else:
        for k in range (i,j,1):
            q=lookup_chain(P,M,i,k)+lookup_chain(P,M,k+1,j)+P[i-1][0]*P[k-1][1]*P[j-1][1]
            if q<M[i][j]:
                M[i][j]=q
    return M[i][j]
P=[(30,35),(35,15),(15,5),(5,10),(10,20),(20,25)]
print(memoized_matrix_chain(P))