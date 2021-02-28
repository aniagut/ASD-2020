def partition(arr,lo,hi):
    pivot=arr[lo]
    i=lo-1
    j=hi+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i] 

def quicksort(arr,lo,hi):
    if lo<hi:
        q=partition(arr,lo,hi)
        quicksort(arr,lo,q)
        quicksort(arr,q+1,hi)

tab=[4,13,10,7,11,8,2,19,4,32,7,17]
print(tab)
n=len(tab)-1
quicksort(tab,0,n)
print(tab)