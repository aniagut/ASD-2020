class node:
    def __init__(self):
        self.next=None
        self.val=None


def print_list(p):
    while p!=None:
        print(p.val)
        p=p.next

def reverse(head):
    if head.next==None:
        return head
    tmp=head.next
    tmp1=reverse(tmp)
    tmp.next=head
    head.next=None
    return tmp1


head=node()
a=node()
b=node()
c=node()
head.val=7
head.next=a
a.val=4
a.next=b
b.val=8
b.next=c
c.val=3333
c.next=None
print_list(head)
print_list(reverse(head))
