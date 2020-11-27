import time

funzioni=['fibMemLRU','fibMem','fibIter','fibRic']

#algoritmo iterativo
def fibIter(n):
    f,fPrec=1,1
    for i in range(3,n+1):
        f,fPrec=f+fPrec,f
    return f

#algoritmo ricorsivo senza memoizzazione
#estremamente lento
def fibRic(n):
    if n==1 or n==2:
        return 1
    return fibRic(n-1)+fibRic(n-2)
    
#algoritmo ricorsivo con memoizzazione
#esplicita
fibDict={1:1,2:1}
def fibMem(n):
    global fibDict
    
    if n in fibDict:
        return fibDict[n]
    fib=fibMem(n-1)+fibMem(n-2)
    fibDict[n]=fib
    return fib


#algoritmo ricorsivo con memoizzazione
#affidata a python

from functools import lru_cache
@lru_cache(maxsize = 1000)  #valori da memorizzare
def fibMemLRU(n):
    if n==1 or n==2:
        return 1
    return fibMemLRU(n-1)+fibMemLRU(n-2)



for fct in funzioni:
    times=time.time()
    for n in range(1,43):
        eval(fct)(n)
    timef=time.time()
    print(fct," "*(10-len(fct)),timef-times)

