
#implementazione ricorsiva della funzione fattoriale
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

#implementazione iterativa della funzione fattoriale
def iterFact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

#stampa tutte le cifre decimali di n
#ciascuna su una riga differente
#a partire dalle unita'
#se passate n negativo, avrete una brutta sorpresa
#se propio volete farlo, usare un assert

def stampa(n):
    if n<=9:
        print(n)
    else:
        print(n%10)   #stampa la cifra delle unita'
        stampa(n//10) #stampa tutto il resto ricorsivamente


#algoritmo ricorsivo senza memoizzazione
#estremamente lento
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1

    return fib(n-1)+fib(n-2)
    
fibDict={1:1,2:1}

def fibMem(n):
    global fibDict
    
    if n in fibDict:
        return fibDict[n]

    fib=fibMem(n-1)+fibMem(n-2)
    fibDict[n]=fib
    return fib








    
