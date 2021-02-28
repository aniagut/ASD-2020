def bubble_sort(A):
    n=len(A)-1
    sorted=False
    while not sorted:
        sorted=True
        for j in range(0,n):
            if A[j]>A[j+1]:
                A[j+1],A[j]=A[j],A[j+1]
                sorted=False
        n-=1

tab=[4,14,3,10,9,1,8,17,6,12,2,10]
print(tab)
bubble_sort(tab)
print(tab)
