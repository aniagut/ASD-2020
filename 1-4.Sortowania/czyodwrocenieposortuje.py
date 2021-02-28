#mamy liste, jesli odwrocenie pewnej podlisty sprawi ze bedzie posortowana lub juz jest posortowana to zwrocic prawde
def fu(list):
    idx=0
    while idx+1<len(list) and list[idx]<list[idx+1]:
        idx=idx+1
    if idx+1==len(list):
        return True
    else:
        konc=list[idx-1]
        pocz=list[idx]
    while idx+1<len(list) and list[idx]>list[idx+1]:
        idx=idx+1
    if idx+1==len(list):
        if list[idx]>konc:
            return True
        else:
            return False
    else:
        if pocz<list[idx+1] and list[idx]>konc:
            idx=idx+1
            while idx+1<len(list) and list[idx+1]>list[idx]:
                idx=idx+1
            if idx+1==len(list):
                return True
            else:
                return False
        else:
            return False

lista=[3,5,19,21,99,74,35,32,23]
print(fu(lista))