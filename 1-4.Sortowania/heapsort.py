#kopiecmax
#n-idx ostatniego elementu
def parent(i):
    return (i-1)//2
def left(i):
    return i*2+1
def right(i):
    return i*2+2
def heapify(A,i,n):
    l=left(i)
    r=right(i)
    max=i
    if l<=n and A[l]>A[max]:
        max=l
    if r<=n and A[r]>A[max]:
        max=r
    if max!=i:
        A[max],A[i]=A[i],A[max]
        heapify(A,max,n)
def build_heap(A,n):
    for i in range (n//2,-1,-1):
        heapify(A,i,n)
def heapsort(A):
    n=len(A)-1
    build_heap(A,n)
    for i in range (n,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i-1)
def extract_max(A,n):
    max=A[0]
    A[0]=A[n]
    heapify(A,0,n-1)
    return max
def insert(A,key,n):
    A.append(key)
    i=n+1
    while i>0 and A[parent(i)]<key:
        A[i]=A[parent(i)]
        i=parent(i)
    A[i]=key
tablica=[7,1,9,10,13,41,28,5,16,34,22,81,18]
print(tablica)
n=len(tablica)-1
build_heap(tablica,n)
insert(tablica,29,n)
print(tablica)



