from back import BackTrack

class SubsetSum0(BackTrack):

    def __init__(self,L,t):
        super().__init__()
        self.L=L
        self.t=t
        self.N=len(L)
        self.sol=None

#required by BackTrack
    def initState(self):
        return [0,[None]*self.N]
        

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        [i,S]=state

        if i==self.N:
            return None
        
        if lmove==None:
            nmove=0
            
        if lmove==0:
            nmove=1

        if lmove==1:
            nmove=None

        return nmove
        

#required by BackTrack
# input:  current state
#         move
# output: new state obtained by making move 
    def makeMove(self,state,move):
        [i,S]=state
        S[i]=move
        i=i+1
        return [i,S]
        

#required by BackTrack
    def setVisited(self,state):
        pass

#required by BackTrack
    def isFinal0(self,state):
        [i,S]=state

        if i<self.N:
            return False

        sm=0
        for j in range(self.N):
            if S[j]==1:
                sm=sm+self.L[j]

        return sm==self.t



#required by BackTrack
#suggerito durante la lezione
#bisogna azzerare i valore delle mosse vecchie

    def isFinal(self,state):
        [i,S]=state
        sm=0
        for j in range(i):
            if S[j]==1:
                sm=sm+self.L[j]

        if sm==self.t: #siamo in uno stato finale
            for j in range(i,self.N):
                S[j]=0  #azzeriamo tutti le rimanenti mosse
            return True
        else:
            return False


    def __str__(self):
        for i in range(self.N):
            if self.sol[1][i] is None or i>=self.sol[0]:
                self.sol[1][i]=0

        return "Input:     "+str(self.L)+"\n"+"Soluzione: "+str(self.sol[1])+"\n"
