from subsetSum0 import SubsetSum0

class Multi(SubsetSum0):

    def __init__(self,L,M,t):

        nL=[]
        for i in range(len(L)):
            nL=nL+[L[i]]*M[i]
        super().__init__(nL,t)
            
