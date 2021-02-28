'''
Zadanie 6
Dana jest posortowana tablica A wielkości n zawierająca parami różne liczby naturalne.
Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.
'''
#w sumie to jak one sa naturalne to jakby mial byc taki element to wszystkie po jego lewej skoro rozne to tez by byly takimi elementami
#wiec jesli A[0]=0 to true a jak nie to nie
#no chyba ze nie jest naturalne
#no ale i tak
def search(A):
    p=0
    k=len(A)-1
    while p<=k:
        m=(p+k)//2
        if A[m]==m:
            return True
        elif A[m]>m:
            k=m-1
        else:
           p=m+1
    return False

A=[-1,0,2,10,11,15]
print(search(A))