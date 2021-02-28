#wybrac jak najwiecej zajec, tak zeby zadne na siebie nie zachodziły
#ALGORYTM:
#1. wybieram zajecia kończące się najwcześniej
#2.dyskfalifikuje wszystkie zajęcia, które na nie nachodzą
#3.jeśli zostały jeszcze jakieś zajęcia, to powtarzam od pkt 1.
#jedna tablica z krotkami (s,f), zwraca tylko ilosc aktywnosci
def activity_selection(A):
    B=[]
    for i in range(len(A)):
        B.append((A[i][1],A[i][0]))
    B.sort()
    licznik=0
    idx=0
    f=0
    while idx<len(B):
        if B[idx][1]>=f:
            licznik+=1
            f=B[idx][0]
        idx+=1
    return licznik
#jedna tablica z krotkami, zwraca indeksy w A
def activity_selection1(A):
    B=[]
    for i in range(len(A)):
        B.append((A[i][1],i))
    B.sort()
    licznik=0
    idx=0
    f=0
    while idx<len(B):
        if A[B[idx][1]][0]>=f:
            licznik+=1
            f=B[idx][0]
            print(B[idx][1])
        idx+=1
#printuje całą krotkę
def activity_selection2(A):
    B=[]
    for i in range(len(A)):
        B.append((A[i][1],i))
    B.sort()
    licznik=0
    idx=0
    f=0
    while idx<len(B):
        if A[B[idx][1]][0]>=f:
            licznik+=1
            f=B[idx][0]
            print(A[B[idx][1]])
        idx+=1


A=[(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
print(activity_selection(A))
activity_selection1(A)
activity_selection2(A)


