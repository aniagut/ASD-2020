"""
Zadanie 1. (problem sumy podzbioru) Dana jest tablica n liczb-A.
Proszę podać i zaimplementować algorytm, który sprawdza, czy da się
wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
"""
def prsupod(A,T):
    n=len(A)
    F=[[False for i in range (T+1)] for j in range (n)]
    for i in range (n):
        F[i][0]=True
    F[0][A[0]]=True
    for i in range (1,n):
        for j in range (1,T+1):
            F[i][j]=F[i-1][j]
            if j>=A[i]:
                if F[i-1][j-A[i]]==True:
                    F[i][j]=True
    print(F)
    return F[n-1][T]
A=[3,17,15,13,43,10,8]
T=109

print(prsupod(A,T))
