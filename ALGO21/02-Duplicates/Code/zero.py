class DuplicatesS:
    desc="Precompute and store all answers"

    def __init__(self,A):
        self.N=len(A)
        self.A=A.copy()
    
        self.results=dict()

        for i in range(self.N):
            for j in range(i+1,self.N+1):
                d=dict()
                self.results[i+j*self.N]=None
                for k in range(i,j):
                    if A[k] in d:
                        self.results[i+j*self.N]=k
                        break
                    else:
                        d[A[k]]=1
                
    def __getitem__(self,key):
        [first,last]=key
        idx=self.results[first+self.N*last]
        if idx is None:
            return None
        else:
            return self.A[idx]
        
def driver():
    A=['a','b','a','a','c','d','b','a','b','c']
    X=Duplicates(A)
    Tests=[[3,6],[4,10]]
    
    print("Testing duplicates in intervals of")
    print(A)
    print()
    for test in Tests:
        [i,j]=test 
        res=X[i,j]
        ss="["+str(i)+","+str(j)+"):"
        if res is None:
            print(f'{ss:15s}{"no duplicate":s}')
        else:
            print(f'{ss:15s}{"   duplicate ":s}{res}')
            

if __name__=='__main__':
    driver()
