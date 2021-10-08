def detRecSelect(A,k):
    pivot=A[0] 
    L=[]
    R=[]
    
    for a in A:
        if a<pivot:
            L.append(a)
        if a>pivot:
            R.append(a)
            
    l=len(L)
    if l==k:
        return pivot
    if l>k:
        return detRecSelect(L,k)
    else:
        return detRecSelect(R,k-l-1)
