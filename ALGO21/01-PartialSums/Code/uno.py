from zero import parSum

class parSumF(parSum):
    desc="Faster precomputation of all answers"
    def __init__(self,A):
        self.N=len(A)
        self.A=A.copy()
    
        self.PS=[]
        for r in range(self.N):
            self.PS.append([0]*(self.N+1))
        
        i=0
        for r in range(self.N):
            last=0
            for c in range(r+1,self.N+1):
                self.PS[r][c]=last+self.A[c-1]
                last=self.PS[r][c]
        

def driver():
    A=[1,2,3,4,5]
    X=parSum(A)
    print(X)
    
    for i in range(len(A)):
        X[i]=10*A[i] 
        print(X)


if __name__=='__main__':
    driver()
