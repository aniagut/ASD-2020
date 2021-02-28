"""
Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. Proszę napisać
algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich NWD jest różny od 1.
Algorytm powinien działać jak najszybciej.
"""
from math import sqrt
def funct(arr):
    dzielniki=[0]*(len(arr)+1)
    for i in range(len(arr)):
        for j in range(2,n+1,1):
            if arr[i]%j==0:
                dzielniki[j]+=1
    print(dzielniki)
    return(max(dzielniki))
n=20
tablica=[19,6,3,11,8,7,19,4,14,20,17,7,4,11,6,10,17,3,5,15]
print(funct(tablica))

