#minimalna ilosc stacji, A-B, moze przejechac D bez tankowania
def search(stacje,odleglosc):
    p=0
    k=len(stacje)-1
    while p<=k:
        m=(p+k)//2
        if stacje[m]==odleglosc or m==k:
            return stacje[m]
        elif stacje[m]>odleglosc :
            k=m-1
        else:
            if m+1>k or stacje[m+1]>odleglosc:
                return stacje[m]
            else:
                p=m+1
def ilestacji(A,B,D,stacje):
    curr=A
    ile=0
    jakie=[]
    while curr+D<B:
        curr=search(stacje,curr+D)
        ile+=1
        jakie.append(curr)
    print(jakie)
    return ile

A=0
B=2400
D=400
stacje=[250,375,650,700,810,920,1200,1425,1675,2000,2100,2300]
print(ilestacji(A,B,D,stacje))


