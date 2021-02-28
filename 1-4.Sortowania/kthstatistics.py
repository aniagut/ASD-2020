def partition(A,p,r):
    piv=A[p]
    i=p
    j=r
    while i<=j:
        while i<=j and A[i]<=piv:
            i+=1
        while i<=j and A[j]>piv:
            j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1
    A[p],A[j]=A[j],A[p]
    return j
def kth_stat(A,p,r,k):
    if p<=r:
        x=partition(A,p,r)
        if x==k-1:
            return A[x]
        elif x<k-1:
            return kth_stat(A,x+1,r,k)
        else:
            return kth_stat(A,p,x-1,k)
tab=[4,10,11,5,2,3,8,1,7,6,9,12,13,16,21,4,12,21,13,7]
print(kth_stat(tab,0,len(tab)-1,10))
tab.sort()
print(tab)
