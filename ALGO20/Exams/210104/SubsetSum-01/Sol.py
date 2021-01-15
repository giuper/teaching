from subsetSum0 import SubsetSum0


class Sol(SubsetSum0):

    def nextAdmMove(self,state,lmove):
        [i,S]=state

        if i==self.N:
            return None
        
        if lmove==None:
            nmove=0
            
        if lmove==0:
            if S[i-1]==0:
                nmove=1
            if S[i-1]==1:
                if S[i-1]>S[i]:
                    nmove=None
                else:
                    nmove=1

        if lmove==1:
            nmove=None

        return nmove
    

