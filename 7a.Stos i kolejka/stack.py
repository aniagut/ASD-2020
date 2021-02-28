#stos LIFO -odkladanie na szczyt i sciaganie ze szczytu
#push,pop,is_empty

#IMPLEMENTACJA TABLICOWA
class Stack:
    #n-rozmiar
    def __init__(self,n):
        self.S=[None]*n
        self.n=n
        self.elements=0
    def push(self,x):
        self.S[self.elements]=x
        self.elements+=1
    def pop(self):
        self.elements-=1
        return self.S[self.elements]
    def is_empty(self):
        return self.elements==0

A=Stack(10)
A.push(6)
A.push(4)
A.push(8)
A.push(16)
print(A.pop())
print(A.elements)
A.pop()
A.pop()
A.pop()
print(A.is_empty())
