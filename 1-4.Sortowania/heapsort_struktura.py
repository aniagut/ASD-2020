def parent(i):
    return (i-1)//2
def left(i):
    return i*2+1
def right(i):
    return i*2+2
class Heap:
    def __init__(self,n):
        self.h=[None]*n
        self.size=0
    def build_heap(self):
        for i in range (self.size//2,-1,-1):
            heapify(self,i)
    def heap_sort(self):
        self.build_heap()
        n=self.size
        for i in range (self.size-1,0,-1):
            self.h[0],self.h[i]=self.h[i],self.h[0]
            self.size-=1
            heapify(self,0)
        self.size=n
    def get_max(self):
        max=self.h[0]
        self.size-=1
        self.h[0]=self.h[self.size]
        heapify(self,0)
        return max
    def insert(self,key):
        self.h[self.size]=key
        i=self.size
        self.size+=1
        while i>0 and self.h[parent(i)]<key:
            self.h[i]=self.h[parent(i)]
            i=parent(i)
        self.h[i]=key

def heapify(H,i):
    max=i
    l=left(i)
    r=right(i)
    if l<H.size and H.h[l]>H.h[max]:
        max=l
    if r<H.size and H.h[r]>H.h[max]:
        max=r
    if max!=i:
        H.h[i],H.h[max]=H.h[max],H.h[i]
        heapify(H,max)
heap=Heap(20)
heap.insert(4)
heap.insert(6)
heap.insert(9)
heap.insert(1)
heap.insert(10)
heap.insert(12)
heap.insert(3)
heap.insert(25)
heap.insert(17)
heap.insert(14)
heap.insert(32)
heap.insert(10)
heap.insert(8)
heap.insert(16)
heap.insert(20)
heap.insert(6)
heap.insert(12)
heap.insert(3)
heap.insert(23)
heap.insert(19)
print(heap.h)
heap.heap_sort()
print(heap.h)