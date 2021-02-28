#Anna Gut
#Biorąc pod uwagę, fakt, że x jest rozłożone równomiernie na przedziale [0,1], wykonujemy bucket sort, który będzie rozkładał liczby
#w koszykach wzdględem potęgi do jakiej podniesione było a
#Jest n+1 koszyków, ponieważ musimy uwzględnić, że x może być równy dokładnie 1
#Otrzymane koszyki sortujemy sortowaniem przez wstawianie(mała ilość elementów więc dobra złożonść) i scalamy w odpowiedniej kolejności
#Algorytm jest poprawny, ponieważ korzystmy z faktu, że funkcja a^x dla a>1 jest rosnąca dla rosnących wartości x
#Złożoność czasowa O(n)- bucket sort ma złożoność liniową, tak samo jak insertion sort dla małych rozmiarów tablicy
#Złożoność pamięciowa O(n)-tablica z bucketami
from zad3testy import runtests
import math

def insertion_sort(tab):
   n=len(tab)
   for i in range (1,n):
       j=i-1
       key=tab[i]
       while j>=0 and tab[j]>key:
           tab[j+1]=tab[j]
           j-=1
       tab[j+1]=key

def fast_sort(tab, a):
    n=len(tab)
    buckets=[[] for i in range (n+1)]
    for i in range (n):
        buckets[int(math.log(tab[i],a)*n)].append(tab[i])
    for i in range (n+1):
        insertion_sort(buckets[i])
    idx=0
    for i in range(n+1):
        m=len(buckets[i])
        tab[idx:idx+m]=buckets[i]
        idx+=m
    return tab



runtests( fast_sort )
