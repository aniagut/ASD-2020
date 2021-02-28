'''
Zadanie 5
Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne,
 a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej liczby naturalnej x
 znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma jej w tablicy, to należy zwrócić None.
'''
def binarysearch(A,range,x):
    p=0
    k=range
    while p<=k:
        m=(p+k)//2
        if A[m]==None or A[m]>x:
            k=m-1
        elif A[m]==x:
            return m
        else:
            p=m+1
    return None


def szukanie(arr,x):
    mn=2
    while arr[mn]!=None: mn*=2
    return binarysearch(arr,mn-1,x)

tab=[2,6,10,12,16,17,21,32,35,39,41,44,46,54,57,60,64,71,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
print(szukanie(tab,72))