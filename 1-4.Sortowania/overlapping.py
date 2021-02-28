#posortowac wzgl poczatkow i sprawdzac czy poczatek 2 przed koncem 1 i koniec 2 po koncu 1
def funkcja(A):
    intervals.sort()
    for i in range(len(intervals)-1):
        konc=intervals[i][1]
        j=i+1
        if intervals[j][0]<konc:
                print(intervals[i],intervals[j])
                return True
    return False
intervals=[(6,8),(4,5),(1,3),(5,6),(6,6),(10,13),(3,4),(5,5)]
print(funkcja(intervals))