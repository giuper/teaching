class soldp:

    def __init__(self,n,L):
        self.n=n
        self.L=L
        self.stato=[-1]*n


    def __str__(self):
        res=""
        for r in range(self.n):
            c=self.stato[r]
            res=res+"*"*c+"Q"+"*"*(self.n-1-c)+"\n"
        return res
    
#verifica se  (r,c) e' una posizione proibita
#e se una regina a (r,c)
#è attaccata da una delle regine già posizionate
#alle righe 0,1,...,r-1
    def controlla(self,r,c):
        for q in range(r):  #per ogni regina q già posizionata
            if self.stato[q]==c:
                return False  #la regina alla riga q è alla stessa colonna
            if q-self.stato[q]==r-c:
                return False  #la regina alla riga q è sulla stessa d. princ.
            if q+self.stato[q]==r+c:
                return False  #la regina alla riga q è sulla stessa d. secon.

        return True #non è attaccata da nessuna delle regine precedenti

    def solve(self):
        return self.psolve(0)

#in precedenza abbiamo piazzato una regina in ciascuna
#delle righe 0,...,r-1
#se r=n abbiamo finito! WOW
#altrimenti tentiamo di posizionare una regina in riga r
    def psolve(self,r):
        if r==self.n:
            return True
        
        if self.L[r]!=-1:
            ListaPossibili=[self.L[r]]
        else:
            ListaPossibili=range(self.n)

        for c in ListaPossibili:
            if self.controlla(r,c): #se non è sotto attacco
                self.stato[r]=c     #piazza una regina alla riga r, colonna c
                res=self.psolve(r+1) #chiama ricorsivamene su r+1 
                if res:             #se abbiamo trovato una soluzione
                    return True
        return False                #se abbiamo provato tutte le colonne senza successo


