def fibDP(n):
    F=[1]*(n+1)
    for i in range (2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]
def fibbetterDP(n):
    Fi=1
    Fj=1
    for i in range(2,n+1):
        F=Fi+Fj
        Fi,Fj=Fj,F
    return Fj
def fibmemo(F,n):
    if F[n]==0:
        F[n]=fibmemo(F,n-1)+fibmemo(F,n-2)
    return F[n]
def fibDPreku(n):
    F=[0]*(n+1)
    F[0],F[1]=1,1
    return fibmemo(F,n)

#print(fibDP(100000))
print(fibbetterDP(100000))
#print(fibDPreku(997))
