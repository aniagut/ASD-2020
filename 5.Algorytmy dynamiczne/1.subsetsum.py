def memo(set,M,i,waga):
    if M[i][waga]==True:
        return True
    elif M[i][waga]==False:
        return False
    else:
        M[i][waga]=False
        if waga>=set[i] and  memo(set,M,i-1,waga-set[i])==True:
            M[i][waga]=True
        elif memo(set,M,i-1,waga):
            M[i][waga]=True
        return M[i][waga]
def subsetsum(set,T):
    n=len(set)
    M=[[[None] for i  in range (T+1)] for i in range (n)]
    for number in range (T+1):
        M[0][number]=False
    for i in range(n):
        if set[i]<=T:
            M[i][set[i]]=True
    return memo(set,M,n-1,T)

set=[3, 34, 4, 12, 5, 2]
sum=13
print(subsetsum(set,sum))
