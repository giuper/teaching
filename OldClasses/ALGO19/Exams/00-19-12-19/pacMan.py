from NRegine import nRegine

class nReginePacMan(nRegine):
    def controlla(self,r,c):
        for q in range(r):  #per ogni regina q già posizionata
            if self.stato[q]==c:
                return False  #la regina alla riga q è alla stessa colonna
            if (q-self.stato[q])%self.n==(r-c)%self.n:
                return False  #la regina alla riga q è sulla stessa d. princ.
            if (q+self.stato[q])%self.n==(r+c)%self.n:
                return False  #la regina alla riga q è sulla stessa d. secon.

        return True #non è attaccata da nessuna delle regine precedenti

