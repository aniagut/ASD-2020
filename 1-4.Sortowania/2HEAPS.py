"""
You can use 2 heaps, that we will call Left and Right.
Left is a Max-Heap.
Right is a Min-Heap.
Insertion is done like this:
If the new element x is smaller than the root of Left then we insert x to Left.
Else we insert x to Right.
If after insertion Left has count of elements that is greater than 1 from the count of elements of Right, then we call Extract-Max on Left and insert it to Right.
Else if after insertion Right has count of elements that is greater than the count of elements of Left, then we call Extract-Min on Right and insert it to Left.
The median is always the root of Left.
So insertion is done in O(lg n) time and getting the median is done in O(1) time.
"""
def parent(i):
    return (i-1)//2
def left(i):
    return i*2+1
def right(i):
    return i*2+2
class Structure:
    def __init__(self,n):
        self.left=[None]*n
        self.right=[None]*n
        self.leftsize=0
        self.rightsize=0
    def heapifymax(self,i):
        l=left(i)
        r=right(i)
        max=i
        if l<self.leftsize and self.left[l]>self.left[max]:
            max=l
        if r<self.leftsize and self.left[r]>self.left[max]:
            max=r
        if i!=max:
            self.left[i],self.left[max]=self.left[max],self.left[i]
            self.heapifymax(max)
    def heapifymin(self,i):
        l = left(i)
        r = right(i)
        min= i
        if l < self.rightsize and self.right[l]<self.right[min]:
            min = l
        if r < self.rightsize and self.right[r] <self.right[min]:
            min = r
        if i != min:
            self.right[i], self.right[min] = self.right[min], self.right[i]
            self.heapifymin(min)
    def extractmaxL(self):
        max=self.left[0]
        self.leftsize-=1
        self.left[0]=self.left[self.leftsize]
        self.left[self.leftsize]=None
        if self.leftsize!=0:
            self.heapifymax(0)
        return max
    def extractminR(self):
        min=self.right[0]
        self.rightsize-=1
        self.right[0]=self.right[self.rightsize]
        self.right[self.rightsize]=None
        if self.rightsize!=0:
            self.heapifymin(0)
        return min

    def insert(self,x):
        if self.leftsize>0 and self.left[0]>x:
            i=self.leftsize
            self.left[self.leftsize]=x
            self.leftsize+=1
            while i>0 and x>self.left[parent(i)]:
                self.left[i]=self.left[parent(i)]
                i=parent(i)
            self.left[i]=x
        else:
            i=self.rightsize
            self.right[self.rightsize]=x
            self.rightsize+=1
            while i>0 and x<self.right[parent(i)]:
                self.right[i]=self.right[parent(i)]
                i=parent(i)
            self.right[i]=x
        if self.leftsize>self.rightsize+1:
            max=self.extractmaxL()
            self.right[self.rightsize]=max
            i=self.rightsize
            self.rightsize+=1
            while i>0 and self.right[parent(i)]>max:
                self.right[i]=self.right[parent(i)]
                i=parent(i)
            self.right[i]=max
        if self.rightsize>self.leftsize:
            min=self.extractminR()
            self.left[self.leftsize]=min
            i=self.leftsize
            self.leftsize+=1
            while i>0 and self.left[parent(i)]<min:
                self.left[i]=self.left[parent(i)]
                i=parent(i)
            self.left[i]=min
    def getmedian(self):
        if self.leftsize==self.rightsize:
            return (self.left[0]+self.right[0])/2
        else:
            return self.left[0]

A=Structure(10)
A.insert(3)
A.insert(4)
A.insert(12)
A.insert(21)
A.insert(14)
A.insert(7)
A.insert(19)
A.insert(4)
A.insert(15)
print(A.left)
print(A.right)
print(A.leftsize)
print(A.rightsize)
print(A.getmedian())






