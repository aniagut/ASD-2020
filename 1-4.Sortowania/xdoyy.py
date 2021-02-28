#x^y>y^x x,y>0
#x=1 y-cos innego -> y^x wieksze lub rowne
#x=2 y=3 -> y^x wieksze
#x=2 y=4 y^x==x^y
#a ogolnie jak y wiekszy to x^y wieksze
def search(tab,x):
    p=0
    k=len(tab)-1
    while p<=k:
        m=(p+k)//2
        if tab[m]==x:
            while m<=len(tab)-1 and tab[m]==x:
                m+=1
            if m<=k:
                return m
            else:
                return None
        elif tab[m]<x:
            p=m+1
        else:
            if m-1>=0 and tab[m-1]<x:
                return m-1
            elif m-1<0:
                return m
            else:
                k=m-1
    return None

def fu(X,Y):
    Y.sort()
    ind=0
    while Y[ind]==1: ind+=1
    sum=ind
    for i in range(len(X)):
        if X[i] != 1:
            if X[i] == 2:
                idx = search(Y, 4)
            else:
                idx=search(Y, X[i])
            if idx!=None:
                sum+=len(Y)-idx
    return sum

X=[2,1,6]
Y=[1,5]
print(fu(X,Y))



