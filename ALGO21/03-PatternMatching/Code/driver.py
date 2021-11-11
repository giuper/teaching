from BF import bfPM
from KMP import kmpPM
from RK import prepareText, lookup
import time

def driver(verbose=False):
    PP=["aaab","aaac","caab","caaa","aaaa","abaa","aaba","baaa",]
    
    for SIZE in [1_000,10_000,50_000,100_000,1_000_000,5_000_000,8_000_000]:
        print(f'{"Testo di lunghezza:":35s}{SIZE:10d}')
        print(f'{"Numero di pattern:":35s}{len(PP):10d}')
        T="a"*SIZE+"b"
    
        totaltime=0
        bfnom=[]
        for P in PP:
            start=time.time()
            bfres=bfPM(T,P)
            totaltime+=time.time()-start
            bfnom.append(len(bfres)-1) #il primo elemento e' il numero di conf
            err=False
            if verbose:
                print("Verifico match trovati da Forza Bruta per pattern: ",P,end=' ')
            for i in bfres[1:]:  #il primo elemento e' il numero di confronti
                if P!=T[i:i+len(P)]:
                    print("\nErrore algoritmo Forza Bruta")
                    print("Pattern: ",P)
                    print("Testo  : ",T[i,i+len(P)])
                    print("Posiz. : ",i)
                    err=True
            if verbose and not err:
                print("--> nessun errore")
            
        print(f'{"Tempo Algoritmo di Forza Bruta: ":35s}{totaltime:10.6f}')
        
        totaltime=0
        kmpnom=[]
        for P in PP:
            start=time.time()
            kmpres=kmpPM(T,P)
            totaltime+=time.time()-start
            kmpnom.append(len(kmpres)-1) #il primo elemento e' il numero di conf
            err=False
            if verbose:
                print("Verifico match trovati da KMP per pattern:        ",P,end=' ')
            for i in kmpres[1:]:#il primo elemento e' il numero di confronti
                if P!=T[i:i+len(P)]:
                    print("\nErrore algoritmo KMP")
                    print("Pattern: ",P)
                    print("Testo  : ",T[i,i+len(P)])
                    print("Posiz. : ",i)
                    err=True
            if verbose and not err:
                print("--> nessun errore")
    
        print(f'{"Tempo Algoritmo KMP: ":35s}{totaltime:10.6f}')
        
        if verbose:
            print("Controllo BF e KMP hanno trovato lo stesso numero di match ",end='')
        err=False
        for i in range(len(bfnom)):
            if bfnom[i]!=kmpnom[i]:
                print("\nPattern: ",PP[i])
                print("KMP NoM: ",kmpnom[i])
                print("BF  NoM: ",bfnom[i])
                err=True
        if verbose and not err:
            print("--> nessun errore")
    
        rkres=[]
        startp=time.time()
        TT=prepareText(T,len(PP[0]))
        finishp=time.time()
        startl=time.time()
        for P in PP:
            rkres.append(lookup(TT,P))
        finishl=time.time()
        print(f'{"Algoritmo Rabin-Karp":35s}')
        print(f'{"   Preparazione testo":35s}{finishp-startp:10.6f}')
        print(f'{"   Operazioni di lookup":35s}{finishl-startl:10.6f}')
        print(f'{"Totale":35s}{finishl-startp:10.6f}')
    
        print()


if __name__=="__main__":
    driver()
    
