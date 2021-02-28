def binary(tab,p,k,x):
    while p<=k:
        m=(p+k)//2
        if tab[m]==x:
            return m
        elif tab[m]==None or tab[m]>x:
            k=m-1
        else:
            p=m+1
    return None

def find(arr,x):
    i=1
    while arr[i]!=None and arr[i]<x:
        i*=2
    if arr[i]==x:
        return i
    else:
        j=i//2
        res=binary(arr,j,i,x)
        return res

tab=[2,3,10,13,16,19,23,29,32,43,55,56,60,72,75,77,81,90,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
print(find(tab,43))
