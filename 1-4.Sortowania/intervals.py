def func(interwaly):
    interwaly=sorted(interwaly)
    i=0
    pokr=[]
    while i<len(interwaly)-1:
        j=i+1
        while interwaly[i][0]<interwaly[j][0] and interwaly[i][1]>interwaly[j][0]:
            if interwaly[i][1]<interwaly[j][1]:
                pokr.append((interwaly[i][0],interwaly[i][1]))
                pokr.append((interwaly[j][0],interwaly[j][1]))
                return pokr
            j=j+1
        i=i+1
    return -1

interwaly=[(1,3),(2,3),(3,6),(4,6),(6,9),(7,8),(25,26),(10,99),(98,100)]
print(func(interwaly))
