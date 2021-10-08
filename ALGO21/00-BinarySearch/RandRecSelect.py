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
