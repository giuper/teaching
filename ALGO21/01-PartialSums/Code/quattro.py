import sys
import time

class parSumT:
    desc="Binary tree"
    def __init2__(self,B):
        self.N=len(B)
        self.A=B.copy()
        self.A.reverse()
        start=0
        end=self.N
        while start<end-1:
            for i in range(start,end,2):
                self.A.append(self.A[i]+self.A[i+1])
            l=(end-start)//2
            start=end
            end=end+l
        self.A.reverse()

    def __init__(self,B): #inefficient
        self.N=len(B)
        self.A=B.copy()
        start=len(B)-1
        while start>0:
            end=0
            while start>end:
                t=self.A[start]+self.A[start-1]
                start=start-2  #consumo due elementi
                self.A.insert(0,t)
                start=start+1
                end=end+1 #annullo l'effetto della insert su start e end
                
    def __setitem__(self,idx,val):
        i=idx+self.N-1 #idx indice in lista originale
                       #i indice nella rappresentazione
        diff=val-self.A[i] ##diff=nuovo valore - vecchio valore
        while(i>=0):
            ##print(f'{"Posizione:":10s}{i:3d}{"  "}{self.A[i]:3d}{"--->"}{self.A[i]+diff:3d}')
            self.A[i]+=diff
            i=(i-1)//2
    
    def theVector(self):
        return self.A[self.N-1:]
   
    def _lookup(self,x,i,j,s,t):  #want answer to [i,j) 
                                  #[i,j) included in [s,t) 
                                  #x index of the element with answer to [s,t)
        if i==j:       #sum of the empty interval
            return 0

        if i==s and j==t:         #[i,j)=[s,t) answer found at index x
            ##print(x,i,j,s,t,"finisce")
            return self.A[x] 

        m=(t+s)//2
        if j<m:
            ##print(x,i,j,s,t,"diventa",2*x+1,i,j,s,m)
            return self._lookup(2*x+1,i,j,s,m)
        if i>m:
            ##print(x,i,j,s,t,"diventa",2*x+2,i,j,m,t)
            return self._lookup(2*x+2,i,j,m,t)
        ##print(x,i,j,s,t,"diventa",2*x+1,i,m,s,m,"+",2*x+2,m,j,m,t)
        return self._lookup(2*x+1,i,m,s,m)+self._lookup(2*x+2,m,j,m,t)
        
    
    def __getitem__(self,key):
        [i,j]=key
        return self._lookup(0,i,j,0,self.N)
    

if __name__=='__main__':
    SIZE=2**20
    B=list(range(SIZE))
    start=time.time()
    A=parSumT(B)
    print(f'{time.time()-start:3.10f}')
    print("Oggetto costruito")

    start=time.time()
    x=A[2,10] ##invoca getitem che implementa lookup/query
    print(f'{time.time()-start:3.10f}')
    print("lookup(2,10):",x)

    if len(B)<100:
        print("prima della modifica: ",B)
    print("modifica elemento di indice 4")
    start=time.time()
    A[4]=28  ##invoca setitem che implementa set
    print(f'{time.time()-start:3.10f}')
    if len(B)<100:
        print("dopo la modifica: ",B)
    x=A[2,10] ##invoca getitem che implementa lookup/query
    print("lookup(2,10):",x)


