'''
Dana jest nieposortowana tablica A.
Należy znaleźć maksymalną różnicę pomiędzy kolejnymi elementami w porządku posortowanym.
Zadanie należy rozwiązać w czasie liniowym.
'''
def funkcja(A):
    if A[0]<A[1]:
        min=A[0]
        max=A[1]
    else:
        min=A[1]
        max=A[0]
    for i in range(2,len(A)-1,2):
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
    buckets=[False]*(max-min+1)
    for i in range(len(A)):
        buckets[A[i]-min]=True
    maxroznica=0
    i=0
    while i<(max-min+1):
        curr=0
        while i<(max-min+1) and buckets[i]==False:
            curr+=1
            i+=1
        if curr>maxroznica:
            maxroznica=curr
        i+=1
    return maxroznica+1

tab=[4,13,1,7,5,12,4,16,21,32,90,54,46,76,28,13]
print(funkcja(tab))
tab.sort()
print(tab)
