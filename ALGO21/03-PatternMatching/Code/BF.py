#restituisce una lista
#primo elemento == numero confronti effettuati
#seguito da tutte le occorrenze di P in T

def bfPM(T,P):
    res=[]
    n=len(T)
    m=len(P)

    nofC=0
    for s in range(n-m+1):
        found=True
        for i in range(m):
            nofC+=1
            if P[i]!=T[s+i]:
                found=False
                break
        if found:
            res.append(s)
    res.insert(0,nofC)
    return res

if __name__=='__main__':
    T="bacabcabcabdcabdcabdcabccccabc"
    P="cabc"
    print("Testo:      ",T)
    print("Pattern:    ",P)
    res=bfPM(T,P)
    print("Confronti:  ",res[0])
    print("Occorrenze: ",res[1:])

    print()
    N=10_000
    print(N,"a seguite da una b")
    T="a"*N+"b"
    P="a"*(N//2)+"b"
    res=bfPM(T,P)
    print("Confronti:  ",res[0])
    print("Occorrenze: ",res[1:])
