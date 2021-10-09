import random

def detIteSelect(A,k):
    l=0
    h=len(A)
    while(l<h):
        i=partition(A,l,h-1)
        if k<i:
            h=i
        if k==i:
            return A[k]
        if k>i:
            l=i+1
    return A[l]

def partition(L,l,h):
    i=l-1         # first element 
    pivot=L[h]    # pivot
  
    for j in range(l,h):
        if L[j]<=pivot:
            i=i+1
            L[i],L[j]=L[j],L[i]

    L[i+1],L[h]=L[h],L[i+1]

    return i+1

if __name__=='__main__':
    N=20
    A=list(range(N))
    for i in range(len(A)-1):
        idx=random.randrange(i,len(A))
        A[i],A[idx]=A[idx],A[i]

    B=[]
    for k in range(len(A)):
        C=A.copy()
        B.append(detIteSelect(C,k))
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

