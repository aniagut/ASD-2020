#[a,b) liczby calkowite
def counting_sort(A,a,b):
    n=len(A)
    C=[0]*(b-a)
    B=[0]*n
    for i in range (n):
        C[A[i]-a]+=1
    for i in range (1,(b-a)):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        C[A[i]-a]-=1
        B[C[A[i]-a]]=A[i]
    for i in range(n):
        A[i]=B[i]
tab=[14,-3,10,7,5,4,-9,11,3,9,8,-5,5,3,-7,10,12,-4,6,11,-5,7,10]
print(tab)
counting_sort(tab,-10,15)
print(tab)
