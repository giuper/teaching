import time



##if x is in the list of elements
## it returns the index
##else
## it returns where it should be

def LS(L,x):
    for i in range(len(L)):
        if L[i]>=x:
            return i
    return len(L)

def BSIter(L,x):
    l=0
    h=len(L)-1
    while l<=h:
        m=(h+l)//2
        if L[m]==x:
            return m
        if x<L[m]:
            h=m-1
        else:
            l=m+1

    return l

def BSRec(L,x):
    return _BSRec(L,0,len(L)-1,x)

def _BSRec(L,l,h,x):
    if l>h:
        return l
    m=(h+l)//2
    if L[m]==x:
        return m
    if x<L[m]:
        return _BSRec(L,l,m-1,x)
    else:
        return _BSRec(L,m+1,h,x)

SIZES=[2**10,2**12,2**15,2**18,2**20,2**22,2**25,2**28]
TESTS=[["Linear search",LS],["Bin Search Iter",BSIter],["Bin Search Rec",BSRec]]

def driver():
    for size in  SIZES:
        L=list(range(0,size,2))
        for [name,func] in TESTS:
            start=time.time()
            x=func(L,0)
            y=func(L,1)
            z=func(L,size+1)
            finish=time.time()
            print(f'{name:18s}{"  Size:":6s}{(size//2):10d}{"  Average time:":20s}{(finish-start)/3:10.6f}')
                
        print()


if __name__=='__main__':
    driver()
