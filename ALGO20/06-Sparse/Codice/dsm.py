from sparseMatrix import SparseMatrix

A=SparseMatrix(3,3)
A[0,0]=12
A[1,1]=11
A[3,3]=2

B=SparseMatrix(3,3)
B[0,0]=12
B[2,2]=22
B[3,3]=-2

C=A+B

print(C)

