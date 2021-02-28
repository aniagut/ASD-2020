#minimalna odleglosc pomiedzy maximum a miniumum w wszystkich mozliwych podciagach o rozm K
#0-k,1-k+1,2-k+2
def left(i):
    return i*2
def right(i):
    return i*2+1
def parent(i):
    return i//2
def heapify_max(K,i):
    l=left(i)
    r=right(i)
    max=i
    if l<=len(K)-1 and K[l][0]>K[max][0]:
        max=l
    if r<=len(K)-1 and K[r][0]>K[max][0]:
        max=r
    if max!=i:
        K[i],K[max]=K[max],K[i]
        heapify_max(K,max)
def heapify_min(K,i):
    l = left(i)
    r = right(i)
    min=i
    if l <= len(K) - 1 and K[l][0] < K[min][0]:
        min=l
    if r <= len(K) - 1 and K[r][0] < K[min][0]:
        min=r
    if min != i:
        K[i], K[min] = K[min], K[i]
        heapify_min(K, min)
def build_heap_max(K):
    for i in range((len(K)-1)//2,-1,-1):
        heapify_max(K,i)
def build_heap_min(K):
    for i in range((len(K)-1)//2,-1,-1):
        heapify_min(K,i)
def wstaw(list,el,idx,K):
    i=0
    while list[i][1]!=idx:
        i+=1
    list[i]=(el,idx+K)

def fu(lista,K):
    newlist=[]
    for i in range(0,len(lista),1):
        newlist.append((lista[i],i))
    minodl=len(lista)
    ind=0
    while ind+K<len(lista):
        build_heap_min(newlist)
        indmin=newlist[0][1]
        build_heap_max(newlist)
        indmax=newlist[0][1]
        if indmax-indmin<minodl:
            minodl=indmax-indmin
        wstaw(newlist,newlist[ind+K][0],ind,K)
        ind+=1
    return minodl

lista=[10,4,15,10,7,1,20,4,14,56,7,19]
build_heap_max(lista)
print(lista)
build_heap_min(lista)
print(lista)
print(fu(lista,4))