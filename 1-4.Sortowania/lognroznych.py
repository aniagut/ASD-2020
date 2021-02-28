"""
3. Jak posortować n-elementową tablicę liczb rzeczywistych, które przyjmują tylko logn różnych wartości?
Uzasadnić poprawność algorytmu i oszacować złożoność. (Nie trzeba implementować).
"""
#tworzymy liste krotek o dlugosci log n ktora bd zawierac (liczba,ile juz ich)
#jesli w liscie jest juz liczba-zwiekszamy ilosc, jesli nie to dodajemy z iloscia 1
#dodajac kolejna liczbe wstawiamy ja na odp miejsce
def search(lista,x):
    flag=True
    if len(lista)>0:
        p = 0
        k = len(lista) - 1
        while p<=k and flag:
            m=(p+k)//2
            if lista[m][0]==x:
                lista[m]=(lista[m][0],lista[m][1]+1)
                flag=False
            elif lista[m][0]>x:
                k=m-1
            else:
                p=m+1
    if flag:
        lista.append((x,1))
        l=len(lista)-2
        while(l>=0 and lista[l][0]>x):
            lista[l+1]=lista[l]
            l-=1
        lista[l+1]=(x,1)
def fu(A,n):
    B=[]
    for i in range(len(A)):
        search(B,A[i])
    new=[]
    for i in range(len(B)):
        for j in range(B[i][1]):
            new.append(B[i][0])
    for i in range(len(A)):
        A[i]=new[i]
tab=[3,1,1,0,4,1,1,4,1,3,0,0,1,4,3,1,0,3,1,4,0]
fu(tab,len(tab)-1)
print(tab)


