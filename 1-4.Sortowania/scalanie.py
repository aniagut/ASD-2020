"""
Zadanie 3 [Algorytm]
Zaproponuj algorytm scalający k posortowanych
tablic w jedną posortowaną tablicę. Łączna liczba
elementów we wszystkich tablicach wynosi n.
Algorytm powinien najlepiej działać w czasie
O(n*log(k)).
"""
def scalanie(arr,k):
    lista=[]
    for i in range(0,len(arr),k):
        lista.append((arr[i],i))
    lista.sort()
    curr_idx=0
    new=[0]*len(arr)
    for i in range(0,len(arr),k):
        new[i:i+k]=arr[lista[curr_idx][1]:lista[curr_idx][1]+k]
        curr_idx+=1
    return new
tab=[28,29,30,31,14,15,16,17,1,2,3,4,41,42,43,44,24,25,26,27,8,9,10,11,99,100,101,102]
print(tab)
print(scalanie(tab,4))