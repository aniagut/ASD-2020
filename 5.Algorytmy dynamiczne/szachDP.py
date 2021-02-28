def szachy(szachownica):
    n=len(szachownica)
    tab=[[float("inf") for i in range (n)] for j in range (n)]
    tab[0][0]=szachownica[0][0]
    for i in range (1,n):
        tab[0][i]=szachownica[0][i]+tab[0][i-1]
    for i in range (n):
        tab[i][0]=szachownica[i][0]+tab[i-1][0]
    for i in range (1,n):
        for j in range(1,n):
            tab[i][j]=szachownica[i][j]
            if tab[i-1][j]<tab[i][j-1]:
                tab[i][j]+=tab[i-1][j]
            else:
                tab[i][j] +=tab[i][j-1]
    return tab[n-1][n-1]
szach=[[1,1,1,2,2],[2,2,1,1,2],[2,2,2,1,1],[2,2,2,2,2],[2,2,2,2,1]]
print(szachy(szach))

