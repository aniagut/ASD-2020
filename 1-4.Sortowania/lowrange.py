#find  elements in range [low, high] that are not in the array
arr1=[4,7,12,0,-6,2,10,8,5,3,9]
# tworze tablice o indeksach [0,.....,high-low](dlugosc high-low+1)
# ide po arr1,jak sie miesci w range to odznaczam w mojej tablicy 1
#ide se po mojej tablicy i wypisuje indeks+low
def funkcja(tab,low,high):
    tmp=[0]*(high-low+1)
    for i in range(len(tab)):
        if tab[i]>=low and tab[i]<=high:
            tmp[tab[i]-low]=1
    for i in range(len(tmp)):
        if tmp[i]==0:
            print(i+low)

arr=[1,14,11,51,15]
low=50
high=55
funkcja(arr,low,high)