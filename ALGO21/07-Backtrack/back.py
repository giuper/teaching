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

    def _Solve(self,stato,verbose=False):

        if self.isFinal(stato):
            return [True,stato]
        for m in self.admMoves(stato):
            if not self.isAdm(stato,m):
                continue
            newStato=self.newStato(stato,m)
            risultato=self._Solve(newStato,verbose)
            if risultato[0]:
                return risultato
        return [False]


