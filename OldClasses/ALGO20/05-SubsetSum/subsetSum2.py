from subsetSum1 import SubsetSum1

class SubsetSum2(SubsetSum1):

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        i=state[0]
        S=state[1]
        s=state[2]
        if i==self.N:
            return None

        if lmove==None:
            rr=0
            for j in range(i+1,self.N):
                rr=rr+self.L[j]
            if rr+s<self.t:
                return 1
            else:
                return 0

        if lmove==0:
            if s+self.L[i]>self.t:
                return None
            else:
                return 1

        if lmove==1:
            return None

