from subsetSum0 import SubsetSum

L=[1,2,4,8,16,32,64,128,256,512,1024,2048]
print(L)
for t in range(1,9192):
    ss=SubsetSum(L,t)
    result=ss.Solve()
    print(t,result)
    if result:   
        print(ss.sol)


