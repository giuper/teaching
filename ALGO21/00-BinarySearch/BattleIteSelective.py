import sys
import random
import time
from DetIteSelect import detIteSelect
from RandIteSelect import randIteSelect

def driver(N):
    print(f'{"Lista di lunghezza: ":30s}{N:>10d}')
    A=list(range(N))
    totalR=0
    nofRuns=10
    for i in range(nofRuns):
        startR=time.time()
        xr=randIteSelect(A,N-1)
        finishR=time.time()
        totalR+=finishR-startR
    averageR=totalR/nofRuns
    print(f'{"Algoritmo iterativo probabilistico: ":40s}{averageR:10.5f}')

    startD=time.time()
    xd=detIteSelect(A,N-1)
    finishD=time.time()
    print(f'{"Algoritmo iterativo deterministico: ":40s}{finishD-startD:10.5f}')
    print(f'{"Speed-up:":30s}{(finishD-startD)/averageR:10.5f}')
    if xr!=xd:
        print("Error")
    print()
        
if __name__=='__main__':
    NN=[100,200,300,400,500,600,700,800,900,1000,2000,10**5,10**6,10**7,10**8,2*10**8]

    for N in NN:
        driver(N)
    
