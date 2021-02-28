"""
Dana jest tablica zawierająca liczby rzeczywiste. Różnych wartości w
tablicy jest tylko log(n), gdzie n to rozmiar tablicy. Proszę
zaproponować algorytm sortujący tablicę w czasie O(nlog(log(n)).
Wskazówka: problem da się rozwiązać wykorzystując algorytm
wyszukiwania binarnego i dodatkową tablicę o rozmiarze log(n).
"""
#tablica tablic z licznikiem ile juz tego bylo i szukamy w niej binarnie
#[[],[],[],[],[],[]]
def binarysearch(arr,x):
    p=0
    k=len(arr)-1
    flag=True
    while p<=k:
        m=(p+k)//2
        if arr[m][0]==x:
            arr[m][1]+=1
            flag=False
            p=k+1
        elif arr[m][0]>x:
            k=m-1
        else:
            p=m+1
    if flag:
        arr.append([x,1])
        i=len(arr)-1
        while i>0 and arr[i-1][0]>arr[i][0]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
def fu(arr):
    lista=[]
    for i in range (len(arr)):
        binarysearch(lista,arr[i])
    nowa=[]
    for i in range(len(lista)):
        for j in range (lista[i][1]):
            nowa.append(lista[i][0])
    return nowa

a=[4,2,6,7,4,4,2,6,7,2,2,2,7,4,2,2,4,6,7,7,2,6,4]
print(fu(a))



