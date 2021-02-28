"""
Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb
naturalnych długości n o zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) -
ma ona zwracać informację o tym, ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
Można założyć, że zawsze a >= 1, b <= k.
"""
#To nie ma O(1) ale nwm co
def count_num_in_range(arr,k,a,b):
    #zaczynamy jak countsorta ale tylko se zliczamy
    count=[0]*(k+1)
    for i in range(len(arr)):
        count[arr[i]]+=1
    for i in range(1,k+1):
        count[i]+=count[i-1]
    return count[b]-count[a-1]
tablica=[4,14,5,6,8,19,3,2,12,20,17,14,10,1,5,16,11]
print(count_num_in_range(tablica,20,7,14))
