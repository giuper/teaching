
def rfib(n):
    if n==1 or n==2:
        return 1
    else:
        return rfib(n-1)+rfib(n-2)

def fib(n):
    res=[1,1]
    for i in range(n-2):
        res.append(res[-1]+res[-2])
    return res[-1]


for i in range(1,100):
    print "N"
    print fib(i)
    print "R"
    print rfib(i)
