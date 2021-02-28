"""
Zadanie 1.Dana jest tablica A o rozmiarze n, zawierająca liczby ze zbioru
 {0, ..., n^2-1}. Proszę podać algorytm sortujący tę tablicę w czasie O(n)
"""
def countsort(arr,dziel,modulo):
    n=len(arr)
    A=[0]*modulo
    B=[0]*n
    for i in range(n):
        A[(arr[i]//dziel)%modulo]+=1
    for i in range (1,modulo):
        A[i]+=A[i-1]
    for i in range (n-1,-1,-1):
        A[((arr[i])//dziel)%modulo]-=1
        B[A[((arr[i]//dziel)%modulo)]]=arr[i]
    for i in range (n):
        arr[i]=B[i]


def radixsort(arr,n):
        countsort(arr,1,n)
        print(arr)
        countsort(arr,n,n)
arr=[32,11,4,15,6,7]
radixsort(arr,6)
print(arr)