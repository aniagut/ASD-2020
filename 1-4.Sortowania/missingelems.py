#wszystkie ktore sa w przedziale,ale nie w tablicy wypisac rosnaco
def binarysearch(arr,x):
    if x>arr[len(arr)-1]:
        return len(arr)
    p=0
    k=len(arr)-1
    while p<=k:
        m=(p+k)//2
        if arr[m]==x:
            return m
        elif arr[m]>x and arr[m-1]<x:
            return m
        elif arr[m]<x and arr[m+1]>x:
            return m+1
        elif arr[m]<x:
            p=m+1
        else:
            k=m-1


def fu(arr, zakres):
    arr=sorted(arr)
    indeks=binarysearch(arr,zakres[0])
    print(arr)
    print(indeks)
    if indeks>=len(arr):
        return
    else:
        for i in range(zakres[0],arr[indeks],1):
            print(i)

        while indeks+1<len(arr) and arr[indeks]<=zakres[1]:
            if arr[indeks+1]-1!=arr[indeks]:
                for i in range(arr[indeks]+1,arr[indeks+1],1):
                    print(i)
            indeks+=1

lista=[4,31,2,19,7,10,13,61,14,16,41]
zakres=[7,15]
fu(lista,zakres)
