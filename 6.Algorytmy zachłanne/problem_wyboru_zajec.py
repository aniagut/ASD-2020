def sort2zmienna(tab):
    n=len(tab)
    for i in range(1,n):
        klucz=tab[i]
        j=i-1
        while j>=0 and tab[j][1]>klucz[1]:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=klucz

def maxzajec(zajecia):
    n=len(zajecia)
    sort2zmienna(zajecia)
    zaj=1
    idx1=0
    idx2=1
    while idx2<n:
        if zajecia[idx2][0]>=zajecia[idx1][1]:
            zaj+=1
            idx1=idx2
        idx2+=1
    return zaj


zajecia=[(2,6),(5,7),(8,10),(7,9),(4,6),(3,4),(0,2),(1,5),(6,8)]
print(maxzajec(zajecia))