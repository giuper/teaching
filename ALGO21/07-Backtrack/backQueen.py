from back import BackTrack

##lo stato per questo problema consiste di una lista di due elementi
##all'indice 0 abbiamo l'indice R della prossima regina da considerare
##all'indice 1 abbiamo la lista regine che contiene le posizioni 
##delle regine gia' piazzate

##stato iniziale 
##0  -->   R=0        prossima regina da considerare
##1  -->  regine=[None]*N  nessuna posizione decisa

class Queen(BackTrack):

    def __init__(self,N):
        super().__init__() #chiama il costruttore della classe madre
        self.N=N

    def Solve(self,verbose=False):
        #R=0
        #regine=[None]*N
        return self._Solve([0,[None]*self.N],verbose)

    def allMoves(self,stato):
        return range(self.N)

    def isAdm(self,stato,m):
        R=stato[0]
        return self._checkQueen(stato[1],R,m)

    def newStato(self,stato,m):
        R=stato[0]
        newStato=[R+1]
        newStato.append(stato[1].copy())
        newStato[1][R]=m
        return newStato
    
    def isFinal(self,stato):
        return stato[0]==self.N

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



for N in range(3,11):
    q=Queen(N)
    soluzione=q.Solve()
    if soluzione[0]:
        print(f'Soluzione per N={q.N}: {soluzione[1][0]}')
    else:
        print(f'Nessuna soluzione per N={q.N}')

print("\n\nIl caso N=4 in modalità verbose")
q=Queen(4)
soluzione=q.Solve(True)
