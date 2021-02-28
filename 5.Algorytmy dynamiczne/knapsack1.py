def knapsack(W,P,MaxW):
    n=len(W)
    M=[None]*n
    for i in range(n):
        M[i]=[0]*(MaxW+1)
    for w in range(W[0],MaxW+1):
        M[0][w]=P[0]
    for i in range(1,n):
        for w in range(1,MaxW+1):
            M[i][w]=M[i-1][w]
            if w>=W[i]:
                M[i][w]=max(M[i][w],M[i-1][w-W[i]]+P[i])
    return M[n-1][MaxW]
def memo(M,P,W,i,w):
    if M[i][w]==-1:
        M[i][w]=memo(M,P,W,i-1,w)
        if w>=W[i]:
            M[i][w]=max(M[i][w],memo(M,P,W,i-1,w-W[i])+P[i])
    return M[i][w]
def knapsack_reku(W,P,MaxW):
    n=len(W)
    M=[None]*n
    for i in range(n):
        M[i]=[-1]*(MaxW+1)
    for i in range(0,W[0]):
        M[0][i]=0
    for w in range(W[0],MaxW+1):
        M[0][w]=P[0]
    res= memo(M,P,W,n-1,MaxW)
    knapsack_wypisz(M,W,n,MaxW)
    return res
def knapsack_wypisz(M,W,n,MaxW):
    t=[]
    w=MaxW
    for i in range(n-1,0,-1):
        if M[i][w]!=M[i-1][w]:
            t.append(i)
            w-=W[i]
    t.sort()
    print(t)

waga=[7,8,4,10,4,6,4]
wartosc=[5,8,3,2,7,9,4]
print(knapsack_reku(waga,wartosc,22))