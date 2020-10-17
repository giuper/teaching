from subsetSum0 import SubsetSum0

class SubsetSum4(SubsetSum0):

#required by BackTrack
#state[0] i next index to be considered
#state[1] set S
#state[2] somma degli elementi in S
#state[3] somma degli element L[i+1]...L[N-1]

    def initState(self):
        return [0,[None for j in range(self.N)],0,sum(self.L)]

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        i=state[0]
        s=state[2]
        r=state[3]
        if i==self.N:
            return None

        lb=s+self.L[i]  #every sum that includes element L[i]
                        #will be at least lb
    
        ub=s+r-self.L[i] #every sum that does not include L[i]
                         #will be at most ub

        if lmove==None:
            if ub>=self.t:
                return 0
            else:
                lmove=0

        if lmove==0:
            if lb<=self.t:
                return 1

        return None

#required by BackTrack
# input:  current state
#         move
# output: new state obtained by making move 
    def makeMove(self,state,move):
        i=state[0]
        S=state[1]
        s=state[2]
        r=state[3]
        S[i]=move
        
        if move==1:
            s=s+self.L[i]
        return [i+1,S,s,r-self.L[i]]

#required by BackTrack
    def isFinal(self,state):
        return state[2]==self.t

