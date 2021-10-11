import random
from Partition import partition

def randIteSelect(A,k):
    l=0
    h=len(A)
    while(l<h):
        idx=random.randrange(l,h)
        A[idx],A[h-1]=A[h-1],A[idx]
        i=partition(A,l,h)
        if k<i:
            h=i
        if k==i:
            return A[k]
        if k>i:
            l=i+1
    return A[l]

if __name__=='__main__':
    N=2000
    A=list(range(N))
    for i in range(len(A)-1):
        idx=random.randrange(i,len(A)-1)
        A[i],A[idx]=A[idx],A[i]

    B=[]
    for k in range(len(A)):
        C=A.copy()
        B.append(randIteSelect(C,k))
    if N<=20:
        print("Lista input: ",A)
        print("Lista output:",B)

    #B dovrebbe essere [0,1,...,N-1]
    correct=True
    for i in range(len(B)):
        if i!=B[i]:
            correct=False
    if correct:
        print("Esecuzione corretta su lista di lunghezza",N)
    else:
        print("Errore su lista di lunghezza",N)
