def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
    return i*2+1
def size(K):
    return K[0]
def heapify(K,i):
    l=left(i)
    r=right(i)
    min=i
    if l<=size(K) and K[l]<K[min]:
        min=l
    if r<=size(K) and K[r]<K[min]:
        min=r
    if min!=i:
        K[min],K[i]=K[i],K[min]
        heapify(K,min)
def build_heap_min(K):
    for i in range (size(K)//2,0,-1):
        heapify(K,i)
def heap_sort(K):
    build_heap_min(K)
    n=size(K)
    for i in range(n,1,-1):
        K[i],K[1]=K[1],K[i]
        K[0]-=1
        heapify(K,1)
    K[0]=n
def remove_median(K):
    heap_sort(K)
    if size(K)%2==1:
        result=K[(size(K)+1)//2]
        K[(size(K)+1)//2]=K[size(K)]
        K[0]-=1
        heap_sort(K)
    else:
        result=float((K[int(1+size(K))//2]+K[int(1+size(K))//2+1])/2)
    return result
def insert(K,x):
    K[0]+=1
    i=size(K)
    K.append(x)
    while K[i]<K[parent(i)]:
        K[i],K[parent(i)]=K[parent(i)],K[i]
        i=parent(i)

K=[11,14,3,20,19,1,72,34,13,10,1,21]
print(K)
build_heap_min(K)
print(K)
insert(K,7)
print(K)
