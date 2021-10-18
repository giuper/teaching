class parSum:
    desc="Precompute all answers and store results"
    def __init__(self,A):
        self.N=len(A)
        self.A=A.copy()
    
        self.PS=[]
        for r in range(self.N+1):
            self.PS.append([0]*(self.N+1))
        
        for i in range(self.N):
            for j in range(i+1,self.N+1):
                for c in range(i,j):
                    self.PS[i][j]+=self.A[c]
        
    def __getitem__(self,key):
        [first,last]=key
        return self.PS[first][last]
        
    def __setitem__(self,idx,val):
        oldval=self.A[idx]
        for i in range(idx+1):
            for j in range(idx+1,self.N+1):
                self.PS[i][j]=self.PS[i][j]-oldval+val
   

    def __str__(self):
        res=""
        for r in range(len(self.PS)):
            res+='{:5d}'.format(r)+"\t"
            for c in range(1,len(self.PS[r])):
                res+='{:5d}'.format(self.PS[r][c])
            res+="\n"
        return res
    
def driver():
    A=[1,2,3,4,5]
    X=parSum(A)
    print(X)
    
    for i in range(len(A)):
        X[i]=10*A[i] 
        print(X)


if __name__=='__main__':
    driver()
