#Lista L da indice l incluso a indice h escluso
def partition(L,l,h):
    if l==h-1:
        return l
    i=l-1         
    pivot=L[h-1] # pivot
  
    for j in range(l,h):
        if L[j]<=pivot:
            L[i+1],L[j]=L[j],L[i+1]
            i=i+1

    return i


