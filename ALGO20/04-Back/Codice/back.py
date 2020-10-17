from stack import Stack

class BackTrack:

#derived class must provide
# initState   -- to get the initial state
# nextAdmMove -- to compute the next admissible move
# makeMove    -- to compute the new state resulting from making a move
# setVisited  -- to mark a state as visited
# isFinal     -- to decide if a state is final

#the stack contains pairs
#state -- as defined by the derived class
#lmove -- last move performed

    def __init__(self):
        self.s=Stack()

    def Solve(self,verbose=False):
        initialState=self.initState()
        self.s.push([initialState,None]) # no move has been taken
        self.setVisited(initialState)    # responsability of the lower class
        
        while self.s:
            [state,lmove]=self.s.pop()
            nmove=self.nextAdmMove(state,lmove)
            if nmove is not None:
                self.s.push([state,nmove])
                self.setVisited(state)
                newState=self.makeMove(state,nmove)
                if self.isFinal(newState):
                    self.sol=newState  #the new state is the solution
                    return True
                self.s.push([newState,None])
        return False

