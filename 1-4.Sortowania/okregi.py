import math
def okregi(arr,k):
    l=len(arr)
    odleglosci=[]
    for i in range(len(arr)):
        odleglosci.append(math.sqrt(arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1]))
    print(odleglosci)
    buckets=[[] for i in range(l)]
    for i in range (l):
        if odleglosci[i]==k:
            buckets[l-1].append(arr[i])
        else:
            buckets[int((odleglosci[i]*l)//k)].append(arr[i])
    for i in range(l):
        print(buckets[i])
    for i in range(l):
        for j in range(1,len(buckets[i]),1):
            k=j
            while k>=1 and (buckets[i][k][0]*buckets[i][k][0]+buckets[i][k][1]*buckets[i][k][1])<(buckets[i][k-1][0]*buckets[i][k-1][0]+ buckets[i][k-1][1]*buckets[i][k-1][1]):
                buckets[i][k],buckets[i][k-1]=buckets[i][k-1],buckets[i][k]
                k-=1
    res=[]
    for i in range(l):
        res.extend(buckets[i])
    arr[0:l]=res[0:l]

arr=[(2,3),(1,4),(-2,3),(-2,-1),(0,5),(4,1),(-3,2),(0,0),(0,1)]
print(arr)
okregi(arr,5)
print(arr)



