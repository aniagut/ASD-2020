def cut_rod(prices,n,memo):
    print(memo)
    if memo[n]>=0:
        return memo[n]
    if n==0:
        q=0
    else:
        q=float('-inf')
        for i in range (1,n+1):
            q=max(q,prices[i]+cut_rod(prices,n-i,memo))
        memo[n]=q
    return q
def ciecie(prices,n):
    memo=[float('-inf')]*(n+1)
    return cut_rod(prices,n,memo)
        # 1 2 3 4 5   6 7  8  9  10
prices=[0,1,5,8,9,10,17,17,20,24,30]
n=10
print(ciecie(prices,n))