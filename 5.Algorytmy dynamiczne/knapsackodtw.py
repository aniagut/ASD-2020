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
    currw=MaxW
    curridx=n-1
    lista=[]
    while curridx>0:
        if F[curridx][currw]>F[curridx-1][currw]:
            lista.append(curridx)
            currw-=W[curridx]
        curridx-=1
    if F[curridx][currw]!=0:
        lista.append(curridx)
        for i in range(len(lista)-1,-1,-1):
            print(lista[i])
weight=[2,4,3,1]
profit=[4,3,5,3]
MaxW=7
knapsack(weight,profit,MaxW)