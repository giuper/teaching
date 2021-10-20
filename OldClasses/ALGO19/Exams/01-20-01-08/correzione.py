solModule=__import__("sol")
testcases=[[1,"sol1",["2 3 + 4 5 + + 2 1 + *"]],[2,"sol2",["a 4 b + 2 a + * +",{'a':1,'b':20}]],[1,"sol3",["33 40 5 + 2 10 + * +"]]]

for testcase in testcases:
    func=getattr(solModule,testcase[1])
    if testcase[0]==1:
        testcase.append(func(testcase[2][0]))
    else:
        testcase.append(func(testcase[2][0],testcase[2][1]))

consegne=["sol"]
modules=map(__import__,consegne)

for module in modules:
    f=[]
    for testcase in testcases:
        #print(testcase)
        try:
            func=getattr(module,testcase[1])
            if testcase[0]==1:
                resc=func(testcase[2][0])
            else:
                resc=func(testcase[2][0],testcase[2][1])
            f.append(resc==testcase[3])
        except:
            f.append(False)
    
    print(module.__name__,"\t",f)

