class parSumNP:
    desc="No Precomputation"
    def __init__(self,A):
        self.A=A.copy()

    def __getitem__(self,key):
        [first,last]=key
        res=0
        for i in range(first,last):
            res=res+self.A[i]
        return res

    def __setitem__(self,idx,val):
        self.A[idx]=val
   

