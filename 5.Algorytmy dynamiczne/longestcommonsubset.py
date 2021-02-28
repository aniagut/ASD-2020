def longest(A,B,n):
    M=[[0 for i in range (n+1)] for i in range (n+1)]
    for i in range (1,n):
        for j in range (1,n+1):
            if A[i-1]==B[j-1]:
                M[i][j]=M[i-1][j-1]+1
            else:
                M[i][j]=max(M[i][j-1],M[i-1][j])
    print(M)
    return M[n-1][n-1]

A=["x","y","a","o","m","l","i","e"]
B=["y","c","a","e","o","n","l","a"]
print(longest(A,B,len(A)))
