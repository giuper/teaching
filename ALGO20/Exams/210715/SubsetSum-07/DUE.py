from subsetSum0 import SubsetSum0

class DUE:

    def __init__(self,LP,LM,t):
        self.LP=LP
        self.LM=LM
        self.t=t
    
    def Solve(self):
        AP=SubsetSum0(self.LP,self.t)
        if AP.Solve():
            return True

        maxc=sum(self.LP)
        for x in range(self.t+1,maxc+1):
            AP=SubsetSum0(self.LP,x)
            AM=SubsetSum0(self.LM,x-self.t)
            if AP.Solve() and AM.Solve():
                return True

        return False
