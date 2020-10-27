from subsetSum4 import SubsetSum4

class SubsetSum5(SubsetSum4):

#state[0] i next index to be considered
#state[1] set S
#state[2] somma degli elementi in S
#state[3] somma degli element L[i+1]...L[N-1]

    def nextAdmMove(self,state,lmove):
        #compute the next move according to standard SubSetSum
        nextmove=super().nextAdmMove(state,lmove)
        i=state[0]
        S=state[1]
        if i>0 and S[i-1]==1 and nextmove==1:
            return None 
        else: 
            return nextmove

