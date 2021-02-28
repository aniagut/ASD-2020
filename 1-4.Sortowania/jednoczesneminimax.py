def getminandmax(A):
    n=len(A)
    if n==0:
        return None
    if n==1:
        return A[0],A[0]
    if A[0]>A[1]:
        min=A[1]
        max=A[0]
    else:
        min=A[0]
        max=A[1]
    for i in range(2,n-1,2):
        if A[i]>A[i+1]:
            if A[i]>max:
                max=A[i]
            if A[i+1]<min:
                min=A[i+1]
        else:
            if A[i+1]>max:
                max=A[i+1]
            if A[i]<min:
                min=A[i]
    if len(A)%2==1:
        if A[n-1]>max:
            max=A[n-1]
        if A[n-1]<min:
            min=A[n-1]
    return min,max
tab=[3,14,0,9,18,7,6,23,4,10,5,16,3,19,7]
print(getminandmax(tab))
