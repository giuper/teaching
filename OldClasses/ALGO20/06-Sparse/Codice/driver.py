import time
from sparseMatrixBS import SparseMatrixBS
from sparseMatrix import SparseMatrix


def SomeOperations(M):
    for i in range(M.numRows()):
        M[i,i]=i
    for i in range(M.numRows()):
        M[i,i]=M[i,i+1]+i+1

for size in [1000,2000,5000,10000,20000,50000]:

    MBS=SparseMatrixBS(size,size)
    startbs=time.time()
    SomeOperations(MBS)
    endbs=time.time()
    timebs=endbs-startbs
    print("Size: ",size,"\t with Binary Search:\t",timebs)
    
    M=SparseMatrix(size,size)
    start=time.time()
    SomeOperations(M)
    end=time.time()
    timenobs=end-start
    print("Size: ",size,"\t without Binary Search:\t",timenobs)
    print("Rapporto: ",timenobs//timebs)
    print()

