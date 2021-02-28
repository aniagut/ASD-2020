def knapsackreku(F,W,P,przedm,waga):
    if F[przedm][waga]!=None:
        return F[przedm][waga]
    else:
        F[przedm][waga]=knapsackreku(F,W,P,przedm-1,waga)
        if waga>=W[przedm]:
            wart=knapsackreku(F,W,P,przedm-1,waga-W[przedm])+P[przedm]
            if wart>F[przedm][waga]:
                F[przedm][waga]=wart
    return F[przedm][waga]
def knapsack(W,P,MaxW):
    n=len(W)
    F=[[None for i in range(MaxW+1)] for j in range (n)]
    for i in range (MaxW+1):
        F[0][i]=0
    for w in range(W[0],MaxW+1):
        F[0][w]=P[0]
    return knapsackreku(F,W,P,n-1,MaxW)
weight=[2,4,3,1]
profit=[4,3,5,3]
MaxW=7
print(knapsack(weight,profit,MaxW))