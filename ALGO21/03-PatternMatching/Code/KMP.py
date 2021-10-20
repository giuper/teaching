def calcolaNext(P):
    M=len(P)
    NXT=[0]
    l=0; i=1
    while i<M:
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
    return NXT
    

def kmpPM(T,P):
    N=len(T)
    M=len(P)
    NXT=calcolaNext(P)
    res=[]
    i=0
    j=0
    while(i<N):
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
    return res
           
        
if __name__=='__main__':
    T="111011110111101111001110111101"
    P="1110111101"
    res=kmpPM(T,P)
    for x in res:
        print(T[x:x+len(P)])
    print(P)


        
    
