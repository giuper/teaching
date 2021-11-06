import sys
import random
import time
from iterativeSelect import iterSelect
from DetRandSelect import RandSelect


def driver(N):
    print(f'{"Lista di lunghezza: ":30s}{N:>10d}')
    A=list(range(N))
    totalR=0
    nofRuns=10
    for i in range(nofRuns):
        startR=time.time()
        RandSelect(A,0)
        finishR=time.time()
        totalR+=finishR-startR
    averageR=totalR/nofRuns
    print(f'{"Algoritmo probabilistico ricorsivo: ":30s}{averageR:10.5f}')

    startD=time.time()
    iterSelect(A,0)
    finishD=time.time()
    print(f'{"Algoritmo deterministico iterativo: ":30s}{finishD-startD:10.5f}')
    print(f'{"Speed-up:":30s}{(finishD-startD)/averageR:10.5f}')
        
    print()
        
if __name__=='__main__':
    NN=[5,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,10_000,20_000]

    for N in NN:
        driver(N)
    
