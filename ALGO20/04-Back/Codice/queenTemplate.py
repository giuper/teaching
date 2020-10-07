from back import BackTrack

class Queen(BackTrack):

#n is the size of the board
    def __init__(self,n):
        super().__init__()
        self.n=n
        self.sol=None

#for this problem a state consists of  (q,nr)
#q the list of position of the queens
#q[r] gives the column of the queen in the r-th row
#nr is the next row to be considered

#queens in rows 0,...,nr-1 are non-attacking

#in the initial state no queen has been placed yet
#q[r]=-1 for r=0,...,n-1
#nr=0

    def initState(self):
        return [[-1]*self.n,0]

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        pass

#required by BackTrack
    def makeMove(self,state,move):
        pass
            
#required by BackTrack
    def setVisited(self,initialState):
        pass 

#required by BackTrack
    def isFinal(self,state):
        pass

##check position of queen in row nr
##is compatible with those in rows 0,1,...,nr-1
##used by nextAdmMove
    def _checkQueen(self,q,nr):
        for i in range(nr):
            if q[i]==q[nr]:
                return False
            if q[i]-i==q[nr]-nr:
                return False
            if q[i]+i==q[nr]+nr:
                return False
        return True


    def __str__(self):
        res=""
        if self.sol is not None:
            for r in range(self.n):
                res=res+"."*self.sol[0][r]+"Q"+"."*(self.n-self.sol[0][r]-1)+"\n"
        return res

