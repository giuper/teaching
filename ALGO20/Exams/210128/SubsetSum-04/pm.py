from subsetSum0 import SubsetSum0

class PM(SubsetSum0):

    def isFinal(self,state):
        [i,S]=state

        if i<self.N:
            return False

        sm=0
        for j in range(self.N):
            sm=sm+S[j]*self.L[j]

        return sm==self.t
    
    def nextAdmMove(self,state,lmove):
        [i,S]=state

        if i==self.N:
            return None
        
        if lmove==None:
            nmove=0
            
        if lmove==0:
            nmove=1

        if lmove==1:
            nmove=-1

        if lmove==-1:
            nmove=None

        return nmove
