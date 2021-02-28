#znajdujemy  najwiekszy termin i tworzymy tablice
#sortujemy zyskami malejaco
#jesli sie da wlozyc w czas zakonczenia to wkladamy, a jak nie to szukamy pierwszego wszesniejszego niz to miejsce, zeby sie dalo wykonac
# i tak se do konca tablicy
def findmax(arr):
    max=arr[0][0]
    n=len(arr)
    for i in range(1,n):
        if arr[i][0]>max:
            max=arr[i][0]
    return max
def sort2zmienna(arr):
   n=len(arr)
   for i in range(1,n):
       j=i-1
       key=arr[i]
       while j>=0 and arr[j][1]<key[1]:
           arr[j+1]=arr[j]
           j-=1
       arr[j+1]=key

def funkcja(zajecia):
    maxczas=findmax(zajecia)
    n=len(zajecia)
    F=[None]*maxczas
    sort2zmienna(zajecia)
    for i in range(n):
        if F[zajecia[i][0]-1]==None:
            F[zajecia[i][0]-1]=zajecia[i][1]
        else:
            idx=zajecia[i][0]-2
            while idx>=0 and F[idx]!=None: idx-=1
            if idx>=0: F[idx]=zajecia[i][1]
    profit=0
    for i in range(maxczas):
        if F[i]!=None:
            profit+=F[i]
    return profit

zajecia=[(2,7),(1,4),(8,2),(4,9),(3,5),(1,2),(4,7)]
print(funkcja(zajecia))