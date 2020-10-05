from back import BackTrack

class Maze(BackTrack):

    #does not handle cycles in the maze
    MOVES=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    #moves
    #0 --> Dummy move
    #1 --> North
    #2 --> East
    #3 --> South
    #4 --> West



    ## EXIT/FINISH -1
    ## LIBERO       0
    ## BLOCCATO     1
    ## VISITATO     2
    ## ESAURITO     3

    #nr -- numero di righe
    #nc -- numero di colonne

    def __init__(self,nr,nc,rs,cs):
        super().__init__()
        self.nr=nr #number of rows
        self.nc=nc #number of columns
        self.rs=rs #starting row
        self.cs=cs #starting col
        #intialize grid with all free 
        self.m=[[0]*nc for x in range(nr)]
        self.sol=None

#required by BackTrack
#for this problem a state consists of 
#current row --> starting row at the start
#current col --> starting col at the start
#current grid -> the initial grid
    def initState(self):
        mm=[]
        for x in self.m:
            mm.append(x.copy())
        return [self.rs,self.cs,mm]

#required by BackTrack
    def nextAdmMove(self,state,lmove):
        [r,c,m]=state
        if lmove is None:
            lmove=0
        for mossa in range(lmove+1,5):
            newr=r+self.MOVES[mossa][0]
            newc=c+self.MOVES[mossa][1]
            if self._isAdmissible(m,newr,newc):
                return mossa
        return None

#required by BackTrack
    def makeMove(self,state,move):
        [r,c,m]=state
        newr=r+self.MOVES[move][0]
        newc=c+self.MOVES[move][1]
        return [newr,newc,m]

#required by BackTrack
    def setVisited(self,state):
        [r,c,m]=state
        m[r][c]=2

#required by BackTrack
    def isFinal(self,state):
        [r,c,m]=state
        return m[r][c]==-1

#used by nextAdmMove 
    def _isAdmissible(self,m,newr,newc,verbose=False):
        if (newr<0) or (newr>=self.nr):
            return False
        if (newc<0) or (newc>=self.nc):
            return False
        if m[newr][newc]>0:
            return False
        return True


#used by application
    def setFinish(self,rf,cf):
        self.m[rf][cf]=-1

    def setBlock(self,r,c):
        self.m[r][c]=1

    def __str__(self):
#if there is no solution yet
#print the instance
#otherwise print the soloution
        if self.sol is None:
            return(self.stampa(self.m))
        else:
#reminder:
#a state consists of current row, current col, grid
#the actual solution is thus found at index 2
            return(self.stampa(self.sol[2]))

    def stampa(self,mm):
        if(self.nc<10):
            res="  "
            for r in range(self.nc):
                res=res+str(r)
            res=res+"\n"
        else:
            res=""
        res=res+" +"+"-"*(self.nc)+"+\n"
        for r in range(self.nr):
            res=res+str(r)+"|"
            for c in range(self.nc):
                if mm[r][c]==1:
                    res=res+"#"
                if mm[r][c]==0:
                    res=res+"."
                if mm[r][c]==-1:
                    res=res+"*"
                if mm[r][c]==2:
                    res=res+"*"
            res=res+"|\n"
        res=res+" +"+"-"*(self.nc)+"+\n"
        return res
