"""
Proszę zaimplementować rozwiązanie problemu “Impraza firmowa” tak, by zwra-cane były imiona pracowników,
którzy idą na imprezę. Należy założyć, że pra-cownicy reprezentowani są w strukturze.
"""
#g-nie idzie
class Employee:
    def __init__(self, fun, name):
        self.emp  = []
        self.fun  = fun
        self.name = name
        self.f=-1
        self.g=-1

def fun(v):
    if v.f>=0:
        return v.f
    x=v.fun
    for vi in v.emp:
        x+=gun(vi)
    y=gun(v)
    v.f=max(x,y)
    return v.f
def gun(v):
    if v.g>=0:
        return v.g
    v.g=0
    for vi in v.emp:
        v.g+=fun(vi)
    return v.g

szef=Employee(4,"szef")
a=Employee(2,"a")
b=Employee(5,"b")
szef.emp=[a,b]
c=Employee(7,"c")
d=Employee(1,"d")
a.emp=[c,d]
e=Employee(4,"e")
f=Employee(6,"f")
b.emp=[e,f]
g=Employee(1,"g")
h=Employee(2,"h")
c.emp=[g,h]
i=Employee(3,"i")
j=Employee(3,"j")
d.emp=[i,j]
k=Employee(6,"k")
l=Employee(4,"l")
e.emp=[k,l]
m=Employee(1,"m")
n=Employee(5,"n")
f.emp=[m,n]
print(fun(szef))



