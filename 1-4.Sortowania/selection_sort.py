def selection_sort(A):
    n=len(A)
    for j in range(n-1):
        min=A[j]
        idx=j
        for i in range(j+1,n):
            if A[i]<min:
                min=A[i]
                idx=i
        if idx!=j:
            A[idx],A[j]=A[j],A[idx]
tab=[3,18,0,2,6,17,4,7,1,12]
print(tab)
selection_sort(tab)
print(tab)