def count_rad(A,i):
    mn=1
    for j in range(i):
        mn*=10
    C=[0]*10
    B=[0]*len(A)
    for i in range(len(A)):
        C[(A[i]//mn)%10]+=1
    for i in range(1,10):
        C[i]+=C[i-1]
    for i in range(len(A)-1,-1,-1):
        C[(A[i]//mn)%10]-=1
        B[C[(A[i]//mn)%10]]=A[i]
    for i in range(len(A)):
        A[i]=B[i]
def radix_sort(A,d):
    for i in range(d):
        count_rad(A,i)

tab=[123,186,911,241,563,810,934,252,617,820,431,576,281,123,150,314,904]
print(tab)
radix_sort(tab,3)
print(tab)