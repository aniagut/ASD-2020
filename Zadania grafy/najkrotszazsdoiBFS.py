class Node:
    def __init__(self,v):
        self.v=v
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def is_empty(self):
        if self.head==None:
            return True
    def enqueue(self,x):
        new = Node(x)
        if self.is_empty():
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new
    def dequeue(self):
        res=self.head.v
        if self.head.v==self.tail.v:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
        return res
def BFS(G,s,t,dist,paths):
    #tablica bedzie przechowywac informacje o tym czy wierzcholek zostal juz przetworzony
    visited=[False]*len(G)
    q=Queue()
    #umieszczamy w kolejce pierwszy wierzcholek
    q.enqueue(s)
    paths[s]=1
    dist[s]=0
    while not q.is_empty():
        #usuwamy z kolejki aktualnie przetwarzany wierzcholek
        curr=q.dequeue()
        #przeglądamy jego sąsiadów
        for i in range (len(G[curr])):
            if G[curr][i]==True:
                if visited[i]==False:
                    q.enqueue(i)
                    visited[i]=True
                #jesli znajdziemy krotszą niz dotychczasowa sciezkę-umieszczamy jej dlugosc w tablicy dist
                if dist[i]>dist[curr]+1:
                    dist[i]=dist[curr]+1
                    paths[i]=paths[curr]
                #jesli znajdziemy sciezkę, ktorej dlugosc jest rowna obecnie najkrotszej-zwiekszamy ilosc najkrotszych sciezek
                elif dist[i]==dist[curr]+1:
                    paths[i]+=paths[curr]
    #zwracamy najkrotsza sciezke z s do t
    return paths[t]
def count_shortest_paths(G,s,t):
    #tablica bedzie przechowywac pod i-tym indeksem najkrotsza odleglosc od wierzcholka s do i
    dist=[float('inf')]*len(G)
    #tablica bedzie przechowywac pod i-tym indeksem, ile jest najkrotszych sciezek z s do i
    paths=[0]*len(G)
    return BFS(G,s,t,dist,paths)
G = [[False, True, True, False],[False, False, True, True ],[False, False, False, True ],[False, False, False, False]]
print( count_shortest_paths( G, 0, 3 )) # wypisze 2
