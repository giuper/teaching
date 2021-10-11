import sys
import random
import time

def driver(N):

    sys.path.insert(1,'./SelectImpl')
    from DetRecSelect import detRecSelect
    from RandRecSelect import randRecSelect

    print(f'{"Lista di lunghezza: ":30s}{N:>10d}')
    A=list(range(N))
    maxN=sys.getrecursionlimit()-10
    totalR=0
    nofRuns=100
    if N>=maxN:
        nofRuns=1
    for i in range(nofRuns):
        startR=time.time()
        xr=randRecSelect(A,N-1)
        finishR=time.time()
        totalR+=finishR-startR
    averageR=totalR/nofRuns
    print(f'{"Algoritmo ricorsivo probabilistico: ":40s}{averageR:10.5f}')

    if N<maxN:   
        startD=time.time()
        xd=detRecSelect(A,N-1)
        finishD=time.time()
        print(f'{"Algoritmo ricorsivo deterministico: ":40s}{finishD-startD:10.5f}')
        print(f'{"Speed-up:":30s}{(finishD-startD)/averageR:10.5f}')
        if xr!=xd:
            print("Error")
    print()
        
if __name__=='__main__':
    NN=[100,200,300,400,500,600,700,800,900,1000,2000,10**5,10**6,10**7,10**8,2*10**8]

    for N in NN:
        driver(N)
    
