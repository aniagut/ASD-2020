def fu(arr1,exit):
    arr1=sorted(arr1)
    exit=sorted(exit)
    maxos=0
    counter=0
    j=0
    czas=0
    for i in range (0,len(exit),1):
        while j<len(arr1) and arr1[j]<=exit[i]:
            counter+=1
            j=j+1
        if counter>maxos:
            maxos=counter
            czas=exit[i]
        counter-=1
    return czas

arr1=[1,2,9,5,5,6,9]
exit=[4,5,12,9,12,11,10]
print(fu(arr1,exit))


