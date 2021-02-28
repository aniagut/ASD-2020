"""
Zaimplementuj funkcję average_score(arr, n, lowest, highest).
Funkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych (ich
rozkład nie jest znany, ale wszystkie są parami różne) i zwraca
średnią wartość podanych liczb po odrzuceniu lowest najmniejszych
oraz highest największych. Zaimplementowana funkcja powinna być
możliwie jak najszybsza. Oszacuj jej złożoność czasową (oraz bardzo
krótko uzasadnić to oszacowanie).
Ale my skupimy się tylko na algorytmie :D
"""
def partition(arr,low,high):
    piwot=arr[low]
    i=low
    j=high
    while i<=j:
        while i<=j and arr[i]<=piwot:
            i+=1
        while j>=i and arr[j]>piwot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    arr[low],arr[j]=arr[j],arr[low]
    return j

def kthstatistics(tab,low,high,K):
    i=partition(tab,low,high)
    if(i==K):
        return tab[i]
    if i>K:
        kthstatistics(tab,low,i-1,K)
    else:
        kthstatistics(tab,i+1,high,K)

def average_score(arr,n,lowest,highest):
    low = kthstatistics(arr, 0, n - 1, lowest - 1)
    high = kthstatistics(arr,0,n-1,n-highest)
    sum=0
    for i in range(n):
        if arr[i]>low and arr[i]<high:
            sum+=arr[i]
    average=sum/(n-lowest-highest)
    return average

tab=[2,3,15,8,1,9,10,5,7,11,12,18,14,13,6,0,20,4,17]
print(average_score(tab,len(tab),3,4))
