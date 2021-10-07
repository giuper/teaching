import sys
import random
import time

def DetSelect(A,k):
    pivot=A[0] 
    L=[]
    R=[]
    
    for a in A:
        if a<pivot:
            L.append(a)
        if a>pivot:
            R.append(a)
            
    l=len(L)
    if l==k:
        return pivot
    if l>k:
        return DetSelect(L,k)
    else:
        return DetSelect(R,k-l-1)

def RandSelect(A,k):
    pivot=random.choice(A)
    L=[]
    R=[]
    
    for a in A:
        if a<pivot:
            L.append(a)
        if a>pivot:
            R.append(a)
            
    l=len(L)
    if l==k:
        return pivot
    if l>k:
        return RandSelect(L,k)
    else:
        return RandSelect(R,k-l-1)
    

def driver(N):
    print(f'{"Lista di lunghezza: ":30s}{N:>10d}')
    A=list(range(N))
    maxN=sys.getrecursionlimit()-10
    totalR=0
    nofRuns=100
    if N>=maxN:
        nofRuns=1
    for i in range(nofRuns):
        startR=time.time()
        RandSelect(A,N-1)
        finishR=time.time()
        totalR+=finishR-startR
    averageR=totalR/nofRuns
    print(f'{"Algoritmo probabilistico: ":30s}{averageR:10.5f}')

    if N<maxN:   
        startD=time.time()
        DetSelect(A,N-1)
        finishD=time.time()
        print(f'{"Algoritmo deterministico: ":30s}{finishD-startD:10.5f}')
        print(f'{"Speed-up:":30s}{(finishD-startD)/averageR:10.5f}')
        
    print()
        
if __name__=='__main__':
    NN=[100,200,300,400,500,600,700,800,900,1000,2000,10**5,10**6,10**7,10**8,2*10**8]

    for N in NN:
        driver(N)
    
