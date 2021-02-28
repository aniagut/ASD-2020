"""
Dana jest n-elementowa tablica A zawierająca liczby naturalne
(potencjalnie bardzo duże). Wiadomo, że tablica A powstała w dwóch
krokach. Najpierw wygenerowano losowo (z nieznanym rozkładem) n
różnych liczb nieparzystych i posortowano je rosnąco. Następnie
wybrano losowo ceil(log n) elementów powstałej tablicy i zamieniono
je na losowo wybrane liczby parzyste. Zaproponuj (bez
implementacji!) algorytm sortowania tak powstałych danych.
Algorytm powinien być możliwie jak najszybszy. Proszę oszacować i
podać jego złożoność czasową.
"""
def fu(arr):
    i=0
    while i<len(arr):
        flag = True #1
        j=i #1
        if arr[i]%2==0: #1
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
            while j<len(arr)-1 and (arr[j+1]<arr[j] or arr[j+1]%2==0):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                j+=1
                flag = False
        if flag==True:
            i+=1

tab=[5,7,34,23,16,31,37,41,56,28,67]
print(tab)
fu(tab)
print(tab)