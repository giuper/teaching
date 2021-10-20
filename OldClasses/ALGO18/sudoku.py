import datetime

def stampa(P):
    print (P[0:9])
    print (P[9:18])
    print (P[18:27])
    print (P[27:36])
    print (P[36:45])
    print (P[45:54])
    print (P[54:63])
    print (P[63:72])
    print (P[72:81])
    print 

def contaNone(A):
    count=0
    for x in A:
        if x==None:
            count+=1
    return count

#restituisce la lista dei 9 elementi nella riga della casella i
def riga(i,P):
    inizio=i//9
    return P[inizio:inizio+9]

#restituisce la lista dei 9 elementi nella colonna della casella i
def colonna(i,P):
    inizio=i%9
    return P[inizio:81:9]
    
#restituisce la lista dei 9 elementi nel riquadro della casella i
def qiquadro(i,P):
    r=i//9
    c=i%9
    rs=(r//3)*3
    cs=(c//3)*3
    A=[]
    for riga in [rs,rs+1,rs+2]:
        for colonna in [cs,cs+1,cs+2]:
            A.append(P[9*riga+colonna])
    return A
        


def trovaINuovo(P):
    for i in range(81):
        if P[i]==None:
            return i

def trovaI(P):
    scoreMin=28
    for i in range(81):
        if P[i]!=None:
            continue
        R=riga(i,P)
        C=colonna(i,P)
        Q=qiquadro(i,P)
        score=contaNone(R)+contaNone(C)+contaNone(Q)
        if score<scoreMin:
            casella=i
            scoreMin=score

    return casella

def completa(P):
    for x in P:
        if x==None:
            return False
    return True

def differentiSet(A):
    B=set(A)
    if len(B)==9:
        return True
    else:
        return False

def differenti(A):
    for i in range(9):
        for j in range(9):
            if i!=j and A[i]!=None and A[j]!=None and A[i]==A[j]:
                return False
    return True
    

#costruisce la lista degli elementi
#nel riquadro che ha come angolo in alto a sinistra
#la casella i
def riquadro(P,i):
    A=[];
    for k in [i,i+9,i+18]:
        for j in range(3):
            A.append(P[k+j])
    return A

##i+0    i+1    i+2
##i+9+0  i+9+1  i+9+2
##i+18+0 i+18+1 i+18+2


#restituisce 
#True se non ci sono ripetizioni in righe, colonne e riquadri
#        di elementi diversi da None
#False altriment

def ammissibile(P):

#controllo se le righe hanno elementi distinti
    for inizio in range(0,81,9):
        A=P[inizio:inizio+9]
        if differenti(A)==False:
            return False

#controllo se le colonne hanno elementi distinti
    for inizio in range(9):
        A=[]
        for i in range(inizio,81,9):
            A.append(P[i])
        if differenti(A)==False:
            return False

#caselle di inizio dei 9 riquadri
#   0+0   0+3   0+6
#  27+0  27+3  27+6
#  54+0  54+3  54+6

    for inizio in [0,27,54]:
        for j in [0,3,6]:
            A=riquadro(P,inizio+j)
            if differenti(A)==False:
                return False

    return True


def isNotExt(P):
    return not ammissibile(P)


def BT(P):
    if completa(P):
        if ammissibile(P):
            print("Soluzione trovata: ")
            stampa(P)
            return 1
        else:
            #print("Soluzione completa non amm: ")
            #stampa(P)
            return 0

    if isNotExt(P):
        #print("Soluzione non estendibile: ")
        #stampa(P)
        return 0
    #print("Soluzione parziale: ")
    #stampa(P)
    i=trovaI(P)
    for s in range(1,10):
        P[i]=s
        if BT(P)==1:
            return 1
    P[i]=None
    return 0

ListProblems=[
[4,None,None,None,None,None,8,None,5,None,3,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,2,None,None,None,None,None,6,None,None,None,None,None,8,None,4,None,None,None,None,None,None,1,None,None,None,None,None,None,None,6,None,3,None,7,None,5,None,None,2,None,None,None,None,None,1,None,4,None,None,None,None,None,None,],
[5,2,None,None,None,6,None,None,None,None,None,None,None,None,None,7,None,1,3,None,None,None,None,None,None,None,None,None,None,None,4,None,None,8,None,None,6,None,None,None,None,None,None,5,None,None,None,None,None,None,None,None,None,None,None,4,1,8,None,None,None,None,None,None,None,None,None,3,None,None,2,None,None,None,8,7,None,None,None,None,None,],
[6,None,None,None,None,None,8,None,3,None,4,None,7,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,None,4,None,7,None,3,None,None,2,None,None,None,None,None,1,None,6,None,None,None,None,None,None,None,2,None,None,None,None,None,5,None,None,None,None,None,8,None,6,None,None,None,None,None,None,1,None,None,None,None,],
[4,8,None,3,None,None,None,None,None,None,None,None,None,None,None,None,7,1,None,2,None,None,None,None,None,None,None,7,None,5,None,None,None,None,6,None,None,None,None,2,None,None,8,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,7,6,None,None,None,3,None,None,None,None,None,4,None,None,None,None,None,None,5,None,None,None,None,],
[None,None,None,None,1,4,None,None,None,None,3,None,None,None,None,2,None,None,None,7,None,None,None,None,None,None,None,None,None,None,9,None,None,None,3,None,6,None,1,None,None,None,None,None,None,None,None,None,None,None,None,None,8,None,2,None,None,None,None,None,1,None,4,None,None,None,None,5,None,6,None,None,None,None,None,7,None,8,None,None,None,],
[None,None,None,None,None,None,5,2,None,None,8,None,4,None,None,None,None,None,None,3,None,None,None,9,None,None,None,5,None,1,None,None,None,6,None,None,2,None,None,7,None,None,None,None,None,None,None,None,3,None,None,None,None,None,6,None,None,None,1,None,None,None,None,None,None,None,None,None,None,7,None,4,None,None,None,None,None,None,None,3,None,],
[6,None,2,None,5,None,None,None,None,None,None,None,None,None,3,None,4,None,None,None,None,None,None,None,None,None,None,4,3,None,None,None,8,None,None,None,None,1,None,None,None,None,2,None,None,None,None,None,None,None,None,7,None,None,5,None,None,2,7,None,None,None,None,None,None,None,None,None,None,None,8,1,None,None,None,6,None,None,None,None,None,],
[None,5,2,4,None,None,None,None,None,None,None,None,None,7,None,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,8,None,2,None,None,None,3,None,None,None,None,None,6,None,None,None,9,None,5,None,None,None,None,None,1,None,6,None,3,None,None,None,None,None,None,None,None,None,None,None,8,9,7,None,None,None,None,None,None,None,None,],
[6,None,2,None,5,None,None,None,None,None,None,None,None,None,4,None,3,None,None,None,None,None,None,None,None,None,None,4,3,None,None,None,8,None,None,None,None,1,None,None,None,None,2,None,None,None,None,None,None,None,None,7,None,None,5,None,None,2,7,None,None,None,None,None,None,None,None,None,None,None,8,1,None,None,None,6,None,None,None,None,None,],
[None,9,2,3,None,None,None,None,None,None,None,None,None,8,None,1,None,None,None,None,None,None,None,None,None,None,None,1,None,7,None,4,None,None,None,None,None,None,None,None,None,None,None,6,5,8,None,None,None,None,None,None,None,None,None,6,None,5,None,2,None,None,None,4,None,None,None,None,None,7,None,None,None,None,None,9,None,None,None,None,None,],
[6,None,None,3,None,2,None,None,None,None,5,None,None,None,None,None,1,None,None,None,None,None,None,None,None,None,None,7,None,2,6,None,None,None,None,None,None,None,None,None,None,None,None,5,4,3,None,None,None,None,None,None,None,None,None,8,None,1,5,None,None,None,None,None,None,None,None,4,None,2,None,None,None,None,None,None,None,None,7,None,None,],
[None,6,None,5,None,1,None,9,None,1,None,None,None,9,None,None,5,3,9,None,None,None,None,7,None,None,None,None,4,None,8,None,None,None,7,None,None,None,None,None,None,None,5,None,8,None,8,1,7,None,5,None,3,None,None,None,None,None,5,None,2,None,None,None,None,None,None,None,None,None,None,None,None,7,6,None,None,8,None,None,None,],
[None,None,5,None,None,None,9,8,7,None,4,None,None,5,None,None,None,1,None,None,7,None,None,None,None,None,None,2,None,None,None,4,8,None,None,None,None,9,None,1,None,None,None,None,None,6,None,None,2,None,None,None,None,None,3,None,None,6,None,None,2,None,None,None,None,None,None,None,9,None,7,None,None,None,None,None,None,None,5,None,None,],
[3,None,6,None,7,None,None,None,None,None,None,None,None,None,None,None,5,1,8,None,None,None,None,None,None,None,None,None,1,None,4,None,5,None,None,None,7,None,None,None,None,None,6,None,None,None,None,None,2,None,None,None,None,None,None,2,None,None,None,None,None,4,None,None,None,None,None,8,None,3,None,None,None,None,None,5,None,None,None,None,None,],
[1,None,None,None,None,None,3,None,8,None,7,None,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,None,3,None,1,None,None,None,None,None,None,None,None,None,None,None,9,5,8,None,None,None,None,None,None,None,None,None,5,None,6,None,None,None,7,None,None,None,None,None,8,None,2,None,None,None,4,None,None,None,None,None,None,None,],
[6,None,None,3,None,2,None,None,None,None,4,None,None,None,None,None,1,None,None,None,None,None,None,None,None,None,None,7,None,2,6,None,None,None,None,None,None,None,None,None,None,None,None,5,4,3,None,None,None,None,None,None,None,None,None,8,None,1,5,None,None,None,None,None,None,None,None,4,None,2,None,None,None,None,None,None,None,None,7,None,None,],
[None,None,None,None,3,None,None,9,None,None,None,None,2,None,None,None,None,1,None,5,None,9,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,2,None,8,None,4,None,6,None,8,None,5,None,None,None,2,None,None,7,5,None,None,None,None,None,None,4,None,1,None,None,6,None,None,3,None,None,None,None,None,4,None,6,None,],
[4,5,None,None,None,None,None,3,None,None,None,None,8,None,1,None,None,None,None,9,None,None,None,None,None,None,None,None,None,None,None,5,None,None,9,None,2,None,None,7,None,None,None,None,None,8,None,None,None,None,None,None,None,None,None,1,None,None,4,None,None,None,None,None,None,None,None,None,None,7,None,2,None,None,None,6,None,None,8,None,None,],
[None,2,3,7,None,None,None,None,6,8,None,None,None,6,None,5,9,None,9,None,None,None,None,None,7,None,None,None,None,None,None,4,None,9,7,None,3,None,7,None,9,6,None,None,2,None,None,None,None,None,None,None,None,None,5,None,None,4,7,None,None,None,None,None,None,None,None,None,2,None,None,None,None,8,None,None,None,None,None,None,None,],
[None,None,8,4,None,None,None,3,None,None,None,None,3,None,None,None,None,None,9,None,None,None,None,1,5,7,4,7,9,None,None,None,8,None,None,None,None,None,None,None,None,7,None,None,5,1,4,None,None,None,None,None,2,None,None,None,9,None,6,None,None,None,2,None,5,None,None,None,None,4,None,None,None,None,None,None,9,None,None,5,6,],
[None,9,8,None,1,None,None,None,None,2,None,None,None,None,None,None,6,None,None,None,None,None,None,None,None,None,None,None,None,None,3,None,2,None,5,None,None,8,4,None,None,None,None,None,None,None,None,None,6,None,None,None,None,None,None,None,None,None,4,None,8,None,9,3,None,None,5,None,None,None,None,None,None,None,None,None,None,None,1,None,None,],
[None,None,2,4,7,None,None,5,8,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,4,None,None,None,None,None,2,None,None,None,9,5,2,8,None,9,None,4,None,None,None,None,9,None,None,None,1,None,None,None,None,None,None,None,None,None,3,None,3,None,None,None,None,7,5,None,None,6,8,5,None,None,2,None,None,None,],
[4,None,None,None,None,None,8,None,5,None,3,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,2,None,None,None,None,None,6,None,None,None,None,None,5,None,4,None,None,None,None,None,None,1,None,None,None,None,None,None,None,6,None,3,None,7,None,5,None,None,2,None,None,None,None,None,1,None,9,None,None,None,None,None,None,],
[None,2,None,3,None,None,None,None,None,None,6,3,None,None,None,None,None,5,8,None,None,None,None,None,None,None,1,5,None,None,None,None,9,None,3,None,None,None,None,7,None,None,None,None,None,None,None,None,1,None,None,None,None,8,None,8,7,9,None,None,2,6,None,None,None,None,None,None,6,None,7,None,None,None,6,None,None,7,None,None,4,],
[1,None,None,None,None,None,7,None,9,None,4,None,None,None,7,2,None,None,8,None,None,None,None,None,None,None,None,None,7,None,None,1,None,None,6,None,3,None,None,None,None,None,None,None,5,None,6,None,None,4,None,None,2,None,None,None,None,None,None,None,None,None,8,None,None,5,3,None,None,None,7,None,7,None,2,None,None,None,None,4,6,],
[4,None,None,None,None,None,3,None,None,None,None,None,8,None,2,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,1,None,None,None,8,7,3,4,None,None,None,None,None,None,None,6,None,None,None,None,None,None,None,None,5,None,None,None,6,None,None,None,None,None,None,None,None,1,None,4,None,None,None,8,2,None,None,None,None,None,None,],
[None,None,None,None,None,None,None,7,1,None,2,None,8,None,None,None,None,None,None,None,None,4,None,3,None,None,None,7,None,None,None,6,None,None,5,None,None,None,None,2,None,None,3,None,None,9,None,None,None,None,None,None,None,None,6,None,None,None,7,None,None,None,None,None,8,None,None,None,None,4,None,None,None,None,None,None,5,None,None,None,None,],
[6,None,None,3,None,2,None,None,None,None,4,None,None,None,None,None,8,None,None,None,None,None,None,None,None,None,None,7,None,2,6,None,None,None,None,None,None,None,None,None,None,None,None,5,4,3,None,None,None,None,None,None,None,None,None,8,None,1,5,None,None,None,None,None,None,None,None,8,None,2,None,None,None,None,None,None,None,None,7,None,None,],
[None,4,7,None,8,None,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,6,None,None,7,None,None,6,None,None,None,None,3,5,7,None,None,None,None,None,None,5,None,None,None,None,1,None,None,6,None,None,None,None,2,8,None,None,4,None,None,None,None,None,9,None,1,None,None,None,4,None,None,None,None,None,2,None,6,9,None,],
[None,None,None,None,None,None,8,None,1,7,None,None,2,None,None,None,None,None,None,None,None,5,None,6,None,None,None,None,None,None,7,None,None,None,5,None,None,1,None,None,None,None,3,None,None,None,8,None,None,None,None,None,None,None,5,None,None,None,None,None,None,2,None,None,4,None,None,8,None,None,None,None,6,None,None,None,3,None,None,None,None,],
[3,8,None,6,None,None,None,None,None,None,None,9,None,None,None,None,None,None,None,2,None,None,3,None,5,1,None,None,None,None,None,None,5,None,None,None,None,3,None,None,1,None,None,6,None,None,None,None,4,None,None,None,None,None,None,1,7,None,5,None,None,8,None,None,None,None,None,None,None,9,None,None,None,None,None,None,None,7,None,3,2,],
[None,None,None,5,None,None,None,None,None,None,None,None,None,None,None,5,None,6,9,7,None,None,None,None,None,2,None,None,None,4,8,None,2,None,None,None,2,5,None,1,None,None,None,3,None,None,8,None,None,3,None,None,None,None,None,None,None,None,None,4,None,7,None,None,1,3,None,5,None,None,9,None,None,2,None,None,None,3,1,None,None,],
[None,2,None,None,None,None,None,None,None,3,None,5,None,6,2,None,None,9,None,6,8,None,None,None,3,None,None,None,5,None,None,None,None,None,None,None,None,None,None,6,4,None,8,None,2,None,None,4,7,None,None,9,None,None,None,None,3,None,None,None,None,None,1,None,None,None,None,None,6,None,None,None,1,7,None,4,3,None,None,None,None,],
[None,8,None,None,4,None,None,None,None,3,None,None,None,None,None,None,1,None,None,None,None,None,None,None,None,2,None,None,None,5,None,None,None,4,None,6,9,None,None,1,None,None,8,None,None,2,None,None,None,None,None,None,None,None,None,None,None,3,None,9,None,None,None,None,6,None,None,None,None,5,None,None,None,None,None,2,None,None,None,None,None,],
[None,None,8,None,9,None,1,None,None,None,6,None,5,None,None,None,2,None,None,None,None,None,None,6,None,None,None,None,3,None,1,None,7,None,5,None,None,None,None,None,None,None,None,None,9,None,None,4,None,None,None,3,None,None,None,5,None,None,None,None,2,None,None,None,7,None,None,None,3,None,8,None,2,None,None,7,None,None,None,None,4,],
[4,None,None,None,None,None,5,None,8,None,3,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,2,None,None,None,None,None,6,None,None,None,None,None,5,None,8,None,None,None,None,None,None,1,None,None,None,None,None,None,None,6,None,3,None,7,None,5,None,None,2,None,None,None,None,None,1,None,8,None,None,None,None,None,None,],
[1,None,None,None,None,None,3,None,8,None,6,None,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,None,3,None,1,None,None,None,None,None,None,None,None,None,None,None,9,5,8,None,None,None,None,None,None,None,None,None,5,None,6,None,None,None,7,None,None,None,None,None,8,None,2,None,None,None,4,None,None,None,None,None,None,None,],
[1,None,None,None,None,6,None,8,None,None,6,4,None,None,None,None,None,None,None,None,None,None,4,None,None,None,7,None,None,None,None,9,None,6,None,None,None,7,None,4,None,None,5,None,None,5,None,None,None,7,None,1,None,None,None,5,None,None,None,None,3,2,None,3,None,None,None,None,8,None,None,None,4,None,None,None,None,None,None,None,None,],
[2,4,9,None,6,None,None,None,3,None,3,None,None,None,None,2,None,None,8,None,None,None,None,None,None,None,5,None,None,None,None,None,6,None,None,None,None,None,None,2,None,None,None,None,None,None,1,None,None,4,None,8,2,None,None,9,None,5,None,None,7,None,None,None,None,4,None,None,None,None,None,1,None,7,None,None,None,3,None,None,None,],
[None,None,None,8,None,None,None,None,9,None,8,7,3,None,None,None,4,None,6,None,None,7,None,None,None,None,None,None,None,8,5,None,None,9,7,None,None,None,None,None,None,None,None,None,None,None,4,3,None,None,7,5,None,None,None,None,None,None,None,3,None,None,None,None,3,None,None,None,1,4,5,None,4,None,None,None,None,2,None,None,1,],
[None,None,None,5,None,1,None,None,None,None,9,None,None,None,None,8,None,None,None,6,None,None,None,None,None,None,None,4,None,1,None,None,None,None,None,None,None,None,None,None,7,None,None,9,None,None,None,None,None,None,None,None,3,None,8,None,None,None,None,None,1,None,5,None,None,None,2,None,None,4,None,None,None,None,None,3,6,None,None,None,None,],
[None,None,None,None,None,None,8,None,1,6,None,None,2,None,None,None,None,None,None,None,None,7,None,5,None,None,None,None,None,None,6,None,None,None,2,None,None,1,None,None,None,None,3,None,None,None,8,None,None,None,None,None,None,None,2,None,None,None,None,None,None,7,None,None,3,None,None,8,None,None,None,None,5,None,None,None,4,None,None,None,None,],
[None,4,7,6,None,None,None,5,None,8,None,3,None,None,None,None,None,2,None,None,None,None,None,9,None,None,None,None,None,None,8,None,5,None,None,6,None,None,None,1,None,None,None,None,None,6,None,2,4,None,None,None,None,None,None,7,8,None,None,None,5,1,None,None,None,6,None,None,None,None,4,None,None,9,None,None,None,4,None,None,7,],
[None,None,None,None,None,7,None,9,5,None,None,None,None,None,1,None,None,None,8,6,None,None,2,None,None,None,None,None,2,None,None,7,3,None,None,8,5,None,None,None,None,None,None,6,None,None,None,3,None,None,4,9,None,None,3,None,5,None,None,None,4,1,7,2,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
[None,4,None,5,None,None,None,None,None,8,None,None,None,9,None,None,3,None,None,7,6,None,2,None,None,None,None,None,1,4,6,None,None,None,None,None,None,None,None,None,None,9,None,None,7,None,None,None,None,None,3,6,None,None,None,None,1,None,None,4,None,5,None,None,6,None,None,None,None,None,None,3,None,None,7,1,None,None,2,None,None,],
[None,8,3,4,None,None,None,None,None,None,None,None,None,7,None,None,5,None,None,None,None,None,None,None,None,None,None,None,4,None,1,None,8,None,None,None,None,None,None,None,None,None,None,2,7,None,None,None,3,None,None,None,None,None,2,None,6,None,5,None,None,None,None,5,None,None,None,None,None,8,None,None,None,None,None,None,None,None,1,None,None,],
[None,None,9,None,None,None,None,None,3,None,None,None,None,None,9,None,None,None,7,None,None,None,None,None,5,None,6,None,None,6,5,None,None,4,None,None,None,None,None,3,None,None,None,None,None,None,2,8,None,None,None,None,None,None,3,None,None,7,5,None,6,None,None,6,None,None,None,None,None,None,None,None,None,None,None,1,2,None,3,None,8,],
[None,2,6,None,3,9,None,None,None,None,None,None,6,None,None,None,None,1,9,None,None,None,None,None,7,None,None,None,None,None,None,None,4,None,None,9,None,5,None,None,None,None,2,None,None,None,None,8,5,None,None,None,None,None,3,None,None,2,None,None,9,None,None,4,None,None,None,None,7,6,2,None,None,None,None,None,None,None,None,None,4,],
[2,None,3,None,8,None,None,None,None,8,None,None,7,None,None,None,None,None,None,None,None,None,None,None,1,None,None,None,6,None,5,None,7,None,None,None,4,None,None,None,None,None,None,3,None,None,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,8,2,None,5,None,None,None,None,6,None,None,None,1,None,None,None,None,None,None,None,],
[6,None,None,3,None,2,None,None,None,None,1,None,None,None,None,None,5,None,None,None,None,None,None,None,None,None,None,7,None,2,6,None,None,None,None,None,None,None,None,None,None,None,None,8,4,3,None,None,None,None,None,None,None,None,None,8,None,1,5,None,None,None,None,None,None,None,None,8,None,2,None,None,None,None,None,None,None,None,7,None,None,],
[1,None,None,None,None,None,9,None,None,None,6,4,None,None,1,None,7,None,None,7,None,None,4,None,None,None,None,None,None,None,3,None,None,None,None,None,3,None,8,9,None,None,5,None,None,None,None,7,None,None,None,None,2,None,None,None,None,None,6,None,7,None,9,None,None,None,None,None,4,None,1,None,None,None,None,1,2,9,None,3,None,],
[None,None,None,None,None,None,None,None,None,9,None,None,None,None,None,None,8,4,None,6,2,3,None,None,None,5,None,None,None,None,6,None,None,None,4,5,3,None,None,None,1,None,None,None,6,None,None,None,9,None,None,None,7,None,None,None,None,1,None,None,None,None,None,4,None,5,None,None,2,None,None,None,None,3,None,8,None,None,None,None,9,],
[None,2,None,None,None,None,5,9,3,8,None,None,5,None,None,4,6,None,9,4,None,None,6,None,None,None,8,None,None,2,None,3,None,None,None,None,None,6,None,None,8,None,7,3,None,7,None,None,2,None,None,None,None,None,None,None,None,None,4,None,3,8,None,None,7,None,None,None,None,6,None,None,None,None,None,None,None,None,None,None,5,],
[9,None,4,None,None,5,None,None,None,2,5,None,6,None,None,1,None,None,3,1,None,None,None,None,None,None,8,None,7,None,None,None,9,None,None,None,4,None,None,2,6,None,None,None,None,None,None,1,4,7,None,None,None,None,7,None,None,None,None,None,None,None,2,None,None,None,3,None,None,8,None,6,None,4,None,None,None,None,None,9,None,],
[None,None,None,5,2,None,None,None,None,None,9,None,None,None,3,None,None,4,None,None,None,None,None,None,7,None,None,None,1,None,None,None,None,None,4,None,None,8,None,None,4,5,3,None,None,6,None,None,None,1,None,None,None,8,7,None,2,None,None,None,None,None,None,None,None,8,None,None,None,None,3,2,None,4,None,None,8,None,None,1,None,],
[5,3,None,None,2,None,9,None,None,None,2,4,None,3,None,None,5,None,None,None,9,None,None,None,None,None,None,None,None,None,None,1,None,8,2,7,None,None,None,7,None,None,None,None,None,None,None,None,None,9,8,1,None,None,None,None,None,None,None,None,None,None,None,None,None,6,4,None,None,None,None,9,1,None,2,None,5,None,4,3,None,],
[1,None,None,None,None,7,8,6,None,None,None,7,None,None,8,None,1,None,8,None,None,2,None,None,None,None,9,None,None,None,None,None,None,None,None,2,4,None,None,None,1,None,None,None,None,None,None,9,None,None,5,None,None,None,6,None,8,None,None,None,None,None,None,None,None,None,None,5,None,9,None,None,None,None,None,None,None,9,3,None,4,],
[None,None,None,None,5,None,None,None,1,1,None,None,None,None,None,None,7,None,None,6,None,None,None,None,None,8,None,None,None,None,None,None,4,None,None,None,None,None,9,None,1,None,3,None,None,None,None,None,5,9,6,None,2,None,None,8,None,None,6,2,None,None,7,None,None,7,None,None,None,None,None,None,3,None,5,None,7,None,2,None,None,],
[None,4,7,None,2,None,None,None,None,8,None,None,None,None,1,None,None,None,None,3,None,None,None,None,9,None,2,None,None,None,None,None,5,None,None,None,6,None,None,8,1,None,None,5,None,None,None,None,None,4,None,None,None,None,None,7,None,None,None,None,3,None,4,None,None,None,9,None,None,None,1,None,4,None,None,2,7,None,8,None,None,],
[None,None,None,None,None,None,9,4,None,None,None,None,None,9,None,None,None,5,3,None,None,None,None,5,None,7,None,None,8,None,4,None,None,1,None,None,4,6,3,None,None,None,None,None,None,None,None,None,None,None,7,None,8,None,8,None,None,7,None,None,None,None,None,7,None,None,None,None,None,None,2,8,None,5,None,2,6,None,None,None,None,],
[None,2,None,None,None,None,None,None,6,None,None,None,None,4,1,None,None,None,None,None,7,8,None,None,None,None,1,None,None,None,None,None,None,7,None,None,None,None,3,7,None,None,None,None,None,6,None,None,4,1,2,None,None,None,None,1,None,None,7,4,None,None,5,None,None,8,None,5,None,None,7,None,None,None,None,None,None,3,9,None,None,],
[1,None,None,None,None,None,3,None,8,None,6,None,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,None,3,None,1,None,None,None,None,None,None,None,None,None,None,None,7,5,8,None,None,None,None,None,None,None,None,None,7,None,5,None,None,None,6,None,None,None,None,None,8,None,2,None,None,None,4,None,None,None,None,None,None,None,],
[2,None,None,None,None,1,None,9,None,None,1,None,None,3,None,7,None,None,9,None,None,8,None,None,None,2,None,None,None,None,None,None,None,8,5,None,None,6,None,4,None,None,None,None,None,None,None,None,None,7,None,None,None,3,None,2,None,3,None,None,None,6,None,None,None,None,5,None,None,None,None,None,1,None,9,None,None,None,2,None,5,],
[None,None,7,None,None,8,None,None,None,None,None,6,None,2,None,3,None,None,None,3,None,None,None,None,None,None,9,None,1,None,None,5,None,None,6,None,None,None,None,None,1,None,None,None,None,None,7,None,9,None,None,None,None,2,None,None,None,None,None,None,None,None,4,None,8,3,None,None,4,None,None,None,2,6,None,None,None,None,5,1,None,],
[None,None,None,3,6,None,None,None,None,8,5,None,None,None,None,None,None,None,9,None,4,None,None,8,None,None,None,None,None,None,None,None,6,8,None,None,None,None,None,None,None,None,None,1,7,None,None,9,None,None,4,5,None,None,None,1,None,5,None,None,None,6,None,4,None,None,None,None,9,None,None,2,None,None,None,None,None,3,None,None,None,],
[3,4,None,6,None,None,None,None,None,None,None,7,None,None,None,None,None,None,None,2,None,None,8,None,5,7,None,None,None,None,None,None,5,None,None,None,None,7,None,None,1,None,None,2,None,None,None,None,4,None,None,None,None,None,None,3,6,None,2,None,None,1,None,None,None,None,None,None,None,9,None,None,None,None,None,None,None,7,None,8,2,],
[None,None,None,None,None,None,4,None,1,8,None,None,2,None,None,None,None,None,None,None,None,6,None,7,None,None,None,None,None,None,8,None,None,None,6,None,None,4,None,None,None,None,3,None,None,None,1,None,None,None,None,None,None,None,6,None,None,None,None,None,None,2,None,None,5,None,None,1,None,None,None,None,7,None,None,None,3,None,None,None,None,],
[None,4,None,None,5,None,None,6,7,None,None,None,1,None,None,None,4,None,None,None,None,2,None,None,None,None,None,1,None,None,8,None,None,3,None,None,None,None,None,None,None,None,2,None,None,None,6,None,None,None,None,None,None,None,None,None,None,None,4,None,None,5,None,3,None,None,None,None,None,8,None,None,2,None,None,None,None,None,None,None,None,],
[None,None,None,None,None,None,None,4,None,None,None,2,None,None,4,None,None,1,None,7,None,None,5,None,None,9,None,None,None,3,None,None,7,None,None,None,None,4,None,None,6,None,None,None,None,6,None,None,1,None,None,8,None,None,None,2,None,None,None,None,1,None,None,8,5,None,9,None,None,None,6,None,None,None,None,None,8,None,None,None,3,],
[8,None,None,7,None,None,None,None,4,None,5,None,None,None,None,6,None,None,None,None,None,None,None,None,None,None,None,None,3,None,9,7,None,None,None,8,None,None,None,None,4,3,None,None,5,None,None,None,None,2,None,9,None,None,None,None,6,None,None,None,None,None,None,2,None,None,None,6,None,None,None,7,None,7,1,None,None,8,3,None,2,],
[None,8,None,None,None,4,None,5,None,None,None,None,7,None,None,3,None,None,None,None,None,None,None,None,None,None,None,None,1,None,None,8,5,None,None,None,6,None,None,None,None,None,2,None,None,None,None,None,None,4,None,None,None,None,3,None,2,6,None,None,None,None,None,None,None,None,None,None,None,None,4,1,7,None,None,None,None,None,None,None,None,],
[None,None,None,None,7,None,None,8,None,None,None,6,None,None,None,5,None,None,None,2,None,None,None,3,None,6,1,None,1,None,None,None,7,None,None,2,None,None,8,None,None,5,3,4,None,2,None,None,9,None,None,None,None,None,None,None,2,None,None,None,None,None,None,5,8,None,None,None,6,None,3,None,4,None,None,None,1,None,None,None,None,],
[None,None,None,None,None,None,8,None,1,6,None,None,2,None,None,None,None,None,None,None,None,7,None,5,None,None,None,None,None,None,6,None,None,None,2,None,None,1,None,None,None,None,3,None,None,None,8,None,None,None,None,None,None,None,2,None,None,None,None,None,None,7,None,None,4,None,None,8,None,None,None,None,5,None,None,None,3,None,None,None,None,],
[None,2,None,None,None,None,None,None,None,None,None,None,6,None,None,None,None,3,None,7,4,None,8,None,None,None,None,None,None,None,None,None,3,None,None,2,None,8,None,None,4,None,None,1,None,6,None,None,5,None,None,None,None,None,None,None,None,None,1,None,7,8,None,5,None,None,None,None,9,None,None,None,None,None,None,None,None,None,None,4,None,],
[None,5,2,None,None,6,8,None,None,None,None,None,None,None,7,None,2,None,None,None,None,None,None,None,6,None,None,None,None,4,8,None,None,9,None,None,2,None,None,4,1,None,None,None,None,None,None,1,None,None,None,None,None,8,None,None,6,1,None,None,3,8,None,None,None,None,None,9,None,None,None,6,3,None,None,6,None,None,1,None,9,],
[None,None,None,None,1,None,7,8,None,5,None,None,None,None,9,None,None,None,None,None,None,None,None,None,None,4,None,None,2,None,None,None,None,None,None,None,None,None,None,6,None,None,None,None,3,None,7,4,None,8,None,None,None,None,None,None,None,None,None,3,None,None,2,None,8,None,None,4,None,None,1,None,6,None,None,5,None,None,None,None,None,],
[1,None,None,None,None,None,None,None,3,None,6,None,3,None,None,7,None,None,None,7,None,None,None,5,None,None,1,2,1,None,7,None,None,None,9,None,None,None,7,None,None,None,None,None,None,None,None,8,None,1,None,None,2,None,None,None,None,8,None,6,4,None,None,None,None,9,None,2,None,None,6,None,None,None,None,4,None,None,None,None,None,],
[4,None,None,None,7,None,1,None,None,None,None,1,9,None,4,6,None,5,None,None,None,None,None,1,None,None,None,None,None,None,7,None,None,None,None,2,None,None,2,None,3,None,None,None,None,8,4,7,None,None,6,None,None,None,None,1,4,None,None,None,8,None,6,None,2,None,None,None,None,3,None,None,6,None,None,None,9,None,None,None,None,],
[None,None,None,None,None,None,8,None,1,7,None,None,2,None,None,None,None,None,None,None,None,5,None,6,None,None,None,None,None,None,7,None,None,None,5,None,None,1,None,None,None,None,3,None,None,None,8,None,None,None,None,None,None,None,5,None,None,None,None,None,None,2,None,None,3,None,None,8,None,None,None,None,6,None,None,None,4,None,None,None,None,],
[9,6,3,None,None,None,None,None,None,1,None,None,None,None,8,None,None,None,None,None,None,2,None,5,None,None,None,None,4,None,8,None,None,None,None,None,None,1,None,None,None,None,7,None,None,None,None,None,None,3,None,None,2,5,7,None,None,None,None,None,None,3,None,None,None,9,None,2,None,4,None,7,None,None,None,None,None,None,9,None,None,],
[1,5,None,3,None,None,None,None,None,None,7,None,None,4,None,2,None,None,None,None,4,None,7,2,None,None,None,None,None,8,None,None,None,None,None,None,None,None,None,9,None,None,1,None,8,None,1,None,None,8,None,7,9,None,None,None,None,None,None,3,8,None,None,None,None,None,None,None,None,None,None,None,6,None,None,None,None,7,4,2,3,],
[None,None,None,None,None,None,None,None,None,None,5,7,2,4,None,None,None,9,8,None,None,None,None,9,4,7,None,None,None,9,None,None,3,None,None,None,5,None,None,9,None,None,1,2,None,None,None,3,None,1,None,9,None,None,None,6,None,None,None,None,2,5,None,None,None,None,5,6,None,None,None,None,None,7,None,None,None,None,None,None,6,],
[None,None,None,None,7,5,None,None,None,None,1,None,None,2,None,None,None,None,None,4,None,None,None,3,None,None,None,5,None,None,None,None,None,3,None,2,None,None,None,8,None,None,None,1,None,None,None,None,None,None,None,6,None,None,None,None,None,1,None,None,4,8,None,2,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,],
[6,None,None,None,None,None,7,None,3,None,4,None,8,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,None,4,None,8,None,7,None,None,2,None,None,None,None,None,1,None,3,None,None,None,None,None,None,None,2,None,None,None,None,None,5,None,None,None,None,None,7,None,9,None,None,None,None,None,None,1,None,None,None,None,],
[None,None,None,None,6,None,None,None,4,None,None,6,None,3,None,None,None,None,1,None,None,4,None,None,5,None,7,7,None,None,None,None,None,8,None,5,None,None,None,8,None,None,None,None,None,6,None,8,None,None,None,None,9,None,None,None,2,None,9,None,None,None,None,4,None,None,None,None,3,2,None,None,None,None,9,7,None,None,1,None,None,],
[None,3,2,None,None,None,None,None,5,8,None,None,3,None,None,None,None,None,9,None,4,2,8,None,None,None,1,None,None,None,4,None,None,None,3,9,None,None,None,6,None,None,None,5,None,None,None,None,None,1,None,None,None,None,None,2,None,None,None,6,7,None,8,None,None,None,None,None,4,None,None,None,None,9,5,None,None,None,None,6,None,],
[None,None,None,5,None,3,None,None,None,None,None,None,None,6,None,7,None,None,5,None,8,None,None,None,None,1,6,3,6,None,None,2,None,None,None,None,None,None,None,4,None,1,None,None,None,None,None,None,None,3,None,None,None,5,6,7,None,None,None,None,2,None,8,None,None,4,None,7,None,None,None,None,None,None,None,2,None,None,5,None,None,],
[None,5,None,3,None,7,None,4,None,1,None,None,None,None,None,None,None,None,None,3,None,None,None,None,None,None,None,5,None,8,None,3,None,6,1,None,None,None,None,8,None,None,5,None,9,None,6,None,None,1,None,None,None,None,None,None,None,None,4,None,None,None,6,None,None,None,6,9,2,7,None,None,None,None,2,None,None,None,9,None,None,],
[None,None,5,None,None,8,None,None,1,8,None,None,None,None,None,None,9,None,None,None,None,None,None,None,7,8,None,None,None,None,4,None,None,None,None,None,6,4,None,None,None,None,9,None,None,None,None,None,None,5,3,None,None,2,None,6,None,None,None,None,None,None,None,None,None,1,3,8,None,None,5,None,None,None,None,9,None,7,1,4,None,],
[None,None,None,None,None,None,None,None,None,None,7,2,None,6,None,1,None,None,None,None,5,1,None,None,None,8,2,None,8,None,None,None,1,3,None,None,4,None,None,None,None,None,None,None,None,None,3,7,None,9,None,None,1,None,None,None,None,None,2,3,8,None,None,5,None,4,None,None,9,None,None,None,None,None,None,None,None,None,7,9,None,],
[None,None,None,6,5,8,None,None,None,None,None,4,None,None,None,None,None,None,1,2,None,None,None,None,None,None,None,None,None,None,None,None,9,6,None,7,None,None,None,3,None,None,5,None,None,None,None,2,None,8,None,None,None,3,None,None,1,9,None,None,8,None,None,3,None,6,None,None,None,None,None,4,None,None,None,None,4,7,3,None,None,],
[None,2,None,3,None,None,None,None,None,None,None,6,None,None,8,None,9,None,8,3,None,5,None,None,None,None,None,None,None,None,2,None,None,None,8,None,7,None,9,None,None,5,None,None,None,None,None,None,None,None,6,None,None,4,None,None,None,None,None,None,None,1,None,None,None,1,None,None,None,4,None,2,2,None,None,7,None,None,8,None,9,],
[None,5,None,None,9,None,None,None,None,1,None,None,None,None,None,6,None,None,None,None,None,3,None,8,None,None,None,None,None,8,None,4,None,None,None,9,5,1,4,None,None,None,None,None,None,None,3,None,None,None,None,2,None,None,None,None,None,None,None,None,None,None,4,None,8,None,None,None,6,None,None,7,7,None,None,1,5,None,None,6,None,],
[None,None,None,None,None,2,None,None,None,None,None,None,None,7,None,None,None,1,7,None,None,3,None,None,None,9,None,8,None,None,7,None,None,None,None,None,None,2,None,8,9,None,6,None,None,None,1,3,None,None,6,None,None,None,None,9,None,None,5,None,8,2,4,None,None,None,None,None,8,9,1,None,None,None,None,None,None,None,None,None,None,],
[3,None,None,None,8,None,None,None,None,None,None,None,7,None,None,None,None,5,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,3,6,None,None,None,2,None,None,4,None,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,6,None,1,3,None,None,4,5,2,None,None,None,None,None,None,None,None,None,None,None,8,None,None,],
]

for P in ListProblems:
    print(datetime.datetime.now())
    stampa(P)
    BT(P)
    print ("\n")
