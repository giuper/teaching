from subsetSum5 import SubsetSum5

L=[1,2,4,8]
for t in range(16):
    ss=SubsetSum5(L,t)
    result=ss.Solve()
    print(t,result)
    if result:   
        print(ss)
    else:
        print()



