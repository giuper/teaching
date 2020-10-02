from stack import Stack

class Maze:

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
    def __init__(self,nr,nc):
        self.nr=nr
        self.nc=nc
        self.s=Stack()
        self.m=[[0]*nc for x in range(nr)]


    def setBlock(self,r,c):
        self.m[r][c]=1

    def __str__(self):
        res="+"+"-"*(self.nc)+"+\n"
        for r in range(self.nr):
            res=res+"|"
            for c in range(self.nc):
                if self.m[r][c]==1:
                    res=res+"#"
                if self.m[r][c]==0:
                    res=res+"."
                if self.m[r][c]==-1:
                    res=res+"*"
            res=res+"|\n"
        res=res+"+"+"-"*(self.nc)+"+\n"
        return res


##    def printSol(self):
##
##    

    def setFinish(self,rf,cf):
        self.m[rf][cf]=-1

    def setVisited(self,r,c):
        self.m[r][c]=2
        

    def isAdmissible(self,newr,newc,verbose=False):
        if (newr<0) or (newr>=self.nr):
            return False
        if (newc<0) or (newx>=self.nc):
            return False
        if self.m[newr][newc]!=0:
            return False


    def nextAdmMove(self,r,c,lmove):
        if lmove==4:
            return None
        for mossa in range(lmove+1,5):
            newr=r+MOVES[mossa][0]
            newc=c+MOVES[mossa][1]
            if self.isAdmissible(newr,newc):
                return mossa
        return None

    def Solve(self,sr,sc,verbose=False):
        
        #(sr,sc) starting row and column
        #the stack contains [r,c,lmove]
        #r:       current row
        #c:       current column
        #lmove: last move tried while at (r,c)

        self.s.push([sr,sc,0])
        self.setVisited(sr,sc)
        
        while self.s:
            
            [r,c,lmove]=self.s.pop()
            nmove=self.nextAdmMove(r,c,lmove)
            if nmove is None:
                self.m[r][c]=3
                continue
            self.s.push([r,c,nmove])
            self.m[r][c]=2
            newr=r+MOVES[nmove][0]
            newc=c+MOVES[nmove][1]
            if self.m[newr][newc]=-1:
                return True
            self.s.push([newr,newc,0])

        return False

        
