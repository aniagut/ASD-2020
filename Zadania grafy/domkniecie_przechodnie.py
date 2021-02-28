#korz z alg floyda warshalla
def domkniecie_przech(G):
    n=len(G)
    Gprim=[[False for i in range (n)] for i in range (n) ]
    for i in range (n):
        for j in range (n):
            if G[i][j]==True:
                Gprim[i][j]=True
    for k in range (n):
        for i in range (n):
            for j in range (n):
                if Gprim[i][j]==False:
                    if Gprim[i][k]==True and Gprim[k][j]==True:
                        Gprim[i][j]=True
    return Gprim


G = [ [False, True , False],[False, False, True ],[False, False, False] ]
print(domkniecie_przech( G ) )