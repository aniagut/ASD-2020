#sortujemy, patrzymy czy pomnozenie dwoch pierwszych z konca da wiekszy wynik niz dwoch pierwszych z poczatku,
#albo kthstat
#1-bierzemy 3 z konca
#2-bierzemy 2 z pocz 1 z konca
def countsort(A):
    min,max=0,0
    if A[0]<A[1]:
        min=A[0]
        max=A[1]
    else:
        min=A[1]
        max=A[0]
    for i in range(2,len(A)-2):
        if A[i]<A[i+1]:
            if A[i]<min:
                min=A[i]
            if A[i+1]>max:
                max=A[i+1]
        else:
            if A[i+1]<min:
                min=A[i+1]
            if A[i]>max:
                max=A[i]
    C=[0]*(max-min+1)
    B=[0]*len(A)
    for i in range(len(A)):
        C[A[i]-min]+=1
    for i in range(1,len(C)):
        C[i]+=C[i-1]
    for i in range(len(A)):
        C[A[i]-min]-=1
        B[C[A[i]-min]]=A[i]
    for i in range(len(A)):
        A[i]=B[i]
    print(A)
def opcja1(A):
    n=len(A)-1
    countsort(A)
    return max(A[n]*A[n-1]*A[n-2],A[0]*A[1]*A[n])
A=[3,1,-11,7,9,10,3,-40,8,6,2,4,7,5,10,2,7,6]
print(opcja1(A))
