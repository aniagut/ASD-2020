def fu(lista):
    lista=sorted(lista)
    mnoznik=1
    i=len(lista)-1
    l1=0
    l2=0
    while i>=1:
        l1+=lista[i]*mnoznik
        l2+=lista[i-1]*mnoznik
        mnoznik*=10
        i-=2
    if i==0:
        l1+=lista[i]*mnoznik
    return l1+l2

lista=[5,3,0,7,4]
print(fu(lista))