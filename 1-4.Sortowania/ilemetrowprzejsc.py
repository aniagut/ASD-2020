class Node:
    def __init__(self,x,n):
        self.plec=x
        self.next=n
class Linia:
    def __init__(self):
        self.pocz=Node(None,None)
def funkcja(line,n):
    tmp=line.pocz
    idx=0
    sum1=0
    sum2=0
    while idx<n:
        if tmp.next.plec=="c":
            sum1+=idx
        idx+=1
        tmp=tmp.next
    while idx<2*n:
        if tmp.next.plec=="d":
            sum2+=idx
        idx+=1
        tmp=tmp.next
    return (sum2-sum1)*2

line=Linia()
a14=Node("c",None)
a13=Node("d",a14)
a12=Node("d",a13)
a11=Node("c",a12)
a10=Node("d",a11)
a9=Node("c",a10)
a8=Node("c",a9)
a7=Node("d",a8)
a6=Node("c",a7)
a5=Node("c",a6)
a4=Node("d",a5)
a3=Node("d",a4)
a2=Node("c",a3)
a1=Node("d",a2)
line.pocz.next=a1
print(funkcja(line,7))