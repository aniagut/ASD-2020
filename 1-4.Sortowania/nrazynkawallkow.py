def funkcja(tab,n):
    lista=[]
    for i in range(0,len(tab),n):
        lista.append((tab[i],tab[i+n-1],i))
    for j in range(1,len(lista)):
        i=j-1
        key=lista[j]
        pocz=lista[j][0]
        konc=lista[j][1]
        while i>=0 and pocz<=lista[i][0] and konc<=lista[i][0]:
            lista[i+1]=lista[i]
            i-=1
        lista[i+1]=key
    new=[]
    for i in range(n):
        new.extend(tab[lista[i][2]:lista[i][2]+n])
    for i in range(len(tab)):
        tab[i]=new[i]

tab=[4,7,9,11,0,1,2,3,29,31,34,36,11,11,11,11]
print(tab)
funkcja(tab,4)
print(tab)