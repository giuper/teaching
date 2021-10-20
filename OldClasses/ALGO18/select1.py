import random

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
    nt=0
    while(found==0):
        r=random.randint(0,n-1)
        nt=nt+1
        x=A[r]
        #print "Trying",x        
        L=[]
        R=[]
    
        for z in A:
            if z<x:
                L.append(z)
            else:
                R.append(z)
        l=len(L)
        #print "l=",l
        #print "n=",n
        #print "n/4=",n/4
        #print "3/4n=",.75*n
        if l>=n/4 and l<=0.75*n:
            #print "Numero tentativi: ",nt
            return x
        else:
            r=r+1
            
