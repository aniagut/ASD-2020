"""
Zadanie 2 [Algorytm, implementacja]
Dana jest tablica zawierająca liczby naturalne. Proszę
zaimplementować funkcję odpowiadającą na pytanie czy
w tablicy jest para sumująca się do jakiejś liczby x.
Funkcja powinna być jak najszybsza.
findPair(arr, x) -> bool.
"""
def merge(arr,p,k,m):
    i=p
    j=m+1
    tmp=[]
    while i<=m and j<=k:
        if arr[i]<arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=m:
        tmp.append(arr[i])
        i+=1
    while j<=k:
        tmp.append(arr[j])
        j+=1
    n=0
    for m in range(p,k+1,1):
        arr[m]=tmp[n]
        n+=1
def mergesort(arr,p,k):
    if p<k:
        m=(p+k)//2
        mergesort(arr,p,m)
        mergesort(arr,m+1,k)
        merge(arr,p,k,m)
#sortujemy merge a potem wsk na pocz i koniec tab
def findpair(arr,x):
    i=0
    j=len(arr)-1
    mergesort(arr,i,j)
    while i<j:
        if arr[i]+arr[j]==x:
            return True
        elif arr[i]+arr[j]>x:
            j-=1
        else:
            i+=1
    return False
tab=[13,4,9,7,16,2,5,14,20,5,10]
print(findpair(tab,7))
