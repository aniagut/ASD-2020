#rozw naiwne
def LCS(s1,s2,idx1,idx2):
    if idx1==len(s1) or idx2==len(s2):
        return 0
    if s1[idx1]==s2[idx2]:
        return 1+LCS(s1,s2,idx1+1,idx2+1)
    else:
        return max(LCS(s1,s2,idx1+1,idx2),LCS(s1,s2,idx1,idx2+1))
#dynamiczne rekurencyjne
def LCS_req(s1,s2):
    memo=[]
    for i in range(len(s1)+1):
            memo.append([None]*(len(s2)+1))
    return LCS_memo(s1,s2,0,0,memo)
def LCS_memo(s1,s2,idx1,idx2,memo):
    if memo[idx1][idx2]!=None:
        return memo[idx1][idx2]
    result=None
    if idx1==len(s1) or idx2==len(s2):
        result=0
    elif s1[idx1]==s2[idx2]:
        result=1+LCS_memo(s1,s2,idx1+1,idx2+1,memo)
    else:
        result=max(LCS_memo(s1,s2,idx1+1,idx2,memo),LCS_memo(s1,s2,idx1,idx2+1,memo))
    memo[idx1][idx2]=result
    return result
#iter dynamo
def LCS_iter(s1,s2):
    arr=[]
    for i in range (len(s1)+1):
        arr.append([0]*(len(s2)+1))
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j]:
                arr[i][j]=1+arr[i+1][j+1]
            else:
                arr[i][j]=max(arr[i+1][j],arr[i][j+1])
    return arr[0][0]


s1="abdgeffhuj"
s2="acdgxffhuy"
print(LCS(s1,s2,0,0))
print(LCS_req(s1,s2))
print(LCS_iter(s1,s2))