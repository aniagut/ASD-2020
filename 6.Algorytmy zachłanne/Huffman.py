#dostajemy tablice krotek ze znakiem i frekwencją występowania
#mamy zwrocic ile minimum bitow potrzeba na zakodowanie
#funkcje pomocnicze do stworzenia struktury kopca:
def left(i):
    return i*2+1

def right(i):
    return i*2+2

def parent(i):
    return (i-1)//2

def size(A):
    return len(A)-1

def heapifymin(A,i,size):
    l=left(i)
    r=right(i)
    idx=i
    if l<=size and A[l]<A[idx]:
        idx=l
    if r<=size and A[r]<A[idx]:
        idx=r
    if i!=idx:
        A[i],A[idx]=A[idx],A[i]
        heapifymin(A,idx,size)

def build_heap(A,size):
    for i in range((size-1)//2,-1,-1):
        heapifymin(A,i,size)
#funkcja, która usuwa z kopca 2 najmniejsze elementy i dodaje do kopca ich sumę, a następnie naprawia strukturę kopca i zwraca daną sumę
def get2min(A,size):
    if size==1 or A[1]<=A[2]:
        sum=A[0]+A[1]
        A[0] = A[size]
        A[1] = sum
        heapifymin(A, 1, size - 1)
        heapifymin(A, 0, size - 1)
        return sum
    else:
        sum=A[0]+A[2]
        A[0] = A[size]
        A[2] = sum
        heapifymin(A,2,size-1)
        heapifymin(A,0,size-1)
        return sum
#funkcja zliczająca minimalną liczbę bitów: dodaje kolejno sumy stworzone z dwoch najmniejszych elementow kopca,
# poki w kopcu są co najmniej 2 elementy elementy:
#(jesli size==0 to w kopcu jest jeden element)
def huffman_len(A):
    if len(A)==0:
        return 0
    if len(A)==1:
        return A[0]
    size=len(A)-1
    build_heap(A,size)
    suma=0
    while size>0:
        suma+=get2min(A,size)
        size-=1
    return suma


print(huffman_len([ 200, 700, 180, 120, 70, 30]))
