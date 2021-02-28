def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key

def bucket_sort(A):
    n=len(A)
    buckets=[[] for i in range(n)]
    for i in range(n):
        buckets[int(A[i]*n)].append(A[i])
    for i in range(n):
        insertion_sort(buckets[i])
    idx=0
    for i in range(n):
        a=len(buckets[i])
        A[idx:idx+a]=buckets[i]
        idx+=a
tab=[0.79,0.13,0.16,0.64,0.39,0.20,0.89,0.53,0.71,0.42,0.71,0.18,0.21,0.32,0.19,0.54]
print(tab)
bucket_sort(tab)
print(tab)