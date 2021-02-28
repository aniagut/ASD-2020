'''
Zadanie 1
Dany jest ciąg przedziałów domkniętych [a1, b1], ..., [an, bn].
Zaproponuj (bez implementacji) algorytm, który znajduje taki przedział [at, bt],
 w którym w całości zawiera się jak najwięcej innych przedziałów.
'''
def merge(A,p,q,k,el):
    i=p
    j=q+1
    tab=[]
    while i<=q and j<=k:
        if A[i][el]<A[j][el]:
            tab.append(A[i])
            i+=1
        else:
            tab.append(A[j])
            j+=1
    while i<=q:
        tab.append(A[i])
        i+=1
    while j<=k:
        tab.append(A[j])
        j+=1
    for i in range(k-p+1):
        A[p+i]=tab[i]
def mergesort(A,p,k,el):
    if p<k:
        q=(p+k)//2
        mergesort(A,p,q,el)
        mergesort(A,q+1,k,el)
        merge(A,p,q,k,el)
def ktoryprzedzial(przedzialy):
    mergesort(przedzialy,0,len(przedzialy)-1,0)
    for i in range(len(przedzialy)):
        przedzialy[i]=(przedzialy[i][0],przedzialy[i][1],i)
    mergesort(przedzialy,0,len(przedzialy)-1,1)
    for i in range(len(przedzialy)):
        przedzialy[i]=(przedzialy[i][0],przedzialy[i][1],przedzialy[i][2],i)
    max=przedzialy[0][3]-przedzialy[0][2]
    maxidx=0
    for i in range(1,len(przedzialy)):
        if przedzialy[i][3]-przedzialy[i][2]>max:
            max=przedzialy[i][3]-przedzialy[i][2]
            maxidx=i
    return (przedzialy[maxidx][0],przedzialy[maxidx][1])
przedzialy=[(2,5),(8,10),(1,7),(2,6),(5,7)]
print(ktoryprzedzial(przedzialy))
