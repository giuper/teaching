from subsetSum0 import SubsetSum0

class PM(SubsetSum0):

    def isFinal(self,state):
        [i,S]=state

        if i<self.N:
            return False

        sm=0
        for j in range(self.N):
            if S[j]==1:
                sm=sm+self.L[j]
            else:
                sm=sm-self.L[j]

        return sm==self.t
    
    def __str__(self):
        for i in range(self.N):
            if self.sol[1][i]==0:
                self.sol[1][i]=-1

        return "Input:     "+str(self.L)+"\n"+"Soluzione: "+str(self.sol[1])+"\n"

