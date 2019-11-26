from stack import Stack

class myStack(Stack):
    def __str__(self):
        if len(self)==0:
            return " "
        else:
            [cr,cc,lmtried,lmtaken]=self.pop()
            return str(self)+"\n("+str(cr)+","+str(cc)+")"

class Maze:

    #does not handle cycles in the maze
    MOVES=[[0,0],[-1,0],[1,0],[0,-1],[0,1]]
    #moves
    #0 --> Dummy move
    #1 --> North
    #2 --> South
    #3 --> East
    #4 --> West

    OPPOSITE=[None,2,1,4,3]
    #move 0 has no opposite
    #move 2 (S) is the opposite of move 1 (N)
    #move 1 (N) is the opposite of move 2 (S)
    #move 3 (E) is the opposite of move 4 (W)
    #move 4 (W) is the opposite of move 3 (E)


    def __init__(self,nr,nc):
        self.nr=nr
        self.nc=nc
        self.m=[[0]*nc for i in range(nr)]
        self.s=myStack()


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


    def printSol(self):
        print(self.s)

    def setBlock(self,r,c):
        self.m[r][c]=1

    def setFinish(self,rf,cf):
        self.rf=rf
        self.cf=cf
        self.m[rf][cf]=-1


    def isAdmissible(self,row,col,verbose):
        if (row<0) or (row>=self.nr) or (col<0) or (col>=self.nc):
            if verbose:
                print("\tOut of bounds")
            return False
        if (self.m[row][col]==1):
            if verbose:
                print("\tinto a wall")
            return False
        return True


    def Solve(self,sr,sc,verbose=False):
        #the stack contains quadruples [r,c,lmtried,lmtaken]
        #r:       current row
        #c:       current column
        #lmtried: last move tried while at (cr,cc)
        #lmtaken: last move taken to reach at (cr,cc)

        #push the starting position on the stack
        #lmtried=0 --> no move has been tried yet
        self.s.push([sr,sc,0,0])

        while(len(self.s)>0):

            [cr,cc,lmtried,lmtaken]=self.s.pop()
        
            if verbose:
                print("\nCurrent position: ",cr,cc)
                print("\tSize of stack: ",len(self.s))

            if self.m[cr][cc]==-1:
                #we have finished
                self.s.push([cr,cc,0,0])
                return True

            for mv in range(lmtried+1,5):
                if verbose:
                    print("Trying move ",mv,"from (",cr,cc,")")
                if mv==Maze.OPPOSITE[lmtaken]:
                    if verbose:
                        print("\tOpposite move")
                    continue
                nr=cr+Maze.MOVES[mv][0] #the new row
                nc=cc+Maze.MOVES[mv][1] #the new col
                if self.isAdmissible(nr,nc,verbose):
                    if verbose:
                        print("\t going to ",nr,nc)
                    #push our last position 
                    self.s.push([cr,cc,mv,lmtaken])
                    cr=nr
                    cc=nc
                    #push our next position
                    self.s.push([cr,cc,0,mv])
                    break   #break the for mv loop

        return False

        


    def recursiveSolve(self,cr,cc,lm,verbose=False):
        if verbose:
            print("\t in ",cr,cc)
        if self.m[cr][cc]==-1:
            if verbose:
                print("\tWOW")
            return([True,[]])

        for mv in range(1,5):
            if verbose:
                print("Trying move ",mv,"from (",cr,cc,")")
            if mv==Maze.OPPOSITE[lm]:
                if verbose:
                    print("\tOpposite move")
                continue
            nr=cr+Maze.MOVES[mv][0] #the new row
            nc=cc+Maze.MOVES[mv][1] #the new col
            if self.isAdmissible(nr,nc,verbose):
                if verbose:
                    print("\t going to ",nr,nc)
                res=self.recursiveSolve(nr,nc,mv,verbose)
                if res[0]:
                    res[1].insert(0,[nr,nc])
                    return res

        return [False]

