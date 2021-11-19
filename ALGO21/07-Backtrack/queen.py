
##controlla se la posizione della regina nella riga R
##e' compatibile con le regine nelle righe 0,1,...,R-1
def checkQueen(posizioni,R):
    r1=R
    c1=posizioni[R]
    for r in range(R):
        r2=r
        c2=posizioni[r]
        if attackingQ(r1,c1,r2,c2):
            return False
    return True

def attackingQ(r1,c1,r2,c2):
    return samecolumn(r1,c1,r2,c2) or sameMajorD(r1,c1,r2,c2) \
            or sameMinorD(r1,c1,r2,c2)

def samecolumn(r1,c1,r2,c2):
    return c1==c2

def sameMajorD(r1,c1,r2,c2):
    return r1-c1==r2-c2

def sameMinorD(r1,c1,r2,c2):
    return r1+c1==r2+c2

def solve(R,regine,N):
    if R==N:
        return True
    for C in range(N):
        regine[R]=C
        if checkQueen(regine,R):
            if solve(R+1,regine,N):
                return True
    return False
        
            
soluzione=[None]*8
if solve(R=0,regine=soluzione,N=8):
    print(soluzione)

