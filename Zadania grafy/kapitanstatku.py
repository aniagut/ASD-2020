def kapitan(T,mapa):
    m=len(mapa)#wiersze
    n=len(mapa[0])#kolumny
    visited=[[False for i in range (n+2)] for i in range (m+2)]
    for i in range(m+2):
        visited[i][0]=True
        visited[i][n+1]=True
    for i in range(n+2):
        visited[0][i]=True
        visited[m+1][i]=True
    return DFSvis(mapa,visited,1,1,T)
def DFSvis(mapa,visited,i,j,T):
    if i==len(mapa) and j==len(mapa[0]): return True
    visited[i][j]=True
    if visited[i-1][j]==False and mapa[i-2][j-1]>T:
        return DFSvis(mapa,visited,i-1,j,T)
    if visited[i][j-1]==False and mapa[i-1][j-2]>T:
        return DFSvis(mapa,visited,i,j-1,T)
    if visited[i+1][j]==False and mapa[i][j-1]>T:
        return DFSvis(mapa,visited,i+1,j,T)
    if visited[i][j+1]==False and mapa[i-1][j]>T:
        return DFSvis(mapa,visited,i,j+1,T)
    return False
mapa=[[6,6,6,1,1,1],[1,4,6,4,4,4],[1,1,6,6,6,6],[1,1,4,4,5,6],[1,1,1,1,4,6]]
T=5
print(kapitan(T,mapa))