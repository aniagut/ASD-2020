class node:
    def __init__(self):
        self.next=None
        self.val=None
def print_list(p):
    while p!=None:
        print(p.val)
        p=p.next

def selection(head):
    if head==None or head.next==None:
        return head
    tmp=head
    while tmp.next!=None:
        najm=tmp.val
        wsk=tmp
        temp=tmp.next
        while temp!=None:
            if temp.val<najm:
                najm=temp.val
                wsk=temp
            temp=temp.next
        tmp.val,wsk.val=najm,tmp.val
        tmp=tmp.next
    return head

head=node()
a=node()
b=node()
c=node()
d=node()
e=node()
head.val=4
a.val=8
b.val=2
c.val=6
d.val=10
e.val=0
head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=None
print_list(head)
print()
print_list(selection(head))
