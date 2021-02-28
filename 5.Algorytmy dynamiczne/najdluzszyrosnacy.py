def maximum(A):
    n=len(A)
    max=A[0]
    idx=0
    for i in range(1,n):
        if A[i]>max:
            max=A[i]
            idx=i
    return (max,idx)
def _print(A,parents,idx):
    if parents[idx]!=-1:
        _print(A,parents,parents[idx])
    print(A[idx])
def najdluzszy(A):
    n=len(A)
    F=[1]*n
    parents=[-1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[i]<F[j]+1:
                F[i]=F[j]+1
                parents[i]=j
    result=maximum(F)
    print(result[0])
    idx=result[1]
    _print(A,parents,idx)

tab=[3,1,5,7,2,4,9,3,17,3]
najdluzszy(tab)

