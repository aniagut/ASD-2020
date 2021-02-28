def sortsort(arr,k,n):
    pom=[]
    m=n//k
    for i in range (0,n,m):
        pom.append((arr[i],i))
    pom.sort()
    wyn=[]
    while pom[0][0]<float("inf"):
        print(pom)
        wyn.append(pom[0][0])
        if pom[0][1]%m!=(m-1):
            pom[0]=(arr[pom[0][1]+1],pom[0][1]+1)
        else:
            pom[0]=(float('inf'),-1)
        pom.sort()
    return wyn
tab=[13,27,178,21,214,264,1,31,405,51,54,356,34,316,379]
print(sortsort(tab,5,15))
