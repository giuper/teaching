def select(A,n,i):

    if n==1:
        return A[0]

    x=findX(A,n)
    L=[]
    R=[]
    
    for z in A:
        if z<x:
            L.append(z)
        else:
            R.append(z)

    l=len(L)
    if i<=l:
        return select(L,l,i)
    else:
        return select(R,n-l,i-l)


def findX(A,n):
    found=0
    r=0
    while(found==0):
        x=A[r]
        L=[]
        R=[]
    
        for z in A:
            if z<x:
                L.append(z)
            else:
                R.append(z)
        l=len(L)
        if l>=n/4 and l<=.75*n:
            return x
        else:
            r=r+1
            
