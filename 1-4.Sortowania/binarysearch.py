#wyszukiwanie połówkowe
def binarysearch(arr,x):
    p=0
    k=len(arr)-1
    while p<=k:
        sr=(p+k)//2
        if arr[sr]==x:
            return sr
        elif arr[sr]>x:
            k=sr-1
        else:
            p=sr+1
    return None

tablica=[1,4,6,8,9,10,13,19,24,56,100]
print(binarysearch(tablica,8))
