import time
from bitarray import bitarray
import hashlib
import random
import math
import sys

class bloomF:

    def __init__(self,m,k):
        self.M=m
        self.A=bitarray(m)
        self.A.setall(0)
        self.H=[]
        for i in range(k):
            hh=hashlib.sha256()
            hh.update(str(random.randint(0,2**32-1)).encode())
            self.H.append(hh)


    def insert(self,x):
        xx=x.encode()
        for hh in self.H:
            hhh=hh.copy()
            hhh.update(xx)
            index=int(hhh.hexdigest(),16)%self.M
            self.A[index]=1

    def lookup(self,x):
        xx=x.encode()
        for hh in self.H:
            hhh=hh.copy()
            hhh.update(xx)
            index=int(hhh.hexdigest(),16)%self.M
            if self.A[index]==0:
                return False
        return True
    


def esempioSemplice(M,K):
    print("Creo un Bloom filter di taglia",M," con ",K," hash function")
    B=bloomF(M,K)
    personaggi=['pluto','topolino','pluto','paperino','minnie']
    for p in personaggi:
        print("Inserisco : ",p)
        B.insert(p)
    
    p='paperoga'
    print("Cerco",p,"ed ottengo",B.lookup('paperoga'))
    
    print("Inserisco : ",p)
    B.insert('paperoga')
    print("Cerco",p,"ed ottengo",B.lookup('paperoga'))

##come varia il numero di falsi positivi come funzione
##del numero k di funzioni hash
##ottimo teorico: k=M/N*ln(2)
def falsiPositiviK(M,N):
    opt=M/N*.69
    print(f'{"N=":2s}{N:<9d}{"M=":2s}{M:<9d}')
    print(f'{"Ottimo k="}{opt:<6.3}')
    opt=math.floor(opt)
    for k in range(max(1,opt-5),opt+5):
        B=bloomF(M,k)
        print(f'{"   k=":2s}{k:<3d}')
        start=time.time()
        x="a"
        for i in range(1,N+1):
            #if i%10_000==0:
                #print(i," inserimenti")
            B.insert(x)
            x=x+"a"
        print(f'{"   Inserimento:":20s}{time.time()-start:7.3f}')
    
        fp=0
        start=time.time()
        for i in range(N+1,2*N+1):
            if B.lookup(x):
                #print("Falso positivo a ",i)
                fp+=1
            x=x+"a"
        print(f'{"   Lookup:":20s}{time.time()-start:7.3f}')
        print(f'{"   Falsi positivi:":22s}{fp/N:5.4f}')
        print()

##filtro contiene M bit
##come varia il numero di falsi positivi come funzione
##del carico L=M/N del filtro
##ottimo teorico: K=M/N*ln(2)
def falsiPositiviL(M):
    for L in range(2,14):
        N=M//L
        K=round(L*.69) 
        #print(f'{"M=":2s}{M:<7d}')
        print(f'{"   N="}{N:<10d}{"L="}{L:<3d}{" K="}{K}')
        B=bloomF(M,K)
        start=time.time()
        x="a"
        for i in range(1,N+1):
            B.insert(x)
            x=x+"a"
        print(f'{"   Inserimento:":20s}{(time.time()-start)/N:7.6f}')
        fp=0
        start=time.time()
        for i in range(N+1,2*N+1):
            if B.lookup(x):
                fp+=1
            x=x+"a"
        print(f'{"   Lookup:":20s}{(time.time()-start)/N:7.6f}')
        print(f'{"   Falsi positivi:":20s}{fp/N:5.4f}')
        print()

if __name__=='__main__':

##    for M in [100_000,1_000_000,2_000_000,5_000_000,7_000_000,10_000_000]:
##        print(f'{"M=":2s}{M:<7d}')
##        falsiPositiviL(M)
##        sys.stdout.flush()
      
    ##for M in [100_000,1_000_000,2_000_000,5_000_000,7_000_000,10_000_000]:
    for M in [10_000_000]:
        for N in [M//2, M//4, M//8 , M//16]:
            falsiPositiviK(M,N)
