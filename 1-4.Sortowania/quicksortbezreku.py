def partition(arr,start,end):
    pivot=arr[end]
    idx=start
    for i in range(start,end,1):
        if arr[i]<=pivot:
            arr[i],arr[idx]=arr[idx],arr[i]
            idx+=1
    arr[idx],arr[end]=arr[end],arr[idx]
    return idx
def QuickSort(A,i,j):
    size = j -i + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = i
    top = top + 1
    stack[top] = j
    while top >= 0:
        j = stack[top]
        top = top - 1
        i = stack[top]
        top = top - 1
        p = partition(A, i, j)
        if p - 1 > i:
            top = top + 1
            stack[top] = i
            top = top + 1
            stack[top] = p - 1
        if p + 1 < j:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = j

tab=[6,5,28,10,1,42,4]
print(tab)
QuickSort(tab,0,len(tab)-1)
print(tab)