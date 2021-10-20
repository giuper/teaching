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
#q[r]=None for r=0,...,n-1
#nr=0

    def initState(self):
        return [[None]*self.n,0]

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        [q,nr]=state
        if lmove==self.n-1:
            return None
        if lmove==None:
            lmove=-1
        for c in range(lmove+1,self.n):
            q[nr]=c
            if self._checkQueen(q,nr):
                return c
        return None

#required by BackTrack
    def makeMove(self,state,move):
        [q,nr]=state
        q[nr]=move
        return[q,nr+1]
            
#required by BackTrack
    def setVisited(self,initialState):
        pass 

#required by BackTrack
    def isFinal(self,state):
        [q,nr]=state
        return nr==self.n

##check position of queen in row nr
##is compatible with those in rows 0,1,...,nr-1
##used by nextAdmMove
    def _checkQueen(self,q,nr):
        r1=nr
        c1=q[nr]
        for i in range(nr):
            r2=i
            c2=q[i]
            if self._attackingQ(r1,c1,r2,c2):
                return False
        return True
   
    ##check if queen in (r1,c1) attacks queen in (r2,c2)
    def _attackingQ(self,r1,c1,r2,c2):
        return self._samecolumn(r1,c1,r2,c2) or self._sameMajorD(r1,c1,r2,c2) or self._sameMinorD(r1,c1,r2,c2)

    def _samecolumn(self,r1,c1,r2,c2):
        return c1==c2

    def _sameMajorD(self,r1,c1,r2,c2):
        return r1-c1==r2-c2

    def _sameMinorD(self,r1,c1,r2,c2):
        return r1+c1==r2+c2


    def __str__(self):
        res=""
        if self.sol is not None:
            for r in range(self.n):
                res=res+"."*self.sol[0][r]+"Q"+"."*(self.n-self.sol[0][r]-1)+"\n"
        return res

