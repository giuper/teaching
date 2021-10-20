
def trovaI(P):
##restituisce una posizione di P che e' ancora vuota

    for i in range(len(P)):
        if P[i]==None:
            return i
    
def ammissibile(P,M):
    if sum(P)<M:
        return False
    
    l=len(P)
    
    for i in range(l-1):
        if P[i+1]==P[i]+1 or P[i+1]==P[i]-1:
            return False
        
    for i in range(l):
        for j in range(l):
            if (P[i]==P[j]) and (i!=j):
                return False
    return True
    
def completa(P):
    for x in P:
        if x==None:
            return False
    return True


def isNotExtUlt(P,d,M,N):
#d is the number of empty positions
#M is the minimum sum for an admissible solution
#N is the maximum value that can be added to P

#calcoliamo la somma di tutti gli elementi
#gia' presenti nella soluzione parziale

    s=0
    for x in P:
        if x!=None:
            s=s+x

    if s+d*N-((d-1)*d)/2<M:
        return True
    
    l=len(P)
    
    for i in range(l-1):
        if P[i]!=None:
            if P[i+1]==P[i]+1 or P[i+1]==P[i]-1:
                return True
        
    for i in range(l):
        for j in range(l):
            if P[i]!=None and P[j]!=None:
                if (P[i]==P[j]) and (i!=j):
                    return True
    return False
    


def isNotExt3(P):
    if P[2]!=None and P[1]!=None:
        if P[2]==P[1]+1:
            return True

    if P[3]!=None and P[4]!=None:
        if P[4]==P[3]+1:
            return True
    
    return isNotExt(P)

def isNotExt2(P):
    if P[2]==None or P[1]==None:
        return False
    if P[2]==P[1]+1:
        return True
    return isNotExt(P)

def isNotExt(P):
    if P[0]!=None and P[1]!=None and P[0]==P[1]:
        return True
    return False

def falsa(P):
    return False

def BT(P,d,M,N):
##inseriamo valori tra 1 e N
##all'inizio avevamo N=9

    if completa(P):
        if ammissibile(P,M):
            print "Soluzione trovata: ",P
            return 1
        else:
            print "Soluzione completa non amm: ",P
            return 0

    if isNotExtUlt(P,d,M,N):
        print "Soluzione non estendibile: ",P
        return 0
    print "Soluzione parziale: ",P
    i=trovaI(P)
    for s in range(N,0,-1):
        P[i]=s
        if BT(P,d-1,M,N)==1:
            return 1
    P[i]=None
    return 0


A=[None]*100;
BT(A,100,1000000,12000)





