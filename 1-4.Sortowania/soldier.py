"""
W szeregu ustawiło się 2n żołnierzy. Połowa z nich to zwykli szeregowi, a połowa to siły specjalne. Mieli się ustawić na 2 grupy:
 najpierw szeregowi, a potem specjalni, ale sierżant zapomniał im o tym powiedzieć. Stoją teraz przypadkowo, z odstępem 1 metra
 pomiędzy kolejnymi żołnierzami. Szereg to lista struktur typu:​
class Soldier:
    type = False  # is a special soldier?​
    next = None​
Zaimplementuj funkcję distanceToIdeal(firstSoldier), która oblicza najmniejszą liczbę metrów, jaką żołnierze
 muszą sumarycznie przejść, żeby szeregowi stali po lewej od żołnierzy specjalnych (i żeby cały szereg dalej stał w tym samym miejscu).​
Uwaga: nie wymaga się sortowania listy.
"""
#te po prawej zle-te po lewej zle *2
class Soldier:
    def __init__(self):
        self.type=False
        self.next=None
def fu(soldier,n):
    p=0
    id=0
    while id<n:
        if soldier.type!=False:
            p+=id
        soldier=soldier.next
        id+=1
    k=0
    while id<2*n:
        if soldier.type==False:
            k+=id
        soldier=soldier.next
        id+=1
    return (k-p)*2

soldier=Soldier()
soldier1=Soldier()
soldier2=Soldier()
soldier3=Soldier()
soldier4=Soldier()
soldier5=Soldier()
soldier6=Soldier()
soldier7=Soldier()
soldier8=Soldier()
soldier9=Soldier()
soldier.next=soldier1
soldier1.next=soldier2
soldier2.next=soldier3
soldier3.next=soldier4
soldier4.next=soldier5
soldier5.next=soldier6
soldier6.next=soldier7
soldier7.next=soldier8
soldier8.next=soldier9
soldier1.type=True
soldier2.type=True
soldier4.type=True
soldier6.type=True
soldier8.type=True
print(fu(soldier,5))



