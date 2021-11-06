import time
from bitarray import bitarray
import hashlib
import random

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
    


B=bloomF(20,2)
personaggi=['pluto','topolino','pluto','paperino','minnie']
for p in personaggi:
    print("Inserisco : ",p)
    B.insert(p)
p='paperoga'
print(p,B.lookup('paperoga'))
print("Inserisco : ",p)
B.insert('paperoga')
print(p,B.lookup('paperoga'))

N=1_000_000
M=N//5
d=6

B=bloomF(N,d)
x="a"
start=time.time()
print("Inseriamo ",M," elementi in un filtro con ", N," posizioni")
print("Usiamo ",d,"hash function")
for i in range(1,M+1):
    if i%10_000==0:
        print(i," inserimenti")
    B.insert(x)
    x=x+"a"
print("Tempo per ",M," inserimenti ",time.time()-start)

print("Eseguiamo il lookup di ", M," elementi non nel filtro")
fn=0
start=time.time()
for i in range(M+1,2*M+1):
    if B.lookup(x):
        print("Falso negativo a ",i)
        fn+=1
    x=x+"a"
print("Tempo per ",M," lookup ",time.time()-start)
print(fn," falsi negativi su ",M," lookup")

