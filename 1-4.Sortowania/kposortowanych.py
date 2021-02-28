#k posortowanych o lacznej dlugosci n scala w jedna posortowana
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
    if l<=size(K) and K[l][0]<K[min][0]:
        min=l
    if r<=size(K) and K[r][0]<K[min][0]:
        min=r
    if min!=i:
        K[min],K[i]=K[i],K[min]
        heapify(K,min)

def build_heap(K):
    for i in range (size(K)//2,0,-1):
        heapify(K,i)
def get_min(K):
    result=K[1][0]
    K[1]=K[size(K)]
    K[0]-=1
    heapify(K,1)
    return result

def insert(K,x):
    K[0]+=1
    K[size(K)]=x
    i=size(K)
    while i>1 and K[parent(i)][0]>K[i][0]:
        K[parent(i)],K[i]=K[i],K[parent(i)]
        i=parent(i)

listalist = [[2, 3, 4], [2, 7, 10, 11], [3, 17, 20], [1, 222], [1, 8, 18]]
def fu(listalist):
    kopiecmin=[]
    kopiecmin.append(len(listalist))
    indeksy=[]
    for i in range (0,len(listalist),1):
        kopiecmin.append((listalist[i][0],i))
        indeksy.append(0)
    build_heap(kopiecmin)
    while size(kopiecmin)>0:
        ind=kopiecmin[1][1]
        indeksy[ind]+=1
        print(get_min(kopiecmin))
        if len(listalist[ind])>indeksy[ind]:
            insert(kopiecmin,(listalist[ind][indeksy[ind]],ind))

fu(listalist)