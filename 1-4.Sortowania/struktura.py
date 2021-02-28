"""
Proszę zaimplementować strukturę danych, przechowującą liczby całkowite umożliwiającą następujące operacje:​

Insert(val) – wstawia do struktury liczbę całkowitą​

GetMedian() – zwraca wartość mediany przechowywanych elementów​

Czas działania powyższych funkcji powinien wynosić O(log(n))
"""

def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
    return i*2+1
def size(A):
    return A[0]
def heapify_max(A,i):
    l=left(i)
    r=right(i)
    max=i
    if l<=size(A) and A[l]>A[i]:
        max=l
    if r<=size(A) and A[r]>A[i]:
        max=r
    if max!=i:
        A[max],A[i]=A[i],A[max]
        heapify_max(A,max)
def heapify_min(A,i):
    l=left(i)
    r=right(i)
    min=i
    if l<=size(A) and A[l]<A[i]:
        min=l
    if r<=size(A) and A[r]<A[i]:
        min=r
    if min!=i:
        A[min],A[i]=A[i],A[min]
        heapify_min(A,min)
def build_heap_max(A):
    for i in range(size(A)//2,0,-1):
        heapify_max(A,i)
def build_heap_min(A):
    for i in range(size(A)//2,0,-1):
        heapify_min(A,i)
def get_maxormin(A):
    result=A[1]
    A[1]=A[size(A)]
    A[0]-=1
    heapify_max(A,1)
def get_median(A):
    while size(A)>2:
        build_heap_max(A)
        get_maxormin(A)
        build_heap_min(A)
        get_maxormin(A)
    if size(A)==1:
        return A[1]
    else:
        return (A[1]+A[2])/2

tab=[3,5,6,8,10,11,4,2,13,5,7,16]
print(get_median(tab))
tab.sort()
print(tab)
