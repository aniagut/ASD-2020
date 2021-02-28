def search3(arr,x):
    p=0
    k=len(arr)-1
    while p<=k:
        m1=p+(k-p)//3
        m2=p+(2*(k-p))//3
        if x==arr[m1]:
            return m1
        elif x==arr[m2]:
            return m2
        elif x<arr[m1]:
            k=m1-1
        elif x>arr[m1] and x<arr[m2]:
            p=m1+1
            k=m2-1
        else:
            p=m2+1
    return -1

tab=[2,15,22,34,46,87,92,101,145,198,204,234,290]
print(tab)
print(search3(tab,198))

