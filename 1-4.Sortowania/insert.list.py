class node:
    def __init__(self):
        self.val=None
        self.next=None
        self.prev=None

def printlist(head):
    while head!=None:
        print(head.val)
        head=head.next


def insertionSort(head):
    #sortowanie przez wstawianie
    #pierwszy posortowany
    if head==None or head.next==None:
        return head
    else:
        tmp=head.next
    while tmp!=None:
        temp=tmp
        while temp.prev!=None and temp.prev.val>temp.val:
            temp.prev.val,temp.val=temp.val,temp.prev.val
            temp=temp.prev
        tmp=tmp.next

head=node()
a=node()
b=node()
c=node()
d=node()
e=node()
head.val=6
a.val=9
b.val=4
c.val=5
d.val=1
e.val=3
head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=None
head.prev=None
a.prev=head
b.prev=a
c.prev=b
d.prev=c
e.prev=d
printlist(head)
insertionSort(head)
print()
printlist(head)