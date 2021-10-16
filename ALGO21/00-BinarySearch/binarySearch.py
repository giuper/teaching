import time



##if x is in the list of elements
## it returns the index
##else
## it returns where it should be

##comp is not used here
def inP(L,x,comp=(lambda x:x)):
    return x in L

##Linear search
def LS(L,x,comp=(lambda x,y:x>y)):
    for i in range(len(L)):
        #if L[i]>=x:
        if L[i]==x or comp(L[i],x):
            return i
    return len(L)

##Binary Search Iterative Version
def BSIter(L,x,comp=(lambda x,y:x>=y)):
    l=0
    h=len(L)-1
    while l<=h:
        m=(h+l)//2
        if L[m]==x:
            return m
        #if x<L[m]:
        if comp(L[m],x):
            h=m-1
        else:
            l=m+1
    return l

##Binary Search Recursive Version
def BSRec(L,x,comp=(lambda x,y:x>=y)):
    return _BSRec(0,len(L)-1,L,x,comp)

def _BSRec(l,h,L,x,comp=(lambda x,y:x>=y)):
    if l>h:
        return l
    m=(h+l)//2
    if L[m]==x:
        return m
    #if x<L[m]:
    if comp(L[m],x):
        return _BSRec(l,m-1,L,x)
    else:
        return _BSRec(m+1,h,L,x)


def driverInt(sizes,algos):
    for size in sizes:
        L=list(range(0,size,2))
        for [name,func] in algos:
            start=time.time()
            x=func(L,0)
            y=func(L,1)
            z=func(L,size+1)
            finish=time.time()
            print(f'{name:18s}{"  Size:":7s}{(size//2):10d}{"  Average time:":20s}{(finish-start)/3:10.6f}')
                
        print()

def driverS(sizes,algos):
    for size in sizes:
        L=['a'*i for i in range(size)]
        for [name,func] in algos:
            start=time.time()
            x=func(L,L[0],(lambda x,y:len(x)>len(y)))
            y=func(L,L[-1],(lambda x,y:len(x)>len(y)))
            z=func(L,L[-1]+"aaaa",(lambda x,y:len(x)>len(y)))
            finish=time.time()
            print(f'{name:18s}{"  Size:":7s}{len(L):10d}{"  Average time:":20s}{(finish-start)/3:10.6f}')
        print()


if __name__=='__main__':
    sizes=[2**10,2**12,2**15,2**18,2**20,2**22,2**25,2**28]
    algos=[["Python in",inP],["Linear search",LS],["Bin Search Iter",BSIter],["Bin Search Rec",BSRec]]

    print("Testing on lists of integers")
    driverInt(sizes,algos)
    print()

    print("Testing on lists of strings ordered by length")
    driverS(sizes[:3],algos)
    

