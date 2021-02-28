#Anna Gut
#Korzystam ze zmodyfikowanego algorytmu Dijkstry do znajdowania najkrótszych ścieżek w grafie-modyfikacja polega na tym,
#że w kolejce priorytetowej oprócz wierzchołka umieszczam także informację o tym, jakim środkiem transportu weszliśmy do danego wierzchołka(liczba 1, 5 lub 8)
#i wychodzę z niego do innego tylko wtedy, gdy krawędź wychodząca, reprezentująca środek transportu ma inną wartość niż wchodząca
#Uzasadnienie poprawności-korzystam z poprawnego algorytmu dijkstry do znajdywania najkrótszych ścieżek
#Złożoność czasowa-O(ElogV), gdzie E-liczba krawędzi, V-liczba wierzchołków
#Złożoność pamięciowa
from zad1testy import runtests
class PriorityQueue:
    def __init__(self,n):
        self.q=[None]*n
        self.head=0
        self.tail=-1
        self.elements=0
    def put(self,x,distances):
        self.tail+=1
        self.elements+=1
        self.q[self.tail]=x
        i=self.tail
        while i>self.head and distances[x[0]]<distances[self.q[i-1][0]]:
            self.q[i]=self.q[i-1]
            i-=1
        self.q[i]=x
    def get(self):
        res=self.q[self.head]
        self.head+=1
        self.elements-=1
        return res
    def is_empty(self):
        return self.elements==0

def dijkstra(G,s,t):
    n=len(G)
    distances=[float("inf")]*n
    distances[s]=0
    q=PriorityQueue(100)
    q.put((s,0),distances)
    while not q.is_empty():
        v=q.get()
        for i in range (n):
            if G[v[0]][i]>0 and G[v[0]][i]!=v[1]:
                if distances[i]>distances[v[0]]+G[v[0]][i]:
                    distances[i]=distances[v[0]]+G[v[0]][i]
                    q.put((i,G[v[0]][i]),distances)
    return distances[t]
def islands(G, A, B):
    x=dijkstra(G,A,B)
    if x<float('inf'):
        return x
    else:
        return None
runtests( islands ) 
