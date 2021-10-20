#lista di primi n numeri di ordine k
def fibIter(n,k):
    if n<=k:
        return 1
    A=[1]*k
    sumP=k
    for i in range(k+1,n+1):
        A.append(sumP)
        x=A.pop(0)
        sumP=2*sumP-x
    return A[k-1]


def maxK(n):
    mx=0
    for k in range(2,n):
        r=fibIter(n,k)
        if r>mx:
            mx=r
            kk=k
    return kk
