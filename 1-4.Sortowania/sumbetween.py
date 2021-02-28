"""
 Proszę zaimplementować funkcję: int SumBetween(int T[], int from, int to, int n);
  Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej tablicy
  znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że liczby w tablicy
T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych). Zaimplementowana funkcja powinna być
możliwie jak najszybsza. Proszę oszacować jej złożoność czasową (oraz bardzo krótko uzasadnić to oszacowanie).
"""
def partition(A,p,r):
    x=A[p]
    i=p
    j=r
    while i<=j:
        while i<=j and A[i]<=x:
            i+=1
        while i<=j and A[j]>x:
            j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1
    A[p],A[j]=A[j],A[p]
    return j
def kthstatistics(A,p,r,x):
    q=partition(A,p,r)
    if q==x:
        return A[q]
    elif q<x:
        return kthstatistics(A,q+1,r,x)
    else:
        return kthstatistics(A,p,q-1,x)

def SumBetween(T,od,do, n):
    mn=kthstatistics(T,0,n-1,od)
    wk=kthstatistics(T,od+1,n-1,do)
    sum=0
    for i in range(n):
        if T[i]>=mn and T[i]<=wk:
            sum+=T[i]
    return sum

tab=[5,11,4,7,3,5,2,10,8,3,8,10,1,13,6]
print(SumBetween(tab,1,6,len(tab)))
tab.sort()
print(tab)
#nlogn??




