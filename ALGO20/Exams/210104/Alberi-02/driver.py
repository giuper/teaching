from sol import tree


T=tree()
T.insert(99,"")

T.insert(77,"L")
T.insert(3,"LL")
T.insert(54,"LLR")
T.insert(9,"LR")

T.insert(3,"R")
T.insert(10,"RL")
T.insert(15,"RR")

T.inorder()
print()

T.nuovo()
T.inorder()

