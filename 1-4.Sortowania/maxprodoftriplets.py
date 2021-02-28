def fu(list):
    positive=[]
    negative=[]
    list=sorted(list)
    i=0
    while i<len(list) and list[i]<0:
        negative.append(list[i])
        i=i+1
    while i<len(list):
        positive.append(list[i])
        i=i+1
    if len(negative)>=2:
        if len(positive)>=2:
            if negative[0]*negative[1]>positive[len(positive)-1]*positive[len(positive)-2]:
                return negative[0]*negative[1]*positive[len(positive)-1]
            else:
                return positive[len(positive)-1]*positive[len(positive)-2]*positive[len(positive)-3]
        elif len(positive)==1:
            return negative[0] * negative[1] * positive[len(positive) - 1]
        else:
            return negative[len(negative)-1]*negative[len(negative)-2]*negative[len(negative)-3]
    else:
        return positive[len(positive)-1]*positive[len(positive)-2]*positive[len(positive)-3]

list=[-10,-3,-5,-6,-20]
print(fu(list))