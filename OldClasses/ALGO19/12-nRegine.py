class nRegine:

    def __init__(self,n):
        self.n=n
        self.stato=[-1]*n


    #def __str__(self):
        #res=""
        #for r in range(self.n):
            #res=res+", ("+str(r)+","+str(self.stato[r])+")"
        #return res
#
    def __str__(self):
        res=""
        for r in range(self.n):
            c=self.stato[r]
            res=res+"*"*c+"Q"+"*"*(self.n-1-c)+"\n"
        return res
    
#verifica se una regina a (r,c)
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

#in precedenza abbiamo piazzato una regina in ciascuna
#delle righe 0,...,r-1
#se r=n abbiamo finito! WOW
#altrimenti tentiamo di posizionare una regina in riga r
    def solve(self,r):
        if r==self.n:
            return True
        for c in range(self.n): #controlla tutte le possibili colonne
            if self.controlla(r,c): #se non è sotto attacco
                self.stato[r]=c     #piazza una regina alla riga r, colonna c
                res=self.solve(r+1) #chiama ricorsivamene su r+1 
                if res:             #se abbiamo trovato una soluzione
                    return True
        return False                #se abbiamo provato tutte le colonne senza successo


for i in range(3,21):
    q=nRegine(i)
    if q.solve(0):
        print(i)
        print(q)
        print()
    else:
        print(i,": nessuna sol.")
        print()



            
