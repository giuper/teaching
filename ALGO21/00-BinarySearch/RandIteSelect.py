import random

def randIteSelect(A,k):
    l=0
    h=len(A)
    while(l<h):
        idx=random.randrange(l,h)
        A[idx],A[h-1]=A[h-1],A[idx]
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
    A=list(range(10))
    for k in range(len(A)):
        print(k,randIteSelect(A,k))
        print()
