import random

def randRecSelect(A,k):
    pivot=random.choice(A)
    L=[]
    R=[]
    
    for a in A:
        if a<pivot:
            L.append(a)
        if a>pivot:
            R.append(a)
            
    l=len(L)
    if l==k:
        return pivot
    if l>k:
        return randRecSelect(L,k)
    else:
        return randRecSelect(R,k-l-1)

if __name__=='__main__':
    N=20000
    A=list(range(N))
    for i in range(len(A)-1):
        idx=random.randrange(i,len(A))
        A[i],A[idx]=A[idx],A[i]

    B=[]
    for k in range(len(A)):
        C=A.copy()
        B.append(randRecSelect(C,k))
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

