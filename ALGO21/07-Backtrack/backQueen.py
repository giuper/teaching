from back import BackTrack

##lo stato per questo problema consiste di una lista di due elementi
##all'indice 0 abbiamo una lista che contiene le posizioni delle regine
##gia' decise
##all'indice 1 abbiamo l'indice della prossima regina da considerare
##stato iniziale 
##0  -->  [None]*n  nessuna posizione decisa
##1  -->   0        prossima regina da considerare
##                  e' la regina in riga 0

class Queen(BackTrack):

    def __init__(self,n):
        super().__init__()
        self.n=n
        self.sol=None

    def Solve(self,verbose=False):
        return self._Solve([[None]*self.n,0],verbose)

    def allMoves(self,stato):
        return list(range(self.n))

    def isAdm(self,stato,m):
        R=stato[1]
        return self._checkQueen(stato[0],R,m)

    def newStato(self,stato,m):
        newStato=[]
        newStato.append(stato[0].copy())
        R=stato[1]
        newStato[0][R]=m
        newStato.append(R+1)
        return newStato
    
    def isFinal(self,stato):
        return stato[1]==self.n

    def _checkQueen(self,q,nr,m):
        r1=nr
        c1=m
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


q=Queen(8)
soluzione=q.Solve()
if soluzione[0]:
    print(f'Soluzione per N={q.n}: {soluzione[1][0]}')
else:
    print("Nessuna soluzione")
