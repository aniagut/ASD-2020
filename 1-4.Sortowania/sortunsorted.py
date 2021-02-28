"""
Dana jest tablica (w Pythonie - lista) arr o długości m*n,
która zawiera parami różne wartości.
"Pocięto" ją na n kawałków takich samych długości,
a następnie losowo poprzestawiano te kawałki.
Następnie elementy w każdym kawałku także losowo
poprzestawiano. Napisz funkcję sortUnsorted(arr, n)
"""
def partition(arr, lo, hi):
    pivot=arr[hi]
    i=lo
    for j in range(lo, hi):
        if arr[j]<=pivot:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i],arr[hi]=arr[hi],arr[i]
    return i

def quicksort(arr,i,j):
    if i<j:
        q=partition(arr,i,j)
        quicksort(arr,i,q-1)
        quicksort(arr,q+1,j)

def sortUnsorted(arr,n):
    length=len(arr)
    m=length//n
    for i in range (0,length,m):
        quicksort(arr,i,i+m-1)
    pom=[]
    for i in range (0,length,m):
        pom.append((arr[i],i))

    pom.sort()
    print(arr)
    print(pom)
    new=[]
    for i in range (n):
        new.extend(arr[pom[i][1]:pom[i][1]+m])
    return new
arr=[17,19,18,1,4,2,21,20,24,16,13,14]

print(sortUnsorted(arr,4))
