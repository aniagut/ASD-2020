#P[i]-wartosc
#W[i]-waga
#MaxW-maksymalna waga
def knapsack(W,P,MaxW):
    n=len(W)
    F=[[0 for i in range(MaxW+1)] for j in range (n)]
    for w in range(W[0],MaxW+1):
        F[0][w]=P[0]
    for i in range (1,n):
        for w in range(1,MaxW+1):
            F[i][w]=F[i-1][w]
            if w>=W[i]:
                if F[i-1][w-W[i]]+P[i]>F[i][w]:
                     F[i][w]=F[i-1][w-W[i]]+P[i]
    return F[n-1][MaxW]
weight=[2,4,3,1]
profit=[4,3,5,3]
MaxW=7
print(knapsack(weight,profit,MaxW))