"""
1. Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej długości.
 Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""
def insert_sort(A,poz):
  for i in range(1,len(A)):
      j=i-1
      key=A[i]
      while j>=0 and A[j][poz]>key:
          A[j+1]=A[j]
          j-=1
      A[j+1]=key

def radix_sort(A,len):
    for i in range(len-1,-1,-1):
        insert_sort(A,i)

def sortString(A):
    dl=0
    for i in range(len(A)):
        if(len(A[i])>dl):
            dl=len(A[i])
    buckets=[[] for i in range(dl+1)]
    for i in range(len(A)):
        buckets[len(A[i])].append(A[i])
    for i in range(1,dl+1):
        radix_sort(buckets[i],i)
    nowa=[]
    for i in range(dl+1):
        nowa.extend(buckets[i])
    for i in range(len(A)):
        A[i]=nowa[i]




A=["pies","kot","ania","maslo","dupa","kupa","jajco","trach","strach","krata"]
sortString(A)
print(A)


