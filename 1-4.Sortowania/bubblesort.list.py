
class node:
    def __init__(self):
        self.next=None
        self.val=None
def print_list(p):
    while p!=None:
        print(p.val)
        p=p.next

def bubble(head):
    if head==None or head.next==None:
        return head
    not_sorted=True
    while not_sorted:
        ile=0
        tmp=head
        while tmp.next!=None:
            if tmp.val>tmp.next.val:
                tmp.val ,tmp.next.val=tmp.next.val,tmp.val
                ile+=1
            tmp=tmp.next
        if ile==0:
            not_sorted=False
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
print_list(bubble(head))


