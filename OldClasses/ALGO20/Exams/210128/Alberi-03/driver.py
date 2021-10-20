from numfo import tree


T=tree()
T.insert(91,"")

T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLR")
T.insert(9,"LR")

T.insert(3,"R")
T.insert(1,"RL")
T.insert(5,"RR")


print("Albero: ")


print("                       91 ")
print("                      /  \ ")
print("                     /    \ ")
print("                    77     3")
print("                   / \    / \ ")
print("                  /   \   | | ")
print("                 33    9  1 5")
print("                  \ ")
print("                   54")

print("Con inorder")
T.inorder()

print("Sostituiamo")
T.numFo()
print("Dovremo ottenere")
print("                        4 ")
print("                      /  \ ")
print("                     /    \ ")
print("                     2     2")
print("                   / \    / \ ")
print("                  /   \   | | ")
print("                  1    1  1 1")
print("                  \ ")
print("                   1 ")


print("Con inorder")
T.inorder()
