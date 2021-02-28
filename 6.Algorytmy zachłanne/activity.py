def tasks(A):
    #algorytm będzie wybierac zajęcia w kolejnosci najwczesniej konczących się, tak by nie zachodzily na siebie
    B=[]
    #tworzę pomocniczą tablicę B, która będzie przechowywac krotki o zawartosci(ei,bi)
    for i in range(len(A)):
        B.append((A[i][1],A[i][0]))
    # sortuję w kolejnosci zakonczenia sie zajec
    B.sort()
    #licznik-ile zajec wybralismy, idx-na ktorym elemencie w tablicy B jestesmy
    #f-oznacza koniec ostatniej wybranej aktywnosci
    licznik,idx,f=0,0,0
    while idx<len(B):
        if B[idx][1]>=f:
            licznik+=1
            f=B[idx][0]
        idx+=1
    return licznik

print(tasks([(0,10),(10,20),(5,15)]))

