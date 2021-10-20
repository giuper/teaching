fibDict={}

def initFib(k):
    global fibDict
    fibDict={}
    for i in range(1,k+1):
        fibDict[i]=1

def fibMem(n,k):
    global fibDict
    
    if n in fibDict:
        return fibDict[n]
    res=0
    for i in range(1,k+1):
        res+=fibMem(n-i,k)
    fibDict[n]=res
    return res

def contaDisp(maxN,k):
    count=0
    initFib(k)
    for n in range(1,maxN+1):
        x=fibMem(n,k)
        count=count+x%2
    return count/maxN

