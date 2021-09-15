class parSumPre():
    desc="Precompute prefixes"
    def __init__(self,A):
        self.A=A.copy()
        self.N=len(A)
        self.Prefixes=[0]   
        tmp=0
        for k in range(1,self.N+1): #Prefixes[k]=A[0]+A[1]+...+A[k-1]
            tmp+=A[k-1] 
            self.Prefixes.append(tmp)
        
    def __getitem__(self,key):
        [first,last]=key
        return self.Prefixes[last]-self.Prefixes[first]

    def __setitem__(self,idx,val):
        delta=val-self.A[idx]
        self.A[idx]=val
        for i in range(idx+1,self.N+1):
            self.Prefixes[i]+=delta

    

def driver():
    A=[100,1,2,3,4,5]
    X=parSumPre(A)
    
    print("Input vector:",X.A)
    for i in range(2,7):
        print("Lookup(2,",i,")=",X[2,i])

    print()
    print("Setting A[3]=300")
    X[3]=300
    print("Input vector:",X.A)
    for i in range(2,7):
        print("Lookup(2,",i,")=",X[2,i])

if __name__=='__main__':
    driver()
