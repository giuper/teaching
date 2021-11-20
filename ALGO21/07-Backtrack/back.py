class BackTrack:

#la classe derivata deve implementare
# allMoves(stato)   -- restituisce la lista di mosse nello stato 
# isAdm(stato,m)    -- True sse mossa m e' ammissibile in stato
# newStato(stato,m) -- restituisce lo stato che si ottiene applicando m
# isFinal(stato)    -- Ture sse lo stato e' finale


##restituisce una lista
##all'indice 0 True/False
##se l'indice 0 e' uguale a True, l'indice 1 contiene uno stato finale
    def _Solve(self,stato,verbose=False):

        if verbose:
            print("Stato:",stato)
        if self.isFinal(stato):
            return [True,stato]
        for m in self.allMoves(stato):
            if not self.isAdm(stato,m):
                if verbose:
                    print("mossa ",m,"non ammissibile in",stato)
                continue
            if verbose:
                print("mossa ",m,"ammissibile in",stato)
            newStato=self.newStato(stato,m)
            risultato=self._Solve(newStato,verbose)
            if risultato[0]:
                return risultato
        return [False]


