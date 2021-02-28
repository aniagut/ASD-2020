"""
remove max
remove min
insert
"""
#ta sama struktura w dwoch kopcach bd miala krotke z wartoscia i numerem indeksu w 2 strukturze
def size(A):
    return A[0]
def left(i):
    return i*2
def right(i):
    return i*2+1
def parent(i):
    return i//2
def indeksowanie(A):
    for i in range(1,len(A)):
        A[i]=(A[i],i)
class Structure:
    def __init__(self,A):
        A1=[len(A)]
        A2=[len(A)]
        A1.extend(A)
        A2.extend(A)
        self.min=build_heap_min(A1)
        self.max=build_heap_max(A2)
    def removemin(self):
        res=self.min[1][0]
        indeks=self.min[1][1]
        self.min[1]=self.min[size(self.min)]
        self.min[0]-=1
        heapifymin(self.min,1)
        idx=size(self.max)
        while self.max[idx][1]!=indeks: idx-=1
        self.max[idx]=self.max[size(self.max)]
        self.max[0]-=1
        heapifymax(self.max,idx)
        return res
    def removemax(self):
        res=self.max[1][0]
        indeks=self.max[1][1]
        self.max[1]=self.max[size(self.max)]
        self.max[0]-=1
        heapifymax(self.max,1)
        idx=size(self.min)
        while self.min[idx][1]!=indeks:idx-=1
        self.min[idx]=self.min[size(self.min)]
        self.min[0]-=1
        heapifymin(self.min,idx)
        return res
    def insert(self,x):
        self.max[0]+=1
        self.min[0]+=1
        if(size(self.min)==len(self.min)):
            self.min.append(0)
            self.max.append(0)
        i=size(self.min)
        while parent(i)>0 and self.min[parent(i)][0]>x:
            self.min[i]=self.min[parent(i)]
            i=parent(i)
        self.min[i]=(x,size(self.min))
        i=size(self.max)
        while parent(i)>0 and self.max[parent(i)][0]<x:
            self.max[i]=self.max[parent(i)]
            i=parent(i)
        self.max[i]=(x,size(self.max))

def heapifymax(A,i):
    l=left(i)
    r=right(i)
    max=i
    if l<=size(A) and A[l][0]>A[max][0]:
        max=l
    if r<=size(A) and A[r][0]>A[max][0]:
        max=r
    if max!=i:
        A[i],A[max]=A[max],A[i]
        heapifymax(A,max)
def heapifymin(A,i):
    l = left(i)
    r = right(i)
    min = i
    if l <= size(A) and A[l][0] < A[min][0]:
        min = l
    if r <= size(A) and A[r][0] < A[min][0]:
        min = r
    if min != i:
        A[i], A[min] = A[min], A[i]
        heapifymin(A, min)
def build_heap_max(A):
    indeksowanie(A)
    for i in range(size(A)//2,0,-1):
        heapifymax(A,i)
    return A
def build_heap_min(A):
    indeksowanie(A)
    for i in range(size(A)//2,0,-1):
        heapifymin(A,i)
    return A

A=[4,12,10,7,5,2,3,14,1,16,7,5,2,24,8]
kopiec=Structure(A)
print(kopiec.min)
print(kopiec.max)
print(kopiec.removemax())
print(kopiec.max)
print(kopiec.min)
print(kopiec.removemin())
print(kopiec.min)
print(kopiec.max)
kopiec.insert(90)
print(kopiec.max)
print(kopiec.min)