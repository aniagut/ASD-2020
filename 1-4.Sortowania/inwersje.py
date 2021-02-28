def fu(lista):
    newlist=[]
    for i in range(0,len(lista),1):
        newlist.append((lista[i],i))
    newlist=sorted(newlist)
    ile=0
    for i in range(0,len(newlist)-1,1):
        j=i+1
        while j<len(newlist):
            if newlist[j][1]<newlist[i][1]:
                ile+=1
            j+=1
    return ile

print(fu(lista))
