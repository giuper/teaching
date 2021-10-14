class parSumT:
    desc="Binary tree"
    def __init__(self,B):
        self.A=B.copy()
        self.A.reverse()
        self.N=len(B)
        start=0
        end=self.N
        while start<end-1:
            for i in range(start,end,2):
                self.A.append(self.A[i]+self.A[i+1])
            l=(end-start)//2
            start=end
            end=end+l
        self.A.reverse()

    def __setitem__(self,idx,val):
        i=idx+self.N-1 #idx indice in lista originale
                       #i indice nella rappresentazione
        diff=val-self.A[i] ##diff=nuovo valore - vecchio valore
        while(i>=0):
            print(f'{"Posizione:":10s}{i:3d}{"  "}{self.A[i]:3d}{"--->"}{self.A[i]+diff:3d}')
            self.A[i]+=diff
            i=(i-1)//2
    
    def theVector(self):
        return self.A[self.N-1:]
   
    def _lookup(self,x,i,j,s,t):  #[i,j) included in [s,t) 
        if i==j: 
            return 0
        if i==s and j==t:         #[s,t) is the subtree of x
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
    B=[12, 9, 4, 7, 21, 4, 9, 15, 3, 8, 3, 18, 9, 4, 8, 5]
    A=parSumT(B)

    x=A[2,10] ##invoca getitem che implementa lookup/query
    print("lookup(2,10):",x)

    print("prima della modifica: ",B)
    print("modifica elemento di indice 4")
    A[4]=28  ##invoca setitem che implementa set
    print("dopo la modifica: ",B)
    x=A[2,10] ##invoca getitem che implementa lookup/query
    print("lookup(2,10):",x)





