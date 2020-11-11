import time
from sparseMatrix1 import SparseMatrix
from sparseMatrixBS import SparseMatrixBS

n=100

A=SparseMatrixBS(n,n)
B=SparseMatrixBS(n,n)

#A is the identity matrix
for i in range(A.numRows()):
    A[i,i]=1

for i in range(B.numRows()):
    B[i,i]=i

##print("Matrice A:")
##print(A)
##print()
##print("Matrice B:")
##print(B)
##print()
##
    
start=time.time()
C=A*B
end=time.time()
print("Tempo per moltiplicazione con BS",end-start)


##A=SparseMatrix(n,n)
##B=SparseMatrix(n,n)
##
###A is the identity matrix
##for i in range(A.numRows()):
##    A[i,i]=1
##
##for i in range(B.numRows()):
##    B[i,i]=i
##
####print("Matrice A:")
####print(A)
####print()
####print("Matrice B:")
####print(B)
####print()
####
##    
##start=time.time()
##C=A*B
##end=time.time()
##print("Tempo per moltiplicazione senza BS",end-start)
##
##
