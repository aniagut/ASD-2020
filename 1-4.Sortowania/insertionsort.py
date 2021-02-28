def insertion_sort(A):
    n=len(A)
    for j in range(1,n):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
tab=[3,7,9,1,4,2,10,11,5]
print(tab)
insertion_sort(tab)
print(tab)