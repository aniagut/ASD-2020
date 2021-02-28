class Soldier:
    type=False
    next=None
def distanceToIdeal(firstSoldier):
    suma=0
    metry=0
    while firstSoldier!=None:
        if firstSoldier.type==False:
            suma+=metry
        metry+=1
        firstSoldier=firstSoldier.next
    metry=metry//2
    licznik=0
    for i in range (metry):
        licznik+=i
    return (suma-licznik)*2
a=Soldier()
b=Soldier()
c=Soldier()
d=Soldier()
e=Soldier()
f=Soldier()
g=Soldier()
h=Soldier()
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=h
h.next=None
b.type=True
c.type=True
e.type=True
h.type=True
print(distanceToIdeal(a))




