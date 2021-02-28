def knapsack(W,P,MaxW):
    n=len(W)
    value=[]
    for i in range(n):
        value.append((P[i]/W[i],i))
    value.sort()
    waga=0
    idx=n-1
    profit=0
    while idx>=0 and waga<MaxW:
        przedmiot=value[idx][1]
        if W[przedmiot]<=MaxW-waga:
            waga+=W[przedmiot]
            profit+=P[przedmiot]
        else:
            profit+=(MaxW-waga)*value[idx][0]
            waga=MaxW
        idx-=1
    return profit
weight=[5,7,4,1,8,2]
profit=[4,11,1,5,10,4]
MaxW=15
print(knapsack(weight,profit,MaxW))

