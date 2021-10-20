from subsetSum2 import SubsetSum2

for t in range(9192):
    ss=SubsetSum2([1,2,4,8,16,32,64,128,256,512,1024,2048],t)
    result=ss.Solve()
    print(t,result)
    if result:   
        print(ss)


