class Node:
    def __init__(self,nazwa,czestosc):
        self.name=nazwa
        self.cz=czestosc
        self.bits=0
        self.wezel=[]
class queue:
    def __init__(self):
        self.head=0
        self.tail=-1
        self.size=0
        self.q=[]
    def enqueue(self,x):
        self.tail+=1
        if self.tail==len(self.q):
            self.q.append(None)
        self.size+=1
        self.q[self.tail]=x
        klucz=x
        idx=self.tail-1
        while idx>=self.head and self.q[idx].cz>klucz.cz:
            self.q[idx+1]=self.q[idx]
            idx-=1
        self.q[idx+1]=klucz
    def dequeue(self):
        res=self.q[self.head]
        self.head+=1
        self.size-=1
        return res
def fu(symbole):
    n=len(symbole)
    kolejka=queue()
    for i in range (n):
        symbole[i]=Node(symbole[i][0],symbole[i][1])
        kolejka.enqueue(symbole[i])
    while kolejka.size>=2:
        a=kolejka.dequeue()
        b=kolejka.dequeue()
        nowy=Node(None,a.cz+b.cz)
        nowy.wezel=[a,b]
        nowy.wezel.extend(a.wezel)
        nowy.wezel.extend(b.wezel)
        for i in nowy.wezel:
            i.bits+=1
        kolejka.enqueue(nowy)
    ile_bitow=0
    for i in range(n):
        print((symbole[i].name,symbole[i].bits))
        ile_bitow+=symbole[i].cz*symbole[i].bits
    print(ile_bitow)


symbole=[("a",700),("b",200),("c",180),("d",120),("e",70),("f",30)]
fu(symbole)