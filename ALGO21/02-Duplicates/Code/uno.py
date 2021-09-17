class Duplicates:
    desc="Report duplicates in [i,j)"

    def __init__(self,A):
        self.A=A.copy()
        d=dict()
        
        max_val=-1
        self.P=[-1]
        self.Q=[-1]
        d[A[0]]=0
        for i in range(1,len(A)):
            if A[i] in d:
                self.P.append(d[A[i]])
                if d[A[i]]>max_val:
                    max_val=d[A[i]]
            else:
                self.P.append(-1)
            d[A[i]]=i
            self.Q.append(max_val)
            
    def __getitem__(self,idx):
        [i,j]=idx
        if self.Q[j-1]<i:
            return None
        else:
            return self.A[self.Q[j-1]]
    
            
                
def driver():
    A=['a','b','a','a','c','d','b','a','b','c']
    X=Duplicates(A)
    print(X.P)
    print(X.Q)
    print(3,6,X[3,6])
    print(4,10,X[4,10])
    
if __name__=='__main__':
    driver()
