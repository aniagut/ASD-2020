#Anna Gut
#Wykorzystuje rekurencję ze spamientywaniem- w tablicy pod indeksem[i][j] trzymam najmniejszą możliwą wartośc bezwgzględna powstałą
#przez zsumowanie elementów od i-tego do j-tego
#trzymam również tablicę z polami parent-wiem jakiego środkowego elementu użyłam żeby zsumowana wartośc byla jak najmniejsza
#następnie odtwarzam drogę do wyniku przy pomocy funkcji display-dodaję do tablicy przez jakie pola przechodziła droga do wyniku i zwracam maksymalną wartośc z tablicy
#Złożoność czasowa O(n^2)
#Złożoność pamięciowa O(n^2)
from zad2testy import runtests


def abs(x,y):
    if x+y<0:
        return -(x+y)
    else:
        return x+y

def DP(sum,i,j,parents):
    if sum[i][j]<float('inf'):
        return sum[i][j]
    else:
        for t in range (i,j):
            q=abs(DP(sum,i,t,parents),DP(sum,t+1,j,parents))
            if q<sum[i][j]:
                sum[i][j]=q
                parents[i][j]=t
    return sum[i][j]
def display(i,j,sum,parents,tab):
    if i==j:
        return
    else:
        tab.append(sum[i][j])
        display(i,parents[i][j],sum,parents,tab)
        display(parents[i][j]+1,j,sum,parents,tab)

def opt_sum(tab):
    n=len(tab)
    parents=[[None for i in range (n)] for i in range (n)]
    sum=[[float('inf') for i in range (n)] for i in range (n)]
    for i in range (n):
        sum[i][i]=tab[i]
    DP(sum,0,n-1,parents)
    tab=[]
    display(0,n-1,sum,parents,tab)
    return(max(tab))

runtests( opt_sum )
