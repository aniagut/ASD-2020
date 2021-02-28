def funkcja(tab):
    n=len(tab)
    tab.sort()
    currstart=tab[0]
    idx=1
    ile=1
    while idx<n:
        if tab[idx]>currstart+1:
            ile+=1
            currstart=tab[idx]
        idx+=1
    return ile
x=[0.25,0.5,1.6]
print(funkcja(x))