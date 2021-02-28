"""
Masz daną POSORTOWANĄ tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej
tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który
posortuje tablicę w czasie O(n)
"""
#tworzymy trzy buckety: do jednego wrzucamy ujemne do drugiego te w zakresie a do trzeciego te wieksze od k i scalamy
def fuct(arr,k):
    buckets=[[] for i in range(3)]
    for i in range(len(arr)):
        if arr[i]>=0 and arr[i]<=k:
            buckets[1].append(arr[i])
        elif arr[i]<0:
            buckets[0].append(arr[i])
        else:
            buckets[2].append(arr[i])
        buckets[0].sort()
        buckets[2].sort()
    result=[]
    for i in range(3):
        result.extend(buckets[i])
    return result

tablica=[1,4,-11,6,79,8,10,157,99,12,-17,15,-2,17,19,541,-4,-13,18,19,20,144]
print(tablica)
print(fuct(tablica,20))