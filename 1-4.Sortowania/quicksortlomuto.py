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

tablica=[3,2,16,5,4,7,11,9,3,5,13]
n=len(tablica)-1
print(tablica)
quicksort(tablica,0,n)
print(tablica)