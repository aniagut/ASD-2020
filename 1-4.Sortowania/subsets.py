#czy arr2 podzbiorem arr1
#oba nieposortowane
#elementy w obrebie jednego sa rozne od siebie
#sortowanie duzej tablicy i wyszukiwanie binarne odp elementow z malej w duzej
def binary_search(arr,x):
    p=0
    k=len(arr)-1
    while(p<=k):
        m=(p+k)//2
        if x==arr[m]:
            return True
        elif x<arr[m]:
            k=m-1
        else:
            p=m+1
    return False

def fu(arr1,arr2):
    arr1=sorted(arr1)
    for i in range(0,len(arr2),1):
        if binary_search(arr1,arr2[i])==False:
            return False
    return True

arr1=[9,21,3,13,100,91,14,57,16,81,43,12,1001,7]
arr2=[21,91,16,12,7]
print(fu(arr1,arr2))