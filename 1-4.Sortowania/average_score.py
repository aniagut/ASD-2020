def partition(arr, lo, hi):
    pivot=arr[hi]
    i=lo
    for j in range(lo, hi):
        if arr[j]<=pivot:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i],arr[hi]=arr[hi],arr[i]
    return i
def kthstat(arr,lo,hi,idx):
    q=partition(arr,lo,hi)
    if q<idx:
        kthstat(arr,q+1,hi,idx)
    if q>idx:
        kthstat(arr,lo,q-1,idx)
def average_score(arr,n,low,hi):
    kthstat(arr,0,n-1,low-1)
    kthstat(arr,low,n-1,n-hi)
    sum=0
    for i in range(low,n-hi):
        sum+=arr[i]
    return sum/(n-low-hi)

tab=[5,11,4,13,20,16,12,25,1,7,14,4,28,17]
print(average_score(tab,len(tab),6,2))
tab.sort()
print(tab)

