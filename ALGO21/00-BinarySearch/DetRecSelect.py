import random

def detRecSelect(A,k):
    pivot=A[0] 
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
        return detRecSelect(L,k)
    else:
        return detRecSelect(R,k-l-1)

if __name__=='__main__':
    N=20
    A=list(range(N))
    for i in range(len(A)-1):
        idx=random.randrange(i,len(A))
        A[i],A[idx]=A[idx],A[i]

    B=[]
    for k in range(len(A)):
        C=A.copy()
        B.append(detRecSelect(C,k))
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

