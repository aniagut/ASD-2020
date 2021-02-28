#tablice X(x) i Y(y)
#ile par takich ze x^y>y^x
#ogolnie jesli y>x to x^y>y^x ale sa wyjatki
#jesli x=1 to nie ma par
#dla kazdego x>=2 para jest y=1
#x=2 y=3 nie spelnia
#x=2 y=4 nie spelnia
#x=3 y=2 spelnia
# wiec jesli x=2 to dopiero od y=5 spelnione
def binarysearch_id(arr,x):
    p=0
    k=len(arr)-1
    if x>arr[k]:
        return k+1
    while p<=k:
        m=(p+k)//2
        if arr[m]==x:
            return m
        elif x<arr[m] and x>arr[m-1]:
            return m
        elif x>arr[m] and x<arr[m-1]:
            return m+1
        elif x>arr[m]:
            p=m+1
        #if x<arr[m]:
        else:
            k=m-1

def fu(X,Y):
    Y=sorted(Y)
    counter=0
    for i in range(0,len(X),1):
        x=X[i]
        if x!=1:
            if Y[binarysearch_id(Y,1)]==1:
                counter+=1
            if x==3:
                if Y[binarysearch_id(Y,2)]==2:
                    counter+=1
            if x==2:
                if binarysearch_id(Y,5)<len(Y):
                    counter+=len(Y)-binarysearch_id(Y,5)
            if x!=2:
                if binarysearch_id(Y,x+1)<len(Y):
                    counter+=len(Y)-binarysearch_id(Y,x+1)
    return counter
X=[2,1,6]
Y=[1,5]
print(fu(X,Y))