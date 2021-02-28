"""
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który
posortuje tę tablicę w czasie O(n).
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""

def radix(lista,dlugoscslowa):
    #petla wyznacza pozycje kolejnych liter(od ostatniej do pierwszej)
    for i in range(dlugoscslowa-1,-1,-1):
        #sortuje sortowaniem przez wstawianie
        for j in range(len(lista)):
            k=j
            while(k>=1 and lista[k][i]<lista[k-1][i]):
                lista[k],lista[k-1]=lista[k-1],lista[k]
                k-=1
def funct(arr,n):
    nowa=[]
    #tworze tablice ktora posiada tuple (dlugosc slowa,slowo)
    for i in range(len(arr)):
        nowa.append((len(arr[i]),arr[i]))
    #tworze n+1 koszykow, numer koszyka bedzie oznaczal dlugosc 0-n(wlacznie)
    buckets=[[] for i in range(n+1)]
    #do koszykow o danym indeksie daje slowo ktorego dlugosc jest rowna indeksowi
    for i in range(len(arr)):
        buckets[nowa[i][0]].append(nowa[i][1])
    #sortuje radixsortem kazdy koszyk (daje mu zawartosc koszyka i dlugosc slow w koszyku)
    for i in range(1,n+1,1):
        #sortuje jesli w koszyku jest wiecej niz jedno slowo
        if len(buckets[i])>1:
            radix(buckets[i],i)
    result=[]
    for i in range(n+1):
        result.extend(buckets[i])
    return result

tablica_slow=["ania","kota","ma","kubus","sratata","lalal","nie","pranie","micha","usmiech","jazda","dupa","hej","ho","lasy"]
print(funct(tablica_slow,66))
