#klasa pomocnicza do implementacji struktury kolejki
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
#implementacja kolejki z operacjami enqueue(x),dequeue(),is_empty()
class Queue:
    def __init__(self):
        self.size=0
        self.head=Node(None)
        self.tail=Node(None)
    def enqueue(self,x):
        new=Node(x)
        if self.size==0:
            self.head=new
            self.tail=new
            self.size+=1
        else:
            tmp=Node(None)
            tmp.next=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=new
            self.tail=new
            self.size+=1
    def dequeue(self):
        res=self.head.val
        self.head=self.head.next
        self.size-=1
        return res
    def is_empty(self):
        return self.size==0
#BFS do sprawdzania, czy istnieje w grafie ścieżka powiększająca z s do t(taka ścieżka z s do t, że każda krawędź w ścieżce
#ma dopuszczalny przepływ większy od 0
#zwraca True-jeśli udało nam się dojść z wierzchołka s do t i False-w przeciwnym przypadku
def BFS(c,s,t,parents):
    visited=[False]*len(c)
    q=Queue()
    q.enqueue(s)
    visited[s]=True
    while not q.is_empty():
        u=q.dequeue()
        for i in range(len(c[u])):
            if visited[i]==False and c[u][i]>0:
                q.enqueue(i)
                visited[i]=True
                parents[i]=u
    if visited[t]==True:
        return True
    else:
        return False
#funkcja max_flow oblicza maksymalny przepływ z wierzchołka s do t

#Dopóki istnieje ścieżka powiększająca z wierzchołka s do t w grafie-wybiera ścieżkę zawierającą krawędź o
#najmnijeszym możliwym dopuszczalnym przepływie i zwiększa maksymalny przepływ o wartość tej krawędzi

#Następnie pomniejsza maksymalny przepływ dla krawędzi w tej ścieżce o tę wartosc i o tę samą wartość powiększa
#przepływ dla krawędzi przeciwnych(żeby ,można było wycofać przepływ)

#funkcja dostaje informacje, które krawędzie zmodyfikować, dzięki pomocniczej tablicy parents

#funkcja przestaje się wykonywać w momencie, gdy w grafie nie ma już żadnej ścieżki powiększającej

def max_flow(c,s,t):
    parents=[None]*len(c)
    max_flow=0
    while BFS(c,s,t,parents):
        curr_flow=(float('inf'))
        fin=t
        while fin!=s:
            curr_flow=min(curr_flow,c[parents[fin]][fin])
            fin=parents[fin]
        max_flow+=curr_flow
        fin=t
        while fin!=s:
            u=parents[fin]
            c[u][fin]-=curr_flow
            c[fin][u]+=curr_flow
            fin=parents[fin]
    return max_flow

c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( max_flow( c, 0, 3 ) ) # wypisze 3