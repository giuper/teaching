from subsetSum2 import SubsetSum2

for x in range(9192):
    ss=SubsetSum2([1,2,4,8,16,32,64,128,256,512,1024,2048],x)
    result=ss.Solve()
    print(x,result)
    if result:   
        print(ss)


