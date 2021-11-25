
##controlla se la colonna C e' una posizione della regina della riga R
##compatibile con le regine nelle righe 0,1,...,R-1
def checkQueen(R,regine,C):
    r1=R
    c1=C
    for r in range(R):
        r2=r
        c2=regine[r]
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
        if checkQueen(R,regine,C):
            regine[R]=C
            if solve(R+1,regine,N):
                return True
    return False
        
for N in range(4,30):
    soluzione=[None]*N
    if solve(R=0,regine=soluzione,N=N):
        print(f'{N:3d} {soluzione}')

