class Employee:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.f=-1
        self.g=-1
    def F(self):
        if self.f>=0:
            return self.f
        else:
            x=self.fun
            for vi in self.emp:
                x+=vi.G()
            y=self.G()
            self.f=max(x,y)
            return self.f
    def G(self):
        if self.g>=0:
            return self.g
        self.g=0
        for vi in self.emp:
            self.g+=vi.F()
        return self.g
a=Employee(7)
b=Employee(5)
c=Employee(10)
a.emp=[b,c]
d=Employee(4)
e=Employee(11)
b.emp=[d,e]
f=Employee(2)
g=Employee(9)
c.emp=[f,g]
h=Employee(13)
i=Employee(1)
d.emp=[h,i]
j=Employee(17)
k=Employee(5)
e.emp=[j,k]
l=Employee(7)
m=Employee(4)
f.emp=[l,m]
n=Employee(2)
o=Employee(12)
g.emp=[n,o]
p=Employee(8)
r=Employee(3)
h.emp=[p,r]
s=Employee(5)
t=Employee(2)
i.emp=[s,t]
print(a.F())