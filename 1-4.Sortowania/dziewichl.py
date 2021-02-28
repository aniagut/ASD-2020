#N dziewczynek i N chlopcow w odleglosci 1 m w dowolnej kolejnosci
#ile najmniej metrow musza przejsc zeby dziewczynki staly najpierw
#dziewczynki-1 chlopcy-0
def fu(list, N):
    #zrobic liste indeksow od 0 do N-1 na ktorych stoja chlopcy
    #zrobic liste indeksow od N do 2N-1 na ktorych stoja dziewczyny
    #indeksy poczatkowe z 1 listy zamieniamy z poczatkowymi z drugiej
    chlopcy=[]
    dziewczyny=[]
    for i in range(0,N,1):
        if list[i]==0:
            chlopcy.append(i)
    for i in range(N,2*N,1):
        if list[i]==1:
            dziewczyny.append(i)
    suma=0
    for i in range(0,len(chlopcy),1):
        suma+=2*(dziewczyny[i]-chlopcy[i])
    return suma
lista=[0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1]
print(fu(lista,8))