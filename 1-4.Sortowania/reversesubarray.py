#czy odwrocenie kawalka tablicy sprawi ze bd posortowana
def funkcja(A):
    idx=0
    while idx<len(A)-1 and A[idx+1]>A[idx]: idx+=1
    if idx==len(A)-1: return True
    pocz=A[idx]
    konc=None
    if idx>0:
        konc=A[idx-1]
    while idx<len(A)-1 and A[idx+1]<A[idx]:idx+=1
    if idx==len(A)-1:
        if konc==None : return True
        if konc!=None and A[idx]<konc: return False
    else:
        if (konc!=None and A[idx]<konc) or pocz>A[idx+1]: return False
    while idx<len(A)-1:
        if A[idx+1]<A[idx]: return False
        idx+=1
    return True
tab=[1,2,5,4,3]
print(funkcja(tab))
