def calcolaNext(P):
    M=len(P)
    NXT=[0]
    l=0; i=1
    nofC=0
    while i<M:
        nofC+=1
        if P[i]==P[l]:
            l=l+1
            NXT.append(l)
            i=i+1
        else:
            if l!=0:
                l=NXT[l-1]
            else:
                NXT.append(0)
                i=i+1
    NXT.append(nofC)
    return NXT
    

def kmpPM(T,P):
    N=len(T)
    M=len(P)
    NXT=calcolaNext(P)
    res=[]
    i=0
    j=0
    nofC=NXT.pop()
    while(i<N):
        nofC+=1
        if (P[j]==T[i]):
            j=j+1
            i=i+1
        if (j==M):
            res.append(i-M) 
            j=NXT[j-1]
            continue
        
        if i<N and P[j]!=T[i]:
            if j!=0:
                j=NXT[j-1]
            else:
                i=i+1
    res.insert(0,nofC)
    return res
           
        
if __name__=='__main__':
    T="bacabcabcabdcabdcabdcabccccabc"
    P="cabc"
    print("Testo:      ",T)
    print("Pattern:    ",P)
    print("Occorrenze: ",kmpPM(T,P))

    print()
    N=100_000_000
    print(N,"a seguite da una b")
    T="a"*N+"b"
    P="a"*(N//2)+"b"
    res=kmpPM(T,P)
    print("Confronti:  ",res[0])
    print("Occorrenze: ",res[1:])

        
    
