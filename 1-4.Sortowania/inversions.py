def merge(A,p,q,r):
    inversions=0
    i=p
    j=q+1
    B=[]
    while i<=q and j<=r:
        if A[i]<=A[j]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[j])
            inversions+=1
            j+=1
    while i<=q:
        B.append(A[i])
        i+=1
    while j<=r:
        B.append(A[j])
        j+=1
    for i in range(len(B)):
        A[p+i]=B[i]
    return inversions

def mergesort(A,p,r,count):
    if p<r:
        q=(p+r)//2
        mergesort(A,p,q,count)
        mergesort(A,q+1,r,count)
        count[0]+=merge(A,p,q,r)
def inversion_sum(A):
    count=[0]
    mergesort(A,0,len(A)-1,count)
    return count[0]
A=[8,4,1,11,2,5,0,6]
print(inversion_sum(A))
print(A)