def multiply(A,B):
    if len(A[0])!=len(B):
        print("Mnożenie tych macierzy nie jest zdefniniowane")
    else:
        C=[[0 for s in range(len(A))] for m in range (len(B[0]))]
        for i in range(len(A)):
            for j in range (len(B[0])):
                for k in range(len(A[0])):
                    C[i][j]+=(A[i][k]*B[k][j])
        return C


A=[[3,4],[5,1],[1,0]]
B=[[5,6,1],[1,2,0]]
print(A)
print(B)
print(multiply(A,B))