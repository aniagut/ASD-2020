#kolejka FIFO first in first out
#dokladamy na koniec kolejki
#sciagamy z poczatku
#enqueue=wstaw, dequeue-pobierz i wyjmij, is_empty

#IMPLEMENTACJA TABLICOWA

class Queue:
    def __init__(self,n):
        self.S=[None]*n
        self.n=n
        self.elements=0
        self.head=0
    def enqueue(self,x):
        if self.elements==0:
            self.S[self.head]=x
            self.elements+=1
        else:
                self.S[(self.head+self.elements)%self.n]=x
                self.elements+=1

    def dequeue(self):
        x=self.S[self.head]
        self.head+=1
        self.elements-=1
        return x

    def is_empty(self):
        return self.elements==0

A=Queue(5)
A.enqueue(7)
A.enqueue(4)
A.enqueue(5)
A.enqueue(3)
print(A.head)
print(A.dequeue())
print(A.head)
A.enqueue(9)
A.enqueue(10)
print(A.S[0])


