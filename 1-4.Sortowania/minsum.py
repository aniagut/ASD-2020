def countsort(A):
    C=[0]*10
    B=[0]*len(A)
    for i in range (len(A)):
        C[A[i]]+=1
    for i in range(1,10):
        C[i]+=C[i-1]
    for i in range(len(A)-1,-1,-1):
        C[A[i]]-=1
        B[C[A[i]]]=A[i]
    for i in range(len(A)):
        A[i]=B[i]
def funkcja(A):
    countsort(A)
    liczba1=0
    liczba2=0
    mnoznik=1
    for i in range(len(A)-1,0,-2):
        liczba1+=A[i]*mnoznik
        liczba2+=A[i-1]*mnoznik
        mnoznik*=10
    if(len(A)%2==1):
        liczba1+=A[0]*mnoznik
    return liczba1,liczba2
tab=[5,3,0,7,4]
print(funkcja(tab))
