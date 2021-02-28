def fu(A,T):
    n=len(A)
    F=[0]*(T+1)
    for i in range(n):
        if A[i]<=T:
            F[A[i]]=1
    for i in range (1,T+1):
        if F[i]==0:
            idx=0
            q=float('inf')
            while idx<n and i>A[idx]:
                if 1+F[i-A[idx]]<q:
                    q=1+F[i-A[idx]]
                idx+=1
            F[i]=q
    print(F)
    return F[T]
A=[1,5,8]
sum=15
print(fu(A,sum))
