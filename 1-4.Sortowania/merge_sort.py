def merge(A,p,q,r):
    i=p
    j=q+1
    tab=[]
    while i<=q and j<=r:
        if A[i]<A[j]:
            tab.append(A[i])
            i+=1
        else:
            tab.append(A[j])
            j+=1
    while i<=q:
        tab.append(A[i])
        i += 1
    while j<=r:
        tab.append(A[j])
        j += 1
    idx=0
    for k in range(p,r+1):
        A[k]=tab[idx]
        idx+=1
def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
tab=[7,16,5,14,3,20,9,1,11,17,8,19,4,1]
print(tab)
merge_sort(tab,0,len(tab)-1)
print(tab)