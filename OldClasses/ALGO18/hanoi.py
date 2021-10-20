
def hanoi(n,i,f,t):

    if n==1:
        print "da ",i,"a ",f
    else:
        hanoi(n-1,i,t,f)
        print "da ",i,"a ",f
        hanoi(n-1,t,f,i)

hanoi(64,"A","C","B")
        
