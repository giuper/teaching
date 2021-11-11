#PRIME=67       #8018
#PRIME=10598   #44
#PRIME=100003  #7
PRIME=1000003 #1
#PRIME=5000011  #1
#PRIME=999999999999999543767  #1

import time
import sys

##Binary Search Iterative Version
def BSIter(L,x):
    l=0
    h=len(L)-1
    while l<=h:
        m=(h+l)//2
        if L[m][0]==x:
            return m
        if x<L[m][0]:
            h=m-1
        else:
            l=m+1
    return l

def RKH(a):
    #print("RKH inizia")
    #sys.stdout.flush()
    value=0
    #b=a[::-1]
    for x in a:
        value=(value*256+ord(x))%PRIME
        #value=(value*256+ord(x))
    #print("RKH finisce")
    #sys.stdout.flush()
    
    return value
    

def prepareText(T,m):
    current=RKH(T[:m])
    TT=[[current,0]]
    power=(256**(m-1))%PRIME
    for i in range(1,len(T)-m+1):
        current=((current-ord(T[i-1])*power)*256+ord(T[i-1+m]))%PRIME
        if (current<0):
            current+=PRIME
        TT.append([current,i])
        ##if len(TT)%10000==0:
            ##print(len(T),m,len(TT))
            ##sys.stdout.flush()
    TT.sort(key=lambda x:x[0])
    return aggregateDup(TT)

def lookup(TT,P):
    p=RKH(P)
    i=BSIter(TT,p)
    if i>=len(TT):
        return []
    if TT[i][0]==p:
        return TT[i][1]
    else:
        return []

def aggregateDup(TT):
    res=[]
    prev=None
    for x in TT:
        if prev is None:
            prev=x[0]
            agg=[x[1]]
            continue
        if prev==x[0]:
            agg.append(x[1])
            continue
        res.append([prev,agg])
        prev=x[0]
        agg=[x[1]]
    res.append([prev,agg])
    return res

if __name__=='__main__':

    f=open('DivinaCommedia.txt','r')
    T=f.read()
    f.close()
    
##    print("Cerchiamo testi di lunghezza 3 nella Divina Commedia")
##    TT=prepareText(T,3)
##    PP=['aba','abe','aca','ace','ada','ade','afa','afe','aga','age','ala','ale','ama','ame','ana','ane','apa','ape','ara','are','asa','ase','ata','ate','ava','ave','aza','aze']
##    for P in PP:
##        print(P,len(lookup(TT,P)))

    P="Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta."
    print("Cerchiamo un testo di lunghezza",len(P)," nella Divina Commedia")
    print(P)
    TT=prepareText(T,len(P))
    L=lookup(TT,P)
    l=len(L)
    print("Numero di match : ",l)
    if l<10:
        print("Posizioni: ",L)
        
    print("Primo utilizzato: ",PRIME)

