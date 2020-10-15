from subsetSum0 import SubsetSum0

class SubsetSum1(SubsetSum0):

#required by BackTrack
#state[0] next index to be considered
#state[1] set S
#state[2] somma degli elementi in S
    def initState(self):
        return [0,[None for j in range(self.N)],0]

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        i=state[0]
        s=state[2]
        if i==self.N:
            return None

        if lmove==None:
            return 0

        if lmove==0:
            if s+self.L[i]>self.t:
                return None
            else:
                return 1

        if lmove==1:
            return None

#required by BackTrack
# input:  current state
#         move
# output: new state obtained by making move 
    def makeMove(self,state,move):
        i=state[0]
        S=state[1]
        s=state[2]
        S[i]=move
        
        if move==1:
            s=s+self.L[i]
        return [i+1,S,s]

#required by BackTrack
    def isFinal(self,state):
        return state[2]==self.t

