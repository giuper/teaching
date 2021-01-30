from lt import tree


T=tree()
T.insert(91,"")
T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLR")
T.insert(9,"LR")
T.insert(3,"R")
T.insert(1,"RL")
T.insert(5,"RR")

print("Inorder dell'albero")
T.inorder()

for k in [0,2,4,7,8,31,39,55,78,1000,10000]:
    print(T.lt(k),"nodi contengono valore < ",k)
