def bfPM(T,P):
    res=[]
    n=len(T)
    m=len(P)

    for s in range(n-m+1):
        found=True
        for i in range(m):
            if P[i]!=T[s+i]:
                found=False
                break
        if found:
            res.append(s)
    return res

if __name__=='__main__':
    T="bacabcabca"
    P="cabc"
    print(bfPM(T,P))

