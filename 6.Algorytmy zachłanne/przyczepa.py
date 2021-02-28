#brac najciezszy mozliwy i przesuwac sie w dół
def fuckcja(ladunki,K):
    n=len(ladunki)-1
    zabrane=[]
    minroznica=float('inf')
    for i in range(n,-1,-1):
        obecnie=0
        idx=i
        tab=[]
        while idx>=0:
            if obecnie+ladunki[idx]<=K:
                obecnie+=ladunki[idx]
                tab.append(ladunki[idx])
            idx-=1
        if (K-obecnie)<minroznica:
            minroznica=(K-obecnie)
            zabrane=tab
    print(zabrane)
    return minroznica
ladunki=[1,1,2,2,4,4,4,8,16]
print(fuckcja(ladunki,27))
