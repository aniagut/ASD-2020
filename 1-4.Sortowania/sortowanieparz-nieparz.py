#jak sie przejdzie raz od przodu raz od tylu to bd ok
def sortowanko(arr):
    n=len(arr)
    for i in range (n):
        if arr[i]%2==0:
            key=arr[i]
            while i>0 and key<arr[i-1]:
                arr[i]=arr[i-1]
                i=i-1
            arr[i]=key
    for i in range (n-1,-1,-1):
        if arr[i]%2==0:
            key=arr[i]
            while i<n-1 and key>arr[i+1]:
                arr[i]=arr[i+1]
                i=i+1
            arr[i]=key
arr=[171,213,346,122,311,415,164,571,591,110,950,673,717]
sortowanko(arr)
print(arr)


