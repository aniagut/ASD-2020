arr1=[1,2,9,5,5]
exit=[4,5,12,9,12]
#posortowac jedno i drugie i patrzec dawac ludzi do srodka poki nie bd czasu wyjscia pierwszej osoby
def impreza(arr1,exit):
    arr1.sort()
    exit.sort()
    max=0
    idx=0
    midx=0
    osoby=0
    for i in range(len(exit)):
        czas=exit[i]
        while idx<len(arr1) and arr1[idx]<=czas:
            osoby+=1
            idx+=1
        if osoby>max:
            max=osoby
            midx=idx-1
        osoby = osoby - 1
    return max,arr1[midx]
print(impreza(arr1,exit))
