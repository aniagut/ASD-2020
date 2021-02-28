def partition(A,p,r):
    piwot=A[p]
    i=p
    j=r
    while i<=j:
        while i<=j and A[i]<=piwot:
            i+=1
        while i<=j and A[j]>piwot:
            j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1
    A[j],A[p]=A[p],A[j]
    return j
def quicksort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p<r-q:
            quicksort(A,p,q-1)
            p=q+1
        else:
            quicksort(A,q+1,r)
            r=q-1

tab=[4,15,10,1,12,6,7,18,4,0,19,3]
print(tab)
quicksort(tab,0,len(tab)-1)
print(tab)