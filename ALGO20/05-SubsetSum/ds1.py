from subsetSum1 import SubsetSum1

for t in range(9192):
    ss=SubsetSum1([1,2,4,8,16,32,64,128,256,512,1024,2048],t)
    result=ss.Solve()
    print(t,result)
    if result:   
        print(ss)


