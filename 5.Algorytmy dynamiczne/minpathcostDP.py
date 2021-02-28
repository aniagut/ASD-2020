#rozwiazanie z wykorzystaniem dp:
def _mincost(G,s,t,tmp):
    #jesli koszt byl wczesniej obliczony, zwracamy go
    if tmp[s]!=None:
        return tmp[s]
    else:
        #jezeli nie to szukamy minimalnego kosztu,
        #ktory wynosi minimum z sum kosztow dojscia z s do sąsiada i oraz dojscia z i do t
        min=float('inf')
        for i in range(len(G[s])):
            t=_mincost(G,G[s][i][0],t,tmp)
            if (G[s][i][1]+t)<min:
                min=G[s][i][1]+t
        tmp[s]=min
        return min
def path_cost( G, s, t ):
    #tworzemy tablice ktora na indkesie i-tym bedzie przechowywac
    #minimalny koszt dojscia z wierzcholka i do t
    tmp=[None]*len(G)
    #koszt dojscia z wierzcholka t do t wynosi 0
    tmp[t]=0
    return _mincost(G,s,t,tmp)
G = [[(1,0), (2,1)],[(3,1), (2,0)],[(3,0)],[]]
print( path_cost( G, 0, 3 ) ) # wypisze 0
