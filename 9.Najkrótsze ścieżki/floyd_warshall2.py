class Node:
    def __init__(self,name):
        self.name=name
        self.d=float('inf')
        self.parent=None
class Graph:
    def __init__(self,n):
        self.size=n
        self.nodes=[]
        for i in range(n):
            a=Node(i)
            self.nodes.append(a)
        self.edges=[[] for i in range (n)]
    def add_edge(self,source,dest,weight):
        self.edges[source].append((dest,weight))

def floyd_warshall(graph):
    macierz=[[float('inf')for i in range (graph.size) ] for i in range (graph.size)]
    for i in range(graph.size):
        macierz[i][i]=0
        for j in range(len(graph.edges[i])):
            u=graph.edges[i][j][0]
            weight=graph.edges[i][j][1]
            macierz[i][u]=weight
    for t in range(0,graph.size):
        for i in range(0,graph.size):
            for j in range(0,graph.size):
                macierz[i][j]=min(macierz[i][j],macierz[i][t]+macierz[t][j])
    print(macierz)
graf=Graph(9)
graf.add_edge(0,1,2)
graf.add_edge(0,2,3)
graf.add_edge(1,5,1)
graf.add_edge(1,6,3)
graf.add_edge(2,3,1)
graf.add_edge(2,4,2)
graf.add_edge(3,5,7)
graf.add_edge(3,8,1)
graf.add_edge(4,8,5)
graf.add_edge(5,6,1)
graf.add_edge(5,7,2)
graf.add_edge(6,7,8)
graf.add_edge(8,7,20)
floyd_warshall(graf)