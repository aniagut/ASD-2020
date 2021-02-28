#jesli wchodzi nawias otwierajacy, to wrzucamy na stos
#jesli zmaykajacy to zdejmujemy ze stosu i sprawdzamy czy sie pokrywaja
class Stack:
    def __init__(self):
        self.s=[]
        self.top=-1
        self.size=0
    def push(self,x):
        self.top+=1
        self.size+=1
        if self.top==len(self.s):
            self.s.append(x)
        else:
            self.s[self.top]=x
    def pop(self):
        self.size-=1
        res=self.s[self.top]
        self.top-=1
        return res
    def is_empty(self):
        return self.size==0
def funkcja(nawiasy):
    s=Stack()
    n=len(nawiasy)
    for i in range(n):
        if nawiasy[i]=="(" or nawiasy[i]=="[":
            s.push(nawiasy[i])
        else:
            if s.is_empty(): return False
            res=s.pop()
            if nawiasy[i]==")":
                if res!="(":
                    return False
            elif nawiasy[i]=="]":
                if res!="[":
                    return False
    if not s.is_empty(): return False
    return True
nawiasy="((([][])))"
print(funkcja(nawiasy))