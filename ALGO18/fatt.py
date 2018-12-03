def fattoriale(n):
    res=1;
    for i in range(1,n+1):
        res=res*i;
    return res

def rfattoriale(n):
    if n==1:
        return 1
    return n*rfattoriale(n-1);

for i in range(1,20):
    print "fattoriale di", i, "=\t",fattoriale(i),"\t\t",rfattoriale(i);
