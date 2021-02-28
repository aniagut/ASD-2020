"""
Mamy daną tablicę A z n liczbami(CALKOWITYMI). Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
czy w tablicy ponad połowa elementów ma jednakową wartość.
"""
def funct(arr):
    minimum=min(arr)
    maximum=max(arr)
    #rozpietosc miedzy max i min(ilosc roznych liczb jakie moga sie pojawic to max-min+1(przyklad min=-10 max=2 ilosc=13
    buckets=[0]*(maximum-minimum+1)
    #koszyk reprezentuje ilosc elementow w nim
    for i in range(len(arr)):
        #dopasowujemy tak,zeby w zerowym koszyku byl minimalny element
        buckets[arr[i]-minimum]+=1
        if buckets[arr[i]-minimum]>=len(arr)/2:
            return arr[i]
    return None
tab=[4,1,14,5,4,4,3,1,4,4,3,4214,3245,4,4,4,14,4,15,4]
print(funct(tab))