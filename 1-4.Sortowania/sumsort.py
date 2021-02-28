"""
1. Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta przyjmuje na wejściu dwie n2-elementowe
 tablice (A i B) i zapisuje w tablicy B taką permutację elementów z A, że: n−1 X i=0 B[i]¬ 2n−1 X i=n B[i]¬ ... ¬ n2−1 Xi =n2−n B[i]
. Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę oszacować i podać jej złożoność czasową.
"""
def partition(A,p,r):
    x=A[p]
    i=p
    j=r
    while i<=j:
        while i<=j and A[i]<=x:
            i+=1
        while i<=j and A[j]>x:
            j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1
    A[p],A[j]=A[j],A[p]
    return j
def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
def SumSort(A,n):
    B=[None]*(n*n)
    for i in range(0,n*n,n):
        quicksort(A,i,i+n-1)
        for j in range(0,n):
            B[(j*n)+(i//n)]=A[i+j]
    return B

A=[2,7,11,9,3,34,5,18,9,12,6,8,19,0,4,15,7,12,9,16,15,3,23,1,17]
print(SumSort(A,5))
